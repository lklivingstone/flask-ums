# Flask UMS

This is a Flask project that includes instructions on how to set up and run the project locally.

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


Before running the project, run the following command:
```
mkdir instance
flask --app src init-db
```

This will create the necessary database tables.


Run the Development Server

Finally, start the Flask development server to run the project locally:
```
flask run
```

The development server should start running at http://127.0.0.1:5000/. You can check the console for the url.

That's it! You can now access the Flask project in your web browser and begin development or testing.

## ENDPOINTS:
