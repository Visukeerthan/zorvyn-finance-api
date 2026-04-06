# Finance API & RBAC System

A robust backend implementation for financial data processing with Role-Based Access Control.

## Key Features
* **Role-Based Access Control (RBAC):** Custom permission classes to restrict access based on User Roles (Admin, Analyst, Viewer).
* **Data Aggregation:** Dedicated dashboard endpoint for real-time financial summaries.
* **RESTful Architecture:** Clean API design using Django REST Framework.

## Project Structure
* `/api/login/`: Token-based authentication.
* `/api/dashboard/`: Financial summary logic.
* `/api/entries/`: CRUD operations for financial records.

## Quick Start
1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py runserver`

## Development Process & Methodology
This project was developed with a focus on **clean architecture and efficient data processing**. 

To ensure the implementation followed industry best practices for security and performance:
* **AI-Assisted Architecture:** I utilized AI tools as a "pair programmer" to refine the **Role-Based Access Control (RBAC)** logic and to ensure the **Data Aggregation** algorithms were optimized for financial reporting.
* **Modern Workflow:** Leveraging AI assistance allowed for rapid prototyping of the API structure while maintaining a high standard for code quality and professional documentation.