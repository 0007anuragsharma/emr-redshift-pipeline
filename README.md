1. An AWS EMR cluster is created to run Apache Spark jobs.

2. The EMR master node is connected from Visual Studio Code using SSH.

3. GitHub Archive dataset (compressed JSON files) is downloaded directly inside the EMR cluster using wget.

4. The downloaded raw JSON files are uploaded from EMR to an Amazon S3 bucket for cloud storage.

5. Apache Spark running on EMR reads the raw JSON data from S3.

6. Spark converts the raw JSON data into optimized Parquet format and stores it in an S3 temp folder.

7. Spark reads the Parquet data from the S3 temp folder.

8. Required fields are selected and transformed.

9. The transformed data is written into Amazon Redshift using JDBC.

10. Data is validated in Redshift using SQL queries.
