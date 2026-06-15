# Ecommerce Analytics Engineering Project using Databricks & dbt

## Project Overview

This project demonstrates an end-to-end Analytics Engineering solution built using Databricks and dbt.

The goal is to transform raw ecommerce data into business-ready analytical datasets following modern data warehousing and analytics engineering best practices.

The project implements a Medallion Architecture (Bronze, Silver, Gold), Star Schema modeling, Incremental Processing, Data Quality Testing, Documentation, Snapshots (SCD Type 2), and Git-based development workflows.

---

## Tech Stack

### Data Platform

* Databricks
* Delta Lake
* Spark SQL

### Transformation Layer

* dbt Core
* dbt-databricks Adapter

### Version Control

* Git
* GitHub

### Data Modeling

* Star Schema
* Fact and Dimension Modeling

### Analytics Engineering Features

* Incremental Models
* Snapshots (SCD Type 2)
* Data Quality Tests
* Documentation
* Lineage Tracking
* Reusable Macros

---

## Architecture

Bronze Layer
↓
Silver Layer
↓
Staging Models
↓
Intermediate Models
↓
Gold Layer
↓
Business KPIs
↓
Power BI / Reporting

---

## Project Structure

```text
ecommerce_dbt/

├── models/

│   ├── staging/
│   │   ├── stg_customers.sql
│   │   ├── stg_orders.sql
│   │   ├── stg_products.sql
│   │   └── stg_returns.sql

│   ├── intermediate/
│   │   ├── int_orders_details.sql
│   │   ├── int_customer_orders.sql
│   │   └── int_returns_summary.sql

│   ├── marts/

│   │   ├── dimensions/
│   │   │   ├── dim_customer.sql
│   │   │   ├── dim_product.sql
│   │   │   └── dim_customer_history.sql

│   │   ├── facts/
│   │   │   └── fact_sales.sql

│   │   └── metrics/
│   │       ├── customer_revenue.sql
│   │       └── product_performance.sql

├── snapshots/
│   └── customer_snapshot.sql

├── macros/
│   └── customer_tier.sql

├── tests/

├── packages.yml

├── dbt_project.yml

└── README.md
```

---

## Data Flow

### Source Layer (Silver)

The project assumes cleaned operational data is available in Silver tables:

* silver.customers
* silver.orders
* silver.products
* silver.returns

---

### Staging Layer

Purpose:

* Standardize column names
* Apply light cleansing
* Remove source system complexity

Models:

* stg_customers
* stg_orders
* stg_products
* stg_returns

---

### Intermediate Layer

Purpose:

* Centralize reusable business logic
* Reduce duplicate SQL
* Simplify Gold models

Models:

#### int_orders_details

Combines:

* Orders
* Customers
* Products

into a single reusable dataset.

#### int_customer_orders

Provides:

* Total Orders
* Total Sales
* Average Order Value

per customer.

#### int_returns_summary

Aggregates return metrics by order.

---

### Gold Layer

The Gold Layer contains business-ready models.

#### Dimensions

##### dim_customer

Customer attributes with surrogate keys.

##### dim_product

Product attributes with surrogate keys.

##### dim_customer_history

Historical customer changes generated from dbt snapshots.

---

#### Fact Table

##### fact_sales

Contains:

* Revenue
* Quantity
* Product Information
* Customer Information
* Return Amounts
* Net Sales

One row represents one business transaction.

---

#### KPI Models

##### customer_revenue

Provides:

* Customer Revenue
* Total Orders
* Average Order Value

##### product_performance

Provides:

* Product Revenue
* Return Metrics
* Sales Performance

---

## Incremental Processing

The fact_sales model uses incremental materialization.

Benefits:

* Faster execution
* Reduced compute costs
* Scalable for large datasets

Configuration:

```sql
{{ config(
    materialized='incremental',
    unique_key='order_id',
    incremental_strategy='merge'
) }}
```

Only recent data is reprocessed during each run.

---

## Slowly Changing Dimensions (SCD Type 2)

Customer history is tracked using dbt snapshots.

Snapshot Strategy:

* check

Tracked Columns:

* city
* state

This allows historical analysis of customer attribute changes over time.

Example:

Customer 101

Delhi → Mumbai

Snapshot captures both versions while preserving historical records.

---

## Data Quality Tests

Implemented tests:

### Generic Tests

* unique
* not_null
* relationships

Examples:

* customer_id must not be null
* product_id must not be null
* surrogate keys must be unique
* fact table relationships must be valid

---

## Documentation

dbt documentation generated using:

```bash
dbt docs generate
dbt docs serve
```

Features:

* Column Documentation
* Model Documentation
* Data Lineage Visualization

---

## Reusable Macro

### customer_tier

Categorizes customers into:

* Platinum
* Gold
* Silver
* Bronze

based on total sales.

Benefits:

* Reusable logic
* Reduced SQL duplication
* Easier maintenance

---

## Git Workflow

Feature branch workflow used:

```text
main
 │
 ├── feature/staging-layer
 ├── feature/intermediate-layer
 ├── feature/gold-layer
 └── feature/incremental-snapshots
```

Development Process:

1. Create Feature Branch
2. Develop Model
3. Run Tests
4. Create Pull Request
5. Review Changes
6. Merge to Main

---

## Running the Project

### Install Dependencies

```bash
dbt deps
```

### Build Models

```bash
dbt build
```

### Run Specific Model

```bash
dbt run --select fact_sales
```

### Full Refresh

```bash
dbt run --select fact_sales --full-refresh
```

### Execute Snapshots

```bash
dbt snapshot
```

### Generate Documentation

```bash
dbt docs generate
dbt docs serve
```

---

## Key Concepts Demonstrated

* Analytics Engineering
* Data Modeling
* Star Schema Design
* Incremental Loading
* SCD Type 2
* Snapshot Management
* Data Quality Testing
* Reusable Macros
* Documentation Generation
* Data Lineage
* Git-Based Development
* Databricks Integration
* Delta Lake Merge Operations

---

## Future Enhancements

* CI/CD using GitHub Actions
* Azure DevOps Integration
* Production Deployment Pipelines
* Custom Generic Tests
* dbt Exposures
* dbt Semantic Layer
* Monitoring & Observability
* Data Contracts
* Advanced Macro Frameworks

---

## Author

Lakshit Tyagi

Analytics Engineering Project using Databricks, Delta Lake, Spark SQL, dbt, and Git.
