# Weather Data Pipeline using AWS and Snowflake

## Project Overview

This project implements an end-to-end weather data pipeline that automatically collects real-time weather information from the OpenWeatherMap API, stores it in AWS DynamoDB, exports the data to Amazon S3 using DynamoDB Streams and AWS Lambda, and finally loads the data into Snowflake for analytics.

## Architecture

OpenWeatherMap API → AWS Lambda (Weather Collector) → DynamoDB → DynamoDB Streams → AWS Lambda (Stream Processor) → Amazon S3 → Snowflake Stage → Snowpipe → Snowflake Table

## Technologies Used

* AWS Lambda
* Amazon DynamoDB
* DynamoDB Streams
* Amazon S3
* Amazon EventBridge
* Snowflake
* Snowpipe
* Python
* Boto3
* Requests
* OpenWeatherMap API

## Project Workflow

### Step 1: Weather Data Collection

A scheduled AWS Lambda function fetches weather data from the OpenWeatherMap API every 5 minutes.

Collected fields:

* City
* Temperature
* Humidity
* Weather Description
* Timestamp

### Step 2: Store Data in DynamoDB

The weather data is stored in a DynamoDB table named:

weather_table

### Step 3: DynamoDB Streams

DynamoDB Streams capture INSERT and MODIFY events whenever new weather data is added.

### Step 4: Export Data to Amazon S3

A second Lambda function processes DynamoDB Stream events and converts records into JSON files.

Example:

{
"city": "Kochi",
"temperature": "31.5",
"humidity": "75",
"weather": "broken clouds",
"timestamp": "2026-06-01T10:00:00"
}

The JSON files are stored in:

s3://weather-project-bucket-123/weather-data/

### Step 5: Load Data into Snowflake

Snowflake accesses the S3 bucket through an external stage.

Data is loaded into:

weather1_db.weather1_schema.weather1_table

### Step 6: Automated Ingestion using Snowpipe

Snowpipe automatically loads newly uploaded JSON files into Snowflake for near real-time analytics.

---

## AWS Services Used

### Lambda Function 1

Purpose:

* Fetch weather data from OpenWeatherMap API
* Insert data into DynamoDB

### Lambda Function 2

Purpose:

* Read DynamoDB Stream events
* Convert records into JSON
* Upload JSON files to S3

### DynamoDB

Purpose:

* Store weather data

### EventBridge

Purpose:

* Trigger Lambda Function 1 every 5 minutes

### S3

Purpose:

* Store weather JSON files

---

## Snowflake Components

### Database

weather1_db

### Schema

weather1_schema

### Table

weather1_table

### Stage

my_stage

### Pipe

weather_pipe

---

## Project Structure

weather-data-pipeline/

├── lambda-weather-api/
│   └── lambda_function.py
│
├── lambda-dynamodb-to-s3/
│   └── lambda_function.py
│
├── snowflake/
│   ├── create_database.sql
│   ├── create_stage.sql
│   ├── create_table.sql
│   └── snowpipe.sql
│
├── requirements.txt
├── architecture.png
└── README.md

---

## Python Dependencies

requirements.txt

boto3
requests

Install:

pip install -r requirements.txt

---

## Sample Snowflake Query

SELECT
data:city::STRING AS city,
data:temperature::FLOAT AS temperature,
data:humidity::INTEGER AS humidity,
data:weather::STRING AS weather
FROM weather1_table;

---

## Key Features

* Fully serverless architecture
* Automated weather data collection
* Near real-time data ingestion
* Event-driven processing using DynamoDB Streams
* Scalable cloud-native design
* Snowflake analytics integration

---

## Future Enhancements

* Support multiple cities
* Real-time dashboard using Streamlit
* Data visualization with Power BI
* Historical weather trend analysis
* Automated alerts and monitoring

---

## Author

Nived P Anil

AWS | Snowflake | Data Engineering | Cloud Projects
