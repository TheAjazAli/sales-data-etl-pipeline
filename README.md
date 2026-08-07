## Test

This is a test change.
# 📊 Sales Data ETL Pipeline

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python and PostgreSQL. The pipeline extracts raw sales data from a CSV file, performs data cleaning and transformation using Pandas, loads the processed data into PostgreSQL, and validates the output by connecting the database to Power BI for visualization.

The objective of this project is to showcase fundamental Data Engineering concepts such as data extraction, preprocessing, database integration, and preparing analytics-ready data.

---

## Architecture

```
                Raw Sales Dataset (CSV)
                         │
                         ▼
                 Extract (Pandas)
                         │
                         ▼
          Data Cleaning & Transformation
                         │
                         ▼
                PostgreSQL Database
                         │
                         ▼
          Power BI (Data Validation)
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- PostgreSQL
- SQLAlchemy
- Power BI
- Git
- VS Code

---

## ETL Process

### 1. Extract

The raw sales dataset was imported from a CSV file into a Pandas DataFrame using `pd.read_csv()`. Initial inspection was performed to verify the dataset structure, column names, data types, and overall quality.

Example:

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")
```

---

### 2. Transform

The extracted dataset was cleaned and transformed to improve data quality.

Transformations performed include:

- Handling missing values
- Removing duplicate records
- Correcting inconsistent values
- Standardizing column formats
- Converting data types where required
- Preparing the dataset for database loading

---

### 3. Load

The cleaned dataset was loaded into PostgreSQL using SQLAlchemy and Pandas.

```python
df.to_sql(
    "sales_data",
    con=engine,
    if_exists="replace",
    index=False
)
```

The destination table was automatically created based on the DataFrame schema.

---



## Output

The processed data is successfully stored inside PostgreSQL and can be queried using SQL.

The database is also connected to Power BI, demonstrating that the ETL pipeline produces analytics-ready data for business reporting.

---

## Skills Demonstrated

- ETL Pipeline Development
- Data Cleaning
- Data Transformation
- Data Preprocessing
- PostgreSQL Integration
- SQLAlchemy
- Pandas
- Database Loading
- Data Validation
- Data Engineering Fundamentals

---

## Future Improvements

Some enhancements that can be implemented in future versions include:

- Reading data directly from APIs
- Loading files from AWS S3
- Automated scheduling using Apache Airflow
- Processing large datasets using Apache Spark
- Data quality validation framework
- Logging and monitoring
- Incremental data loading
- Containerization using Docker

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Understanding the ETL lifecycle
- Working with real-world datasets
- Cleaning and transforming raw data
- Loading structured data into PostgreSQL
- Preparing data for analytics and reporting
- Building a foundational Data Engineering workflow

---

## Author

**Ajaz Ali**

Aspiring Data Engineer

Python | SQL | PostgreSQL | Hadoop | Apache Spark | Airflow | Snowflake
