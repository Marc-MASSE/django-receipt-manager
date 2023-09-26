# Receipt Manager

## Description
Application for managing receipts.

A receipt contains 3 pieces of information: date, title and amount.

## Installation

Install Python `3.11+`.

## Usage

```bash
python main.py  # or python3 main.py
```
The application will add employees randomly, either a commercial or a developer.
To add a new employee, press the enter key.
The application automatically stops when the society can no longer accept a new employee.

## Tests

```bash
pytest -v tests\
```

## Data

The number of offices and their composition can be found in the file :
**constants/data_for_initialisation.py**

## Django account

Superuser

## Database migration

In receiptmanager directory :
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

## Endpoints examples

#### superuser account ####

http://127.0.0.1:8000/admin/ </br>
To manage the database.




