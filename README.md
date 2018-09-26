# Shopping List Api

## Requirements
- [Python 3](https://www.python.org)
- [Django](https://www.djangoproject.com)
- [Postgresql](https://www.postgresql.org/)

## Running the application
To run this application, clone the repository on your local machine and run the following commands.
```sh
    $ git clone https://github.com/Collinslenjo/shopping.git
    $ cd shopping
    $ virtualenv virtenv
    $ source virtenv/bin/activate
    $ pip install -r requirements.txt
    $ ./manage.py makemigrations
    $ ./manage.py migrate
    $ ./manage.py runserver
```
#### Endpoints of a user authentication and signup
|End point | Public Access|Action
|----------|--------------|------
auth/login | True | Login a user
auth/logout | False | Logout a user
auth/reset-password | False | Reset a user password

#### Endpoints to create, update, view and delete a shopping list & it's items
|End point | Public Access|Action
|----------|--------------|------
api/<v(1,2,3,4)>/lists/ | False | Create and Retrieve shopping lists
api/<v(1,2,3,4)>/lists/<int:list_id> | False | View a shopping list and all it's items also Update & Delete Shopping list
api/<v(1,2,3,4)>/items/ | False | View all shopping list items
api/<v(1,2,3,4)>/items/<int:item_id>/ | False | Retrieve Update and Delete a shopping list item