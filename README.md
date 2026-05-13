# Museum API

Лабораторна робота №8 з дисципліни "Організація баз даних".

## Варіант 18 - Музей

Проєкт містить REST API для роботи з базою даних музею.

## Технології

- Python
- Flask
- SQLite
- GitHub Actions

## Основні файли

- app.py - код REST API
- variant_18.db - база даних SQLite
- requirements.txt - залежності Python
- .github/workflows/ci.yml - файл CI/CD

## API

- GET /api/exhibits - отримати всі експонати
- POST /api/exhibits - додати експонат
- PUT /api/exhibits/<id> - оновити експонат
- DELETE /api/exhibits/<id> - видалити експонат

CI/CD перевірка виконується автоматично через GitHub Actions.