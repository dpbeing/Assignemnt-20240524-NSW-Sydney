# Assignemnt-20240524-NSW-Sydney

## Description
This project demonstrates an ETL (Extract, Transform, Load) pipeline using a Test-Driven Development (TDD) approach. The pipeline reads data from a CSV file, transforms it, and loads it into a MongoDB or JSON file.


## Requirements
- Python 3.8+
- Docker
- Docker Compose

## Setup and Run

1. Build and run the Docker containers:
   ```sh
   docker-compose up --build



# ETL Pipeline with Docker Compose

This project implements an ETL (Extract, Transform, Load) pipeline using Docker Compose. The pipeline reads data from a CSV file, transforms it, and loads it into a predefined collection as a JSON document collection on disk.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone this repository:

   ```sh
   git clone https://github.com/dpbeing/Assignemnt-20240524-NSW-Sydney.git
   :
   ```

2. Place your CSV file (`members-data.csv`) in the project root directory.

## Usage

### 1. Running the ETL Pipeline
To load the transformed data as a JSON document collection on disk:

```sh
docker-compose -f docker-compose.json.yml up --build
```

This README provides clear instructions for setting up and running the ETL pipeline using Docker Compose, along with customization options for database configuration and output file path.

### 2. Verifying the Output

- If loading data into MongoDB, you can use a MongoDB client to verify that the data has been inserted into the specified collection.
- If storing data as a JSON document collection, you can find the output JSON file named `output.json` in the project root directory.

### 3. Customization
- **Output File Path:** If you want to change the output file path for storing the JSON document collection, you can modify the `docker-compose.json.yml` file accordingly.

## Notes

- Ensure that your CSV file follows the required format specified in the assignment.
- For any issues or questions, please open an issue in this repository.

## Credits

This ETL pipeline project was created by Deep Mehta.
``

This README provides clear instructions for setting up and running the ETL pipeline using Docker Compose, along with customization options for database configuration and output file path.