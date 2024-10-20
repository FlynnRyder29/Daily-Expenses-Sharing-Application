Daily Expense Sharing Application
This is a backend service for a daily expense-sharing application. It allows users to add expenses and split them by three methods: exact amounts, percentages, and equal splits. The application provides user management, expense management, and the ability to generate balance sheets.

Features
User management (create, retrieve user details)
Expense management (add, retrieve expenses)
Split expenses equally, by exact amounts, or by percentages
Download balance sheets
Input validation and error handling
User authentication (optional)
Requirements
Python 3.8+
FastAPI
SQLAlchemy
Uvicorn
SQLite (for local development)
Pytest (for running tests)
Installation
Follow these steps to set up the project on your local machine.

1. Clone the repository
bash
Copy code
git clone https://github.com/FlynnRyder29/Daily-Expenses-Sharing-Application.git
cd Daily Expenses Sharing Application
2. Create a virtual environment
bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:
bash
Copy code
.\venv\Scripts\activate
Mac/Linux:
bash
Copy code
source venv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Set up the Database
The application uses SQLite for the local environment. To set up the database, run the following commands:

bash
Copy code
alembic upgrade head
This will create the necessary database tables.

5. Run the Application
Use Uvicorn to run the FastAPI application:

bash
Copy code
uvicorn app.main:app --reload
The app will be available at http://127.0.0.1:8000.

6. API Endpoints
You can interact with the API using the following endpoints:

User Endpoints:

POST /users/: Create a new user
GET /users/{user_id}: Get user details
Expense Endpoints:

POST /expenses/: Add a new expense
GET /expenses/user/{user_id}: Retrieve expenses for a specific user
GET /expenses/: Retrieve all expenses
GET /expenses/download/{user_id}: Download balance sheet for a user
For full API documentation, you can access the Swagger UI at:

arduino
Copy code
http://127.0.0.1:8000/docs
7. Run the Tests
You can run unit tests using pytest:

bash
Copy code
pytest
Ensure that you have pytest installed in your virtual environment by running:

bash
Copy code
pip install pytest
8. Database Migrations
This project uses Alembic for database migrations. If you modify the database schema, create a new migration script:

bash
Copy code
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
9. Example Environment Variables
The application can use environment variables for configuration. Create a .env file in the root directory and include variables like:

perl
Copy code
DATABASE_URL=sqlite:///./sql_app.db
You can configure other environment variables as needed, such as for authentication and database connections.

Contributing
Feel free to fork the repository, make improvements, and create a pull request. All contributions are welcome!

License
This project is licensed under the MIT License.

Make sure to adjust the paths and repository URL according to your setup. This README.md provides clear instructions for setting up, running, and testing the application.