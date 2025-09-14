#Flask API
This Flask API will return data that we scraped from bbb.org using the scrapy scraper.

Installation Steps:

1. Clone this repo.
2. Create a virtual environment using below command
```bash
python3 -m pip venv virtualenv
```
3. Activate the virtualenv using below command.
In Linux
```bash
source virtualenv/bin/activate
```
In Windows
```bash
\virtualenv\Scripts\Activate
```
4. Install all the packages using below command.
```bash
python3 -m pip install -r requirements.txt
```
5. Then import the database.sql database.
6. Now use the .env.example file and create .env file. You will need a valid mysql db string and a 32 digit secret key which can be any random string.
7. Now you are ready to start the API using the below command.
```bash
python3 run.py
```

After following all the steps you can import the flask API's postman collection and test the API's.
