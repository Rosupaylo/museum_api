from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = "variant_18.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return "Museum API is running"


# GET - отримати всі експонати
@app.route("/api/exhibits", methods=["GET"])
def get_exhibits():
    conn = get_db_connection()
    exhibits = conn.execute("SELECT * FROM exhibits").fetchall()
    conn.close()

    return jsonify([dict(row) for row in exhibits])


# GET - отримати один експонат за id
@app.route("/api/exhibits/<int:exhibit_id>", methods=["GET"])
def get_exhibit(exhibit_id):
    conn = get_db_connection()
    exhibit = conn.execute(
        "SELECT * FROM exhibits WHERE id = ?",
        (exhibit_id,)
    ).fetchone()
    conn.close()

    if exhibit is None:
        return jsonify({"error": "Exhibit not found"}), 404

    return jsonify(dict(exhibit))


# POST - додати новий експонат
@app.route("/api/exhibits", methods=["POST"])
def add_exhibit():
    data = request.get_json()

    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO exhibits
        (id, collection_id, inventory_code, exhibit_name, material,
         estimated_year, preservation_state, exhibit_status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["id"],
            data["collection_id"],
            data["inventory_code"],
            data["exhibit_name"],
            data["material"],
            data["estimated_year"],
            data["preservation_state"],
            data["exhibit_status"]
        )
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Exhibit added successfully"})


# PUT - оновити експонат
@app.route("/api/exhibits/<int:exhibit_id>", methods=["PUT"])
def update_exhibit(exhibit_id):
    data = request.get_json()

    conn = get_db_connection()
    conn.execute(
        """
        UPDATE exhibits
        SET exhibit_name = ?,
            material = ?,
            preservation_state = ?,
            exhibit_status = ?
        WHERE id = ?
        """,
        (
            data["exhibit_name"],
            data["material"],
            data["preservation_state"],
            data["exhibit_status"],
            exhibit_id
        )
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Exhibit updated successfully"})


# DELETE - видалити експонат
@app.route("/api/exhibits/<int:exhibit_id>", methods=["DELETE"])
def delete_exhibit(exhibit_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM exhibits WHERE id = ?", (exhibit_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Exhibit deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)