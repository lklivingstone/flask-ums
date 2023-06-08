# Django Todo

This is a Django project that includes instructions on how to set up and run the project locally.

## Clone the Repository

To get started, clone this GitHub repository to your local machine using the following command:


git clone https://github.com/lklivingstone/django-todo.git

Set Up a Virtual Environment
It is recommended to use a virtual environment to isolate the project's dependencies. Follow these steps to create and activate a virtual environment:

Change into the project directory:

```
cd your-project
```

Create a virtual environment using venv or virtualenv. Run one of the following commands:

For venv (Python 3):
```
python3 -m venv env
```
For virtualenv:
```
virtualenv env
```
Activate the virtual environment:

On macOS/Linux:
```
source env/bin/activate
```
On Windows:
```
.\env\Scripts\activate
```
Install Dependencies

Once the virtual environment is activated, install the project dependencies using pip:
```
pip install -r requirements.txt
```
Apply Migrations

Before running the project, apply the database migrations using the following command:
```
python manage.py makemigrations
python manage.py migrate
```
This will create the necessary database tables based on the project's models.

Run the Development Server

Finally, start the Django development server to run the project locally:
```
python manage.py runserver
```
The development server should start running at http://127.0.0.1:8000/

That's it! You can now access the Django project in your web browser and begin development or testing.