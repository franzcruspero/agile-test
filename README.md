# Agile Values and Principles List App

This repository is used for both backend and frontend of a list app developed with VueJS and Django.

# Backend

## Local Environment Setup

### Features

1. **Rest API** login using [Django Rest Framework]

### Requirements

1. Python 3.9.2
2. Pipenv ver. 2020-11-15 and up

### Installation

1. Install `pipenv`
2. Clone this repo and `cd backend`
3. Run `pipenv install`

### Getting Started

1. Run `pipenv shell`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`

### Running unit tests

1. Run `pipenv shell`
2. Run `python manage.py test`

### Notes

**A fixture json file has already been prepared to pre-fill the backend database with the 4 values and 12 principles of Agile Software Development. The fixture file will be ran as a migration**

# Frontend

1. NodeJS ver. 14.17.5
2. Vue CLI ver. 4.5.3

### Installation

1. Install Vue CLI
2. Clone this repo and `cd frontend`
3. Run `npm install`

### Getting Started

1. Run `npm run serve`

### Running unit tests

1. Open terminal and redirect to the frontend directory
2. Run `npm run test:unit`
