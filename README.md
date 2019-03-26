# REBBIT

## Neighbourhood is a python app which keeps neighbours and friends up to date with what is happening in their hood.Its a loop af what happens around 

### March 11th, 2019

#### By **[Mugo Ndungu](https://github.com/mugo-ndungu)**

## Description

Neighbourhood is a python app which keeps neighbours and friends up to date with what is happening in their hood.Its a loop af what happens around to visit the site Click [here](https://) to see the live site

## Setup and installation

- Clone the Repo uding the following command:
  `git clone https://github.com/Mugo-Ndungu/neighbourhood.git
- Activate virtual environment using python3.6 as default handler by running
  `python3.6 -m venv virtual` then enter the virtual environment using `source virtual/bin/activate`
- Download the latest version of pip in the virtual environment: `$ curl https://bootstrap.pypa.io/get-pip.py | python`

- Install all application dependancies
  `pip install -r requirements.txt`

- Create the Database
  -On the terminal,run `psql`

  - Create a database by typing
    `CREATE DATABASE awards;` for example.

- Create a .env file and add the following:

  - SECRET_KEY = `<Secret_key>`
  - DB_NAME = `awards`
  - DB_USER = `<Username>`
  - DB_PASSWORD = `your db password`
  - DEBUG = `True`

- Run Initial Migration
  `python3.6 manage.py makemigrations <name of the app>`
  `python3.6 manage.py migrate`

- Run the app
  `python3.6 manage.py runserver`
  `Open terminal on localhost:8000`

## User Stories

The application user is able to:

- Create an account and confirm through email verification.
- Sign in to the application to start using.
- Post neighbour hood you are currently in
- View stories posted within your neighbour hood.
- Search for neighbour hood
- View my profile page.

## Admin

The application admin is able to:

- Regulate neighbour hoods uploaded deleting them from the admin dashboard.
- Close a users account.

## Specifications

| Behavior                  | Input                          | Output                                 |
| ------------------------- | ------------------------------ | -------------------------------------- |
| Signup                    | string text                    | Creates user account                   |
| Login                     | string text                    | logs in to user account                |
| Submit new neighbour hood post   | upload neighbour hood                   | new neighbour hood post from user               |
| Add comment to neighbour hood post | String text                    | New comment to neighbour hood post selected     |
| View posted neighbour hood post    | Click on neighbour hood post  | Display neighbour hood posts in that    |
| View user neighbour hood post      | Click on user profile          | Display neighbour hood posts posted by the user |

## Technologies Used

- Python 3.6.6(Django Framework)
- HTML5
- CSS3
- Bootstrap4
- Postgresql
- Heroku(Deployment)
- Visual Studio Code text editor

## Known Bugs

No known bugs so far.Contact me if you come across any.

## Support and contact details

Contact me on [Email](twinnymugo@gmail.com) for any comments, reviews or advice.

### License

Copyright (c) **Mugo Ndungu**