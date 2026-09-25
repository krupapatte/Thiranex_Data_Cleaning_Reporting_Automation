# Data Cleaning \& Reporting Automation

## Student Project

**Course Task:** Data Cleaning \& Reporting Automation  
**Year:** 3rd Year  
**Tools Used:** Python, Pandas, Matplotlib, CSV and Excel

## 1\. Introduction

This project is created as part of my 3rd year coursework. The main purpose of the project is to clean a small dataset and generate a simple report automatically using Python.

The project focuses on common data cleaning tasks such as handling missing values, removing duplicate records, correcting inconsistent data, and preparing the data for reporting.

## 2\. Objectives

The main objectives of this project are:

* To understand basic data preprocessing.
* To identify and handle missing values.
* To remove duplicate records.
* To correct inconsistent text data.
* To generate useful summary information from the cleaned data.
* To create a simple chart for better understanding of the results.

## 3\. Technologies Used

* **Python** – main programming language
* **Pandas** – used for reading, cleaning and processing the data
* **Matplotlib** – used to create the sales chart
* **CSV** – used for storing the input and output data
* **Excel** – used for viewing the generated report and cleaned data

## 4\. Project Structure

```text
Thiranex\_Data\_Cleaning\_Reporting\_Automation/
│
├── data/
│   └── raw\_data.csv
│
├── output/
│   ├── cleaned\_data.csv
│   ├── city\_summary.csv
│   ├── report\_summary.csv
│   ├── report.txt
│   ├── cleaning\_report.xlsx
│   └── charts/
│       └── sales\_by\_city.png
│
├── screenshots/
│   └── task\_screenshot.png
│
├── run.py
├── requirements.txt
└── README.md
```

## 5\. Data Cleaning Process

The following steps are performed by the Python program:

1. Read the raw CSV file.
2. Remove unnecessary spaces from text values.
3. Standardize city names.
4. Convert email addresses to lowercase.
5. Convert the order date column into the correct date format.
6. Convert sales values into numeric values.
7. Handle missing sales values using the median.
8. Replace blank email values with a standard placeholder.
9. Remove duplicate customer records.
10. Create a simple sales category as Low, Medium or High.
11. Generate summary tables.
12. Create a chart showing total sales by city.

## 6\. How to Run the Project

### Step 1: Install Python

Install Python 3.10 or a newer version on the computer.

### Step 2: Open the Project

Open the project folder using VS Code or another Python editor.

### Step 3: Install Required Libraries

Open the terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Program

Run the following command:

```bash
python run.py
```

### Step 5: Check the Output

After running the program, open the `output` folder.

The folder contains:

* cleaned data
* city-wise sales summary
* report summary
* text report
* Excel report
* sales chart

## 7\. Expected Result

The program takes the raw dataset and performs basic cleaning automatically. It then produces a cleaned dataset along with summary reports and a chart.

This helps reduce repetitive manual work when preparing data for reporting.

## 8\. Tutorial Reference

The following tutorial was referred to while working on this task:

https://youtu.be/jxq4-KSB\_OA?si=TYTTnUR3vC7TyIib

## 9\. Conclusion

This project helped me understand the basic steps involved in data cleaning and automated reporting using Python. It also gave me practical experience with Pandas, data preprocessing, CSV files and simple data visualization.

The project can be extended in the future by using larger datasets and creating more reports or dashboards.

