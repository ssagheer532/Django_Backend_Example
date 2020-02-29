## Django Back-End Example

This API is built with django with a postgres database. Main API logic is in `MH_Backend_Exercise/modernHealth/programLibrary/views.py`

Instructions: 

1. Create a virtual environment and source it by running `python -m venv venv` followed by `source venv/bin/activate`.

2. Cd into ` MH_Backend_Exercise` and install all python requirements: `pip install -r requirements.txt`

3. Install postgress and create a postgres database. This guide assumes you already have postgres installed.  Run `psql -U <USER_NAME>` to login and run `create database <YOUR_DB_NAME>;` to create a database. 

4. Export the following database environment variables your valid values for Django to use: 

 `export DATABASE_USR=`

 `export DATABASE_PWD=`

 `export DATABASE_NAME=`


5. Create and run migrations. In directory backendApp, run `python manage.py makemigrations` to generate the SQL commands to setup the database and `python manage.py migrate` to apply those SQL commands

6. At this point everything is setup! There are two ways to test this api: 

    1. The first way to test the api is to just run `python manage.py test` to run tests located in `modernHealth/programLibrary/tests.py`. There are three unit tests which test basic functionality and error handling. 

    2.  The second way to test the api is to spin up a server and manually hit the api. First, load the fixture data by running `python manage.py loaddata dummyData.json`. Now run ` python manage.py runserver` to start the server. On the console Django should say what address the server is running on (in my case it is `http://127.0.0.1:8000/`). To hit the api, go to your browser and paste this link:  `http://127.0.0.1:8000/modernHealth/programlibrary/get/program1`. The last variable (`program1`) is the name of the program you want to search for.  
