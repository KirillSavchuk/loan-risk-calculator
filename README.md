# Loan Risk Calculator
## About
The following tool has an alternative client recognition scoring model in order to predict the customer's pay-out behaviour and thus reduce the organization's costs.

## Technologies
This project is created with:
* **Python 3.8.0** - back-end programing language
* **Django 3.2**  - WEB framework
* **HTML/CSS/JS/jQuery** - front-end programming languages
* **SQLite 3** - relational database

## Hot to run application
### Install dependencies
##### Python
Download and install the latest **Python** version from [official page](https://www.python.org/downloads/).
##### pip
Download and install the latest **pip** *(package installer for Python)* version from [official page](https://pip.pypa.io/en/stable/installing/).

After **pip** is installed, application requirements has to be installed by running the following command from the root directory of the project:
```python
pip install -r requirements.txt
```

### Run application
Open **CMD** or **PowerShell** window in the root directory of this project.

Run the following commands:
##### 1. Prepare database migration scripts: 
```python
python manage.py makemigrations
```
##### 2. Create database tables from prepared migrations:
```python
python manage.py migrate
```
##### 3. Create admin user:
```python
python manage.py createsuperuser --username admin --email admin@email.com
```
You can choose whatever *username* and *email* you wish.

After command execution, you will be asked to provide user password 2 times.
##### 4. Run application:
```python
python manage.py runserver
```
After application is started, you should see something like that:
```
Starting development server at http://127.0.0.1:8000/
```
Copy the provided URL and open it in your browser - here you should see started application.

### Upload data
##### 1. Config files upload
All of your configuration files must be located 
```
/loans/config/import?files=config,age,monthly-income,monthly-expenses,free-money,dependents,external-liabilities,finished-loans,prev-loan-interaction,last-contract-status,debt-days
```

##### 2. Loan database upload







