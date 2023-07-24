### Django-Django REST framework-ReactJS sample

This sample project is based on Django (backend) and the ReactJS library (frontend) using Django REST framework. The project provides a basic setup for developing custom web applications.

#### Tools & requisites
- Windows
- PowerShell
- Git
- Python >=3.10
- pipenv
- nvm
- nodejs

---

### How to use the sample
- Download Zip file from the repository
- Unpack the Zip file and rename the folder
- Create virtual environment: 
  - $ `cd /your-project-folder/` 
  - $ `pipenv shell`
- Create .env file (without any extension)
- Generate a secret key: 
  - $ `python -c 'import secrets;print(secrets.token_urlsafe())'`
- Add the next variables to the .env file:
  - `export DEBUG=True`
  - `export SECRET_KEY=/your-generated-secret_key/`

#### Install nvm and nodejs
- If you have already installed nvm-windows and Node.js then you can ignore the next steps!
- [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows)
- [download & install nvm-setup.zip](https://github.com/coreybutler/nvm-windows/releases)
- restart the terminal/powershell
- $ `nvm install /node-version-number/`
- [download & install nodejs](https://nodejs.org/en/download)
- return to your project folder using cd ...

#### Continue the setup
- $ `npm install axios`
- $ `pipenv install -r requirements.txt`
- $ `python manage.py migrate`
- $ `python manage.py createsuperuser`
- localhost:8000/admin/
  - create a todo to ensure that everything is okay!

***

### Important notes
- $ `npm run build` /if you modify something in React/
- '$' refers to a command in terminal/powershell

### Deploying
---
### Prepare Django
---
$ `cd /your-project-path/`

$ `pipenv install dj_database_url, psycopg2`

*config/settings.py*
```
import dj_database_url
                
# DATABASE_URL => https://dashboard.heroku.com/apps
db_config = dj_database_url.config(conn_max_age=600, ssl_require=True)

if db_config:
    # Production
    DATABASES = {}
    DATABASES['default'] = db_config
else:
    DATABASES = {
        default': {
       	    'ENGINE':'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
$ `pipenv install whitenoise`

*config/settings.py*

```
INSTALLED_APPS = ['whitenoise.runserver_nostatic',]

MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware',]  # 2.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### Static assets

- $ `python manage.py collectstatic --noinput`

#### Procfile

- $ `pipenv install gunicorn`

  - `-web: gunicorn config.wsgi --log-file -`

#### Hosts

- `ALLOWED_HOSTS = ["127.0.0.1", "localhost", "<app-name>.herokuapp.com"]`

$ `pip freeze > requirements.txt`

---
### Prepare React
---
*package.json*

- Add to the end as the last {obj}

```
"engines": {
    "node": "18.16.1",
    "npm": "9.5.1"
},
```
---
### GitHub
---
#### Create a repository

$ `git add .`

$ `git commit -m "deploy-to-heroku"`

$ `git add remote ...`

$ `git branch -M main`

---
### Heroku
---
#### Sign up & login to [Heroku](https://www.heroku.com/)

- Create new app on Heroku

- Go to the dashboard/Settings/Config Vars/
  - `SECRET_KEY`, `DISABLE_COLLECTSTATIC=1`

- Download & install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

- Restart terminal

$ `heroku --version`

$ `heroku login`

$ `heroku git remote -a /app-name/`

#### Add buildpacks (choose one)

- Heroku UI
  - Settings/Buildpacks/heroku-nodejs/heroku-python

- Heroku CLI
  - $ `heroku buildpacks:add --index 1 heroku/nodejs`
  - $ `heroku buildpacks:add --index 2 heroku/python`

$ `git push heroku main`

$ `heroku run python manage.py migrate`

$ `heroku run python manage.py createsuperuser`

$ `heroku open`

