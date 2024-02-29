# Expense Tracker

## Overview

This Expense Tracker is a simple tool designed to help individuals manage their personal finances by keeping track of expenses. Built with Python, it utilizes a SQLite database to store expense records, including date, description, category, and price.

## Features

### Create Expense Records
Add new expenses with details such as date, description, category, and amount.

### Database Management
Automatically creates and manages a SQLite database to store all expense records securely.

### User Interaction
Through a CLI, users can easily input and view their expenses.

## Installation

1. Clone this repository to your local machine.
```bash
git clone https://github.com/QiQiEva/expense-tracker/
```
2. Ensure you have Python installed on your system. I used the latest version Python 3.12

## Usage

To start tracking your expenses, follow these steps:
1. **Delete expenses.db from directory**
2. **Initialize the database:**
```bash
python create_db.py
```
This will create a `expenses.db` file in your project directory if it doesn't already exist.

3. **Run the main application:**
```bash
python main.py
```
