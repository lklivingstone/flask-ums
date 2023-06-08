# Flask UMS

This is a Flask project that includes instructions on how to set up and run the project locally.

## Clone the Repository

To get started, clone this GitHub repository to your local machine using the following command:

```
git clone https://github.com/lklivingstone/flask-ums.git
```

Set Up a Virtual Environment
It is recommended to use a virtual environment to isolate the project's dependencies. Follow these steps to create and activate a virtual environment:

Change into the project directory:

```
cd flask-ums
```

Create a virtual environment using venv or virtualenv. Run one of the following commands:

For venv (Python 3):
```
python -m venv env
or 
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
This will create the necessary database tables.
```
mkdir instance
flask --app src init-db
```

```
touch .env
```

If it does not work:
Create a file in root directory with filename: ".env"
Copy paste the following content inside the .env file:

```
export SECRET_KEY=123
export JWT_SECRET_KEY='lakfghnolvnsdvsa'
```

Run the Development Server

Finally, start the Flask development server to run the project locally:
```
flask run
```

The development server should start running at http://127.0.0.1:5000/. You can check the console for the url.

That's it! You can now access the Flask project in your web browser and begin development or testing.

## ENDPOINTS:

### REGISTER User:

POST [http://127.0.0.1:5000/api/auth/register](http://127.0.0.1:5000/api/auth/register)

Request Body:
```
{
    "username": {username},
    "password": {password}
}
```

Example:
```
{
    "username": "lklivingstone1",
    "password": "lklivingstone"
}
```

### Login User:

POST [http://127.0.0.1:5000/api/auth/login](http://127.0.0.1:5000/api/auth/login)

Request Body:
```
{
    "username": {username},
    "password": {password}
}
```

Example:
```
{
    "username": "lklivingstone1",
    "password": "lklivingstone"
}
```

### CREATE Task:

POST [http://127.0.0.1:5000/api/task](http://127.0.0.1:5000/api/task)

Request Body:
```
{
  "title": "Task Title 2",
  "description": "Task Description",
  "due_date": "2023-06-10",
  "status": "Incomplete"
}
```

Headers:
```
Authorization : Bearer {access_token}
```

Example:
```
{
  "title": "Task Title 2",
  "description": "Task Description",
  "due_date": "2023-06-10",
  "status": "Incomplete"
}
```

### GET ALL Tasks (with pagination):

GET [http://127.0.0.1:5000/api/tasks?page=3&per_page=3](http://127.0.0.1:5000/api/tasks?page=3&per_page=3)

Params:
```
{
  page : {page_number},
  per_page : {per_page_number}
}
```

Headers:
```
Authorization : Bearer {access_token}
```

### GET Task:

GET [http://127.0.0.1:5000/api/task/2](http://127.0.0.1:5000/api/task/2)


Headers:
```
Authorization : Bearer {access_token}
```


### UPDATE Task:

PUT [http://127.0.0.1:5000/api/task/2](http://127.0.0.1:5000/api/task/2)


Headers:
```
Authorization : Bearer {access_token}
```

Request Body (Example):
```
{
  "title": "Updated Title",
  "description": "Task Description",
  "due_date": "2023-06-10",
  "status": "Incomplete"
}
```

### DELETE Task:

DELETE [http://127.0.0.1:5000/api/task/2](http://127.0.0.1:5000/api/task/2)


Headers:
```
Authorization : Bearer {access_token}
```
