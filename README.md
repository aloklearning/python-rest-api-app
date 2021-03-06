# PYTHON REST API USING FLASK

[![dependency](https://img.shields.io/github/pipenv/locked/dependency-version/metabolize/rq-dashboard-on-heroku/flask)](https://img.shields.io/github/pipenv/locked/dependency-version/metabolize/rq-dashboard-on-heroku/flask)
[![license-mit](https://img.shields.io/github/license/aloklearning/python-rest-api-app)](https://img.shields.io/github/license/aloklearning/python-rest-api-app)
[![githubbuild](https://img.shields.io/appveyor/build/gruntjs/grunt)](https://img.shields.io/appveyor/build/gruntjs/grunt)
[![pyversion](https://img.shields.io/pypi/pyversions/django)](https://img.shields.io/pypi/pyversions/django)

- This project is a learning project created on the basis of learning `backend development` from the Udemy course **REST APIs with FLASK and PYTHON**
- This will consists of normal Flask level backend dev
- Using Flask-JWT, Flask-RESTful for advanced backend operations
- Using Sqlite3 for Database Management
- Using SQLAlchemy for storage simplification
- Developing more secure REST APIs

## Prerequisites

- [X] Make sure you have Flask installed in your system, which will act a server for API work
- [X] Python is installed, better to make use of the latest python only, that is **Version 3.x**
- [X] For advanced operations, we can install Flask-RESTful for using `Resource`, `Api`, `reqparser`
- [X] Flask-JWT is required for user authentication via JWT(JSON Web Token) token 

## Getting Started

- Make sure you are inside the project directory
- The python project runs on flask, using the command `python<version> app.py`
- `app.py` file consist of the basic operation with the usage of Flask
- `flask-restful-app` consists of the `code/new-app.py` contains the file with advanced operation with `flask-restful` and `flsak-jwt`
- `flask-with-sqldb` consists of same folders like, `code/new-app.py` with operation using `sqlite3`, which is used as our database. So this is not at all working volatile data now. The data is being stored in the `data.db` file, which is the DataBase file in this case
- Information for advanced operation is inside the [Commands.md](https://github.com/aloklearning/python-rest-api-app/blob/master/flask-restful-app/Commands.md)
- `flask-with-sqlalchemy` contains the folders having installed `Flask`, `Flask-JWT`, `Flask-RESTful` and `Falsk-SQLAlchemy` in the virtual envorinment. To install `SQLAlchemy`, just do `pip3/pip install Flask-SQLAlchemy` and it will be installed in your vritual environment
- To copy folder's content to another folder, here is the terminal command *For Mac* `cp <from-foldername>/* <To-Foldername>`. For example `cp ../flask-with-sqldb/code/* code/`
