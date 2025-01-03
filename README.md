# Stock Screener
A simple web application to display stock tickers based on selected categories. Users can choose a category from a dropdown menu, and the app dynamically displays relevant stock tickers.

## Features
Dropdown Menu: Easily select a category (Consolidation, Breakout, Moving Average Consolidation).
Dynamic Ticker Display: Stock tickers are displayed based on the selected category.
Responsive Design: Built with Bootstrap for mobile and desktop compatibility.

## Setup
### Prerequisites
Python (for backend server, if using Flask/Django)

## Installation
### Clone Repository:
git clone <repository_url>
cd stock-screener

### Install dependancies:
pip install -r requirements.txt

### Run server:
python app.py

### Navigate to browser link:
http://localhost:5000

## Use:
Select a category from the dropdown menu.
The app will navigate to the selected category and display relevant stock tickers.

Update the data for most recent date by running http://localhost:5000/snapshot
