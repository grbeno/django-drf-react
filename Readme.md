##### Django-Django REST framework-ReactJs sample to develop web applications

This sample project is based on Django, Django REST framework (backend) and ReactJS library (frontend). The sample contains a basic setup to develop custom web applications.

###### Tools & requisites
- Windows
- PowerShell
- Git
- Python >=3.10
- pipenv
- nvm
- nodejs

###### How to use this sample
- Download Zip file from the repository
- Unpack the Zip file and rename the folder
- Create virtual environment: 
  - $ cd <your-project-folder> 
  - $ pipenv shell
- Create .env file (without any extension)
- Generate a secret key: 
  - $ python -c 'import secrets;print(secrets.token_urlsafe())'
- Add the next variables to it:
  - export DEBUG=True
  - export SECRET_KEY=/your-generated-secret_key/

###### Install nvm and nodejs
- If you have already installed nvm and nodejs then ignore the next steps!
- [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows)
- [download & install nvm-setup.zip](https://github.com/coreybutler/nvm-windows/releases)
- restart the terminal/powershell
- nvm install /node-version-number/
- [download & install nodejs](https://nodejs.org/en/download)
- return to your project folder using cd ...

###### Continue the setup
- $ npm install axios
- $ pipenv install -r requirements.txt
- $ python manage.py migrate
- $ python manage.py createsuperuser
- localhost:8000/admin/
  - create a todo to check if everything is okay

###### Important
- $ npm run build: if you modify something in React
- '$': a command in terminal/powershell