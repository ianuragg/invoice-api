# Invoice API

Invoice API is a Django project that allows users to create, update, and retrieve invoices and invoice details using a single URL /invoices/. It uses Django REST framework to create RESTful APIs for the invoice models, and supports nested serializers for the invoice details.

## Installation and usage

To install and run this project, follow these steps:

- Clone this repository to your local machine using `git clone https://github.com/ianuragg/invoice-api.git`
- Create a virtual environment using `python -m venv env` and activate it using `source env/bin/activate`
- Install the required packages using `pip install -r requirements.txt`
- Run the migrations using `python manage.py migrate`
- Start the development server using `python manage.py runserver`
- Access the API endpoints using `http://localhost:8000/invoices/`

## Features

This project provides the following features:

- Create an invoice with invoice details using a POST request to the /invoices/ endpoint with the following JSON data format:

```json
{
    "date": "2023-10-03",
    "customer_name": "Anurag Chauhan",
    "details": [
        {
            "description": "Product A",
            "quantity": 2,
            "unit_price": 100.00,
            "price": 200.00
        },
        {
            "description": "Product B",
            "quantity": 1,
            "unit_price": 50.00,
            "price": 50.00
        }
    ]
}
