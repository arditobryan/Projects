# Deploy Your Flask Project To Heroku

This is an example repository that uses **Flask** and **Gunicorn** to deploy your project to Heroku.

# Problematic

Currently, Flask is not suitable for a production environment and it doesn't scale well (see [flask documentation on deployment](http://flask.pocoo.org/docs/1.0/deploying/)).

If we want to deploy our project to Heroku, we need a **Web Server Gateway Interface** (WSGI) such as **Gunicorn**.

# Solution

To overcome this obstacle we can use **Gunicorn** to aide us deploy our Flask project into a Heroku app.

This guide _assumes_ that you already had gone through the process of installing and authenticating the [Heroku Toolbelt](https://devcenter.heroku.com/articles/heroku-cli).

## Fork The Repository

You should **fork the repository** and then **clone it** so you can manage your own repo and use this only as a template.

```
$ git clone https://github.com/your_username/flask-heroku-example.git
```

At this point you should be able to modify the Flask app `app.py`:
```python
"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
```

**WARNING:** If you change the file name (`app.py`) and the Flask **app** (`app = Flask(__name__)`) then remember to change Heroku's Procfile:
```
web: gunicorn <filename>:<app_name>
```

## Create Your Heroku App

You can also leave `your_app_name` empty if you want Heroku to create a randomized name.

```
$ heroku create your_app_name
Creating app... done, ⬢ your_app_name
https://your_app_name.herokuapp.com/ | https://git.heroku.com/your_app_name.git
```

## Deploy Your Project

Your project is going to be deploy using **gunicorn** as a web server using the **Procfile** and it will be detected as a Python project since it is declared in **runtime.txt**

* **Add necessary files and commit them**
```bash
$ git add -A
$ git commit -am "finished flask project"
```

* **Push to Heroku**
```bash
$ git push heroku master
-- SNIP --
remote: -----> Python app detected
remote: -----> Installing python-3.6.5
remote: -----> Installing pip
remote: -----> Installing dependencies with Pipenv 11.8.2…
remote:        Installing dependencies from Pipfile.lock (59a99c)…
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 53.9M
remote: -----> Launching...
remote:        Released v3
remote:        https://your_app_name.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/your_app_name.git
 * [new branch]      master -> master
```

That's it, you can visit your app now with `heroku open`.
