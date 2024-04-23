# Fund Management System

## Overview

The Fund Management System is a web application developed to manage investment funds. It provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on investment funds and allows users to interact with the system programmatically.

## Features

- Retrieve a list of all funds
- Create a new fund
- Retrieve details of a specific fund using its ID
- Update the performance of a fund using its ID
- Delete a fund using its ID

## Technologies Used

- Python
- Django
- Django Rest Framework
- SQLite (for lightweight database)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/justinsoo96/fund-management.git
    cd fund-management
    ```
2. **Create Virtual Environment and activate:**
   ```bash
   python -m venv env
   source env/Script/activate
   ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    ```bash
    python manage.py makemigrations InvestmentFund
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the API at** `http://127.0.0.1:8000/gateway/funds/`.

7. **To access API documentation at** `http://127.0.0.1:8000/docs/`.

## API Endpoints

- `GET /funds/`: Retrieve a list of all funds
- `POST /funds/`: Create a new fund
- `GET /funds/<fund_id>/`: Retrieve details of a specific fund using its ID
- `PUT /funds/<fund_id>/`: Update the performance of a fund using its ID
- `DELETE /funds/<fund_id>/`: Delete a fund using its ID

## Testing

To run tests:

```bash
python manage.py test
```