CREATE OR REPLACE DATABASE weather1_db;
CREATE OR REPLACE SCHEMA weather1_schema;

USE DATABASE weather1_db;
USE SCHEMA weather1_schema;

CREATE OR REPLACE FILE FORMAT weather_json
TYPE = JSON;

CREATE OR REPLACE STAGE my_stage
URL = 's3://weather-project-bucket-123/weather-data/'
CREDENTIALS = (
    AWS_KEY_ID = '*****',
    AWS_SECRET_KEY = '*****'
)
FILE_FORMAT = weather_json;