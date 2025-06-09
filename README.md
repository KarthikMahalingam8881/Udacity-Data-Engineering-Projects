# 🎯 Redshift Data Warehouse: Log & Song Analysis Pipeline

## 🚀 Overview

This project builds a scalable AWS Redshift-based data warehouse to analyze user activity logs and song metadata stored in S3. The goal is to enable analytical queries like “What songs were most played?” by designing a robust star schema and automating the full ETL pipeline in Python and SQL.

---

## 🛠️ Tools & Technologies

- **AWS Redshift** (Provisioned Cluster)
- **AWS S3** (Public Dataset: `udacity-dend`)
- **Python** (ETL scripts)
- **SQL** (Schema, COPY, and INSERT queries)
- **psycopg2** (PostgreSQL connector)
- **IAM Roles** (Redshift ↔ S3 access)

---

## 🧱 Data Warehouse Architecture

    [S3 Logs & Songs]
            |
    [Staging Tables]
            |
   ┌────────┴────────┐
   
   [Fact Table: songplays]
  
  ┌────┬────┬────┬────┐

[users] [songs] [artists] [time]


- **Staging Tables**: Raw JSON logs and song metadata
- **Fact Table**: `songplays` — one row per song play
- **Dimension Tables**: `users`, `songs`, `artists`, `time`

  ---

## ⚙️ ETL Pipeline Steps

1. **Configure IAM Role**  
   - Create `dwhRole` in IAM with `AmazonS3ReadOnlyAccess`
   - Copy the ARN to `dwh.cfg` file (not committed for security)

2. **Redshift Setup**
   - Created a **provisioned cluster** (not serverless due to `psycopg2` connection format)
   - Manually updated EC2 security group rules to allow inbound Redshift access from local IP
   - Enabled Redshift Query Editor v2 with required permissions

3. **ETL Code Flow**
   - `create_tables.py`: Drops & creates staging and final schema tables
   - `etl.py`: Loads data from S3 → staging → final tables
   - `sql_queries.py`: Stores all COPY and INSERT SQL queries
   - Verified schema and queries using Redshift Query Editor

---

## 🧪 Sample Analytical Queries

-- Top 5 most played songs

SELECT songs.title, COUNT(*) AS play_count

FROM songplays

JOIN songs ON songplays.song_id = songs.song_id

GROUP BY songs.title

ORDER BY play_count DESC

LIMIT 5;

-- Active users by location

SELECT users.location, COUNT(*) AS user_count

FROM users

GROUP BY users.location

ORDER BY user_count DESC;

# 💡 Lessons Learned
* How to manually configure AWS IAM roles and security groups

* Why Redshift provisioned clusters are required when using PostgreSQL-style connectors

* How DISTKEY and SORTKEY improve Redshift performance

* JSONPath and S3 URI best practices for Redshift COPY commands

* Transitioning between environments (Colab → VS Code) when port access is blocked

# 📁 Folder Structure

Data_Warehouse/

│

├── create_tables.py       # Create/drop tables

├── etl.py                 # Run full ETL

├── sql_queries.py         # All SQL queries

├── dwh.cfg                # Config file (excluded via .gitignore)

└── README.md              # This file

# 🔐 Note
Make sure your dwh.cfg file is excluded from Git using .gitignore:
# .gitignore
dwh.cfg

# ✍️ Author:
Karthik Mahalingam
Open-source Contributor | Data Engineer
GitHub: @KarthikMahalingam8881



