# Web Project

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.1-green)](https://flask.palletsprojects.com/en/2.0.x/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3+-orange)](https://tailwindcss.com/)
[![Alpine.js](https://img.shields.io/badge/Alpine.js-3+-blue)](https://github.com/alpinejs/alpine)

## Description

Welcome to this web application built with Python (Flask) and HTML/CSS, leveraging the TailwindCSS and Alpine.js frameworks. It provides an intuitive interface to explore key data from the 2023 season of FIA Formula One©.

## Quick Start (first time)

1. Install the project dependencies using the requirements.txt file (optional: set up a Python virtual environment).
2. Run ```npm install``` in the project using Node.js.
3. Execute the docker-compose for the database.
   - For the first time, run the dumps stored in the ```sql``` folder (subsequently, the data mount allows persistence).
     - In order, execute:
       - f1db.sql
       - add_data.sql
4. Don't forget to create your .env file using the example file, specifying your own environment variables.

## Start Project

1. Run the main.py file.
2. In another terminal tab, run ```npm run tailwind``` (a script based on package.json to watch and hot-refresh Tailwind classes).
3. Visit http://localhost:5001 to explore your application.

## Informations

- Some data may be outdated (auto-generated)
- Flask 2.3.1 is used to fit with flask_table (deprecated since higher versions of Flask)

## Roadmap

- Refactor and clean up the code
- Add flags in driver standings
- Add logos in constructor files
- Add transitions on toasts
- Create a docker-compose to set up the entire development environment
- Position the footer at the bottom of the page when there is no scroll
- Restrict max page resizing in width to 550px
- Production state for the app (build)
