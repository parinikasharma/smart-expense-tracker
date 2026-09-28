# Smart Expense Tracker & Budget Analyzer

## Overview

Smart Expense Tracker & Budget Analyzer is a Python-based expense management application designed to help users record, organize, analyze, and monitor their daily expenses.

The application provides features such as expense management, category-wise analysis, monthly budget tracking, report generation, and CSV export.

## Problem Statement

Managing daily expenses manually can be difficult and time-consuming. Users may lose track of their spending, exceed their monthly budget, or find it difficult to understand where their money is being spent.

This project provides a simple digital solution for recording expenses and analyzing spending patterns.

## Objectives

- Record daily expenses efficiently.
- Store expense information permanently.
- Categorize expenses.
- Set and monitor a monthly budget.
- Calculate total and average spending.
- Identify the highest expense.
- Analyze category-wise spending.
- Generate expense reports.
- Export expense data to CSV format.
- Validate user inputs and handle errors.

## Features

### 1. Expense Management
- Add new expenses.
- View all recorded expenses.
- Delete expenses.
- Search expenses by category.

### 2. Budget Management
- Set a monthly budget.
- Calculate remaining budget.
- Detect when the budget has been exceeded.

### 3. Expense Analytics
- Calculate total spending.
- Calculate average expense.
- Find the highest expense.
- Display category-wise spending.

### 4. Reporting
- Generate an expense report.
- Export expense records to CSV format.

### 5. Data Storage
- Store expenses using JSON.
- Store the monthly budget using JSON.
- Automatically create the data directory when required.

### 6. Input Validation
- Validate expense amounts.
- Validate categories.
- Validate descriptions.
- Validate dates.

## Technologies Used

- Python 3
- JSON
- CSV
- Object-Oriented Programming
- File Handling
- Exception Handling
- Python Standard Library

## Project Structure

```text
smartexpensetracker/
│
├── main.py
├── expense.py
├── expense_manager.py
├── budget.py
├── analytics.py
├── reports.py
├── storage.py
├── validator.py
│
├── data/
│   ├── expenses.json
│   └── budget.json
│
└── tests/
