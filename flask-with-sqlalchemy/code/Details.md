# Flask-SQLAlchemy

- Flask-SQLAlchemy is used to make the mapping in the REST API more convenient for the developers. 
- This folder will detail about every thing we make changes in this `flask-with-sqlalchemy` folder, since it more advanced than the previous folders

## Resource Folder [Package]

- Resources is the external representation of an entity
- It acts as a package for the files which inherits `Resources`. 
- In our case `user.py` has `UserRegister` and `item.py` consists of Resource inherited classes only.
- In our to make the code look cleaner, we have done this
- Now since the `resource` consists files, which now acts as a Resource packages, to import them, we need to do `<foldername>.<filename>`, in our case it is `resource.user` and `resource.item`
- It has `__init__.py` because it tell the files to how or where to look into the file

## Models Folder [Package]

- Models is nothing but our/internal representation of an entity
- `user.py` consists of a `User` class which doesn't implements Resources. It is more of a like a representation and how we can model the User for storing the User data and certain operation 
- Model is essentially a helper, that gives us more felxibility in our program without polluting the `Resources`, which our client interact with
- Model and Resources can be linked, in order to give the data to the client