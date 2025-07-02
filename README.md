# Real-Time Streaming Data Pipeline for Retail Orders

This project simulates a real-time data pipeline for a retail/ecommerce client, processing customer orders using Apache Kafka, Apache Airflow, and Apache Spark.

## Objective
To build a scalable and real-time data processing pipeline that ingests customer orders from Kafka, processes the data with Spark, and orchestrates workflows using Airflow.

## Technologies Used
- Apache Kafka
- Apache Airflow
- Apache Spark
- Python
- PostgreSQL (for metadata storage)
- Docker (for containerization)

## Folder Structure
- `streaming/` – Kafka producer and consumer scripts
- `dags/` – Airflow DAGs for orchestration
- `data/` – Sample order data in JSON format

## How to Run
1. Start Kafka and Airflow using Docker Compose.
2. Use the Kafka producer to send JSON order data.
3. Airflow triggers Spark jobs for transformation.

---

## Real-World Relevance

This project reflects my professional experience at Infosys, where I built and maintained real-time data pipelines for a retail/e-commerce client. It simulates the ingestion, processing, and orchestration of streaming customer order data using tools such as Apache Kafka, Apache Airflow, and Apache Spark. The repository demonstrates a simplified version of the production architecture I worked on, adapted with open-source tools and mock data to showcase the end-to-end pipeline functionality while maintaining data privacy.
