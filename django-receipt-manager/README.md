# Receipt Manager

## Description
Application CRUD for managing receipts.

A receipt contains 3 pieces of information: date, title and amount.
The date must be unique.

This application use Python 3.11, Django 4.2 and Bootstrap 5.

## Installation

Install Python `3.11+`.

## Usage

In receiptmanager directory :
```bash
python manage.py runserver
```
This application will be visible at this url :</br>
http://127.0.0.1:8000/

## Tests

In receiptmanager directory :
```bash
python manage.py test 
```

## Database migration

In receiptmanager directory :
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

## Endpoints examples

#### superuser account

http://127.0.0.1:8000/admin/ </br>
To manage the database.

#### Receipt list

http://127.0.0.1:8000/receipts/ </br>
Display the list of all receipts.

#### Receipt detail

http://127.0.0.1:8000/receipt/1/ </br>
Display all data about a receipt according to its id.

#### Create a new receipt

http://127.0.0.1:8000/receipt/create/ </br>
To create a new receipt. </br>
Please note, the date is in the format YYYY-MM-DD 
and it must not have already been used. 
The amount must have only 2 digits after the decimal point.

#### Update a receipt

http://127.0.0.1:8000/receipt/1/update </br>
To update a receipt according to its id.
Please note, the date is in the format YYYY-MM-DD 
and it must not have already been used. 
The amount must have only 2 digits after the decimal point.

#### Delete a receipt

http://127.0.0.1:8000/receipt/1/delete </br>
To delete a receipt according to its id.

#### Receipt totals

http://127.0.0.1:8000/receipt/totals/ </br>
Display the total of all receipts and a table containing the totals by month.
