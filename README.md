# todoapp
# Django TodoApp


## The App Preview
![TodoApp](https://github.com/tijjken/TodoApp/blob/master/static/TodoApp2.png)


### Setup
To get this repository, run the following command inside your git enabled terminal

```
$ git clone https://https://github.com/tijjken/todoapp.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory and run the following command

```
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```
$ python manage.py migrate
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```
$ python manage.py runserver
```

### visit http://127.0.0.1:8000 to start the App
