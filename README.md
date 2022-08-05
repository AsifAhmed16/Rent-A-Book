# Rent-A-Book

```
A very simple library where user can select a book to read authorized by admins.

```

```
TECHNOLOGIES USED ::::

● Python, Django 
● PostgreSQL
● Fixtures

```

```
Functionalities ::::

● Request for a book
● Pick a book from list
● Responsive CSS
● Easy setup/deployment

```

# Step 1: DB Create

```
Create a database - 'rent_a_book_db'
sudo -i -u postgres
psql
CREATE DATABASE rent_a_book_db;
```

# Step 2: Creating a Virtual Env and Requirements.txt file for installing dependencies

```
python -m venv venv
pip install requirements.txt
```

# Step 3: Migration

```
python manage.py makemigrations
python manage.py migrate

```

# Step 4: Data load using fixtures

```
python manage.py loaddata book

```

# Run commands

```
python manage.py runserver
Local: http://localhost:8000
```

# Additional Requirements

```
Creation of a user entry with the registration form provided within the app by considering validations.
```

# Additional features for future

```

● User reminder for expiration and calculatiuon of penalties
● Online payment using a gateway
● Dockerizing
● python unittest 

```


# Conclusion

```

# My Focus
● My initial thoughts was to establish main features as fast as I can.
● Using as much as cutting edge technologies I can attach through the application. 
● Establish the whole application with a monolyth architecture and intersect features to microservice over time.
● This library can be used with multiple architecture as a python standard library package.
● Just in case of scheduling task, a celery and celery-beat third party library is very much useful.

# Field of Improvement
More user interactive application with new features. Will be initiated with celery and ssl support in future.

```
