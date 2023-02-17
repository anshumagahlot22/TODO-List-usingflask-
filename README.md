# TODO-List

Python Version:
This app was developed and tested with Python version 3.11.2


Running the Application:
To run the application, you can follow these steps:
1. Install the required Python modules by running the following command in your terminal:
	pip install -r requirements.txt
This will install all the external modules needed to run the app.
2. Create the database by running the following command in your terminal:
	python create_db.py
This will create a SQLite database in the current directory named database.db.
3. Start the application by running the following command in your terminal:
		python app.py
In your web browser, go to http://localhost:5000 to access the app. From there, you can add new todos by submitting a form with a name field.

DESCRIPTION:
This project is a simple TODO list app built using Python and the Flask web framework. The app provides a web-based interface for creating and managing a list of tasks or to-do items. The app stores all the to-do items in a SQLite database.
Here's a high-level overview of the app's functionality:
Users can add new to-do items to the list by submitting a form with a name field.
The app will create a new to-do item in the database and display the updated list of to-do items.
Users can view the list of all to-do items on the homepage of the app.
The app uses RESTful API endpoints to create and read data in the database.
The app uses Flask-SQLAlchemy to manage the database and Flask-Marshmallow to serialize and deserialize data.
The app also includes a requirements.txt file that lists all the external modules used in the project.
Overall, this app provides a simple, easy-to-use interface for managing a list of to-do items. It's a great example of how to use Flask to build a web app that communicates with a database via RESTful API endpoints
