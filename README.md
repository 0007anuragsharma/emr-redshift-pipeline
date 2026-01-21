# AWS-WORKFLOW-BDP:
This project demonstrates a production-grade data pipeline that ingests semi-structured GitHub Archive data, processes it at scale using Apache Spark on AWS EMR, and loads the refined data into Amazon Redshift for analytical querying and BI.

# Architecture Flow
Local System → Amazon S3 → AWS EMR (Spark) → Temporary S3 Location → Amazon Redshift

# 🏗️ Architecture :
Ingestion: GitHub Archive (JSON) files are stored in Amazon S3 (Data Lake).

Processing: AWS EMR (Spark Cluster) reads the raw data, performs transformations, and filters events.

Intermediate Storage: Transformed data is staged in a temporary S3 bucket (required for Redshift COPY command).

Data Warehousing: The final structured data is loaded into Amazon Redshift for high-performance SQL analytics.

# 🛠️ Tech Stack
Cloud: AWS (S3, EMR, Redshift, IAM)

Processing: PySpark (Apache Spark)

IDE: VS Code (Remote SSH connection to EMR Master Node)

Format: JSON (Raw), Parquet/JDBC (Processed)

# 🚀 Step-by-Step Implementation
# 1. Infrastructure Setup
AWS EMR: Launched a cluster with m5.xlarge instances. Configured Security Groups to allow inbound SSH (Port 22) and Redshift (Port 5439).

Redshift: Set up a cluster and created the target schema.

IAM Roles: Configured roles to allow EMR to read/write to S3 and allow Redshift to access S3 for the COPY operation
<img width="1920" height="934" alt="emr" src="https://github.com/user-attachments/assets/9e1a83fe-a76a-4b70-95c0-427c7054c7ec" />

# 2. Development Workflow :
To ensure a seamless development experience, I connected VS Code directly to the EMR Master Node via the Remote - SSH extension. This allowed for:

Real-time script editing on the cluster.

Direct execution of spark-submit jobs.
<img width="1920" height="1008" alt="vscode" src="https://github.com/user-attachments/assets/dffb573f-90ef-43a1-9181-b40114e5e915" />

# 3. Data Transformation (PySpark)
The core logic performs the following:

Filtering: Focused on PushEvent types to analyze developer activity.

Flattening: Extracted nested JSON fields (e.g., actor.login, repo.name).

Optimization: Utilized a temporary S3 directory for the Redshift Spark Connector to ensure efficient data transfer.
<img width="1920" height="1008" alt="download" src="https://github.com/user-attachments/assets/e76ab6d6-3ab7-4dc1-9daf-69c467b3155d" />
<img width="1920" height="946" alt="s3_raw" src="https://github.com/user-attachments/assets/647876cd-3c8a-46a9-9d4b-b2697f3ee6cf" />


# 4 : Write Transformed Data to Temp S3
Stored the transformed data in a temporary S3 location in Parquet format for optimized loading.
<img width="1920" height="934" alt="s3_temp" src="https://github.com/user-attachments/assets/66c6952e-8363-4f6a-b3fe-c647f75991e9" />

# 5 : Redshift Table Creation and Data Validation
Created target tables in Amazon Redshift Query Editor based on the transformed schema and Validate the loaded data by running analytical queries in Amazon Redshift.
<img width="1920" height="942" alt="redshift" src="https://github.com/user-attachments/assets/ac7c18ec-c386-4bff-bfdf-30c71b566f11" />

