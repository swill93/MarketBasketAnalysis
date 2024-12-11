# MarketBasketAnalysis

## Overview
This project implements Market Basket Analysis using Apache Spark's FPGrowth Algorithm to discover frequent itemsets and association rules from a retail transaction dataset. The goal is to identify items that frequently co-occur in transactions, helping businesses improve sales strategies and product recommendations.

## Technologies Used
Programming Language: Python
Library:
PySpark: For distributed data processing and implementing the FPGrowth algorithm to discover frequent itemsets and generate association rules.
Visualization Tool:
Tableau: Used to create interactive dashboards for visualizing frequent itemsets, association rules, and relationships between products.
Environment:
PySpark (for distributed computing)

## Dataset
The dataset used in this project contains retail transaction data, where each transaction consists of a set of items purchased. The dataset can be in a CSV or another compatible format.

Example dataset: transactions.csv
BillNo: Unique identifier for each transaction.
Itemname: Item(s) purchased in the transaction.

## Steps Taken
Data Preprocessing:

Cleaned and transformed the dataset to prepare it for the FPGrowth algorithm, including encoding the transactions into a suitable format for processing in PySpark.

### Frequent Itemset Generation:
Used FPGrowth (Frequent Pattern Growth) from PySpark to generate frequent itemsets based on a minimum support threshold. This algorithm efficiently handles large datasets and identifies itemsets that appear frequently together in transactions.

### Association Rule Mining:
Generated association rules from the frequent itemsets using metrics like confidence and lift to evaluate the strength of relationships between products.
Visualization:

Exported the frequent itemsets and association rules to CSV format.
Used Tableau to create interactive dashboards, visualizing the frequent itemsets and association rules, and providing a user-friendly interface for exploring the relationships between items.




