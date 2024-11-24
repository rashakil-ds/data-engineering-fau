# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation Between Education Spending and GDP Growth in North America

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How does government expenditure on education as a percentage of GDP correlate with GDP growth in North American countries from 2016 to 2023?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The project will investigate the potential relationship between public investment in education and economic growth, providing insights into how education funding impacts economic performance.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Worldbank (Government expenditure on education, total (% of GDP))
* Metadata URL: https://data.worldbank.org/indicator/SE.XPD.TOTL.GD.ZS
* Data URL: https://api.worldbank.org/v2/en/indicator/SE.XPD.TOTL.GD.ZS?downloadformat=csv
* Data Type: Zip->CSV

This dataset contains data on government expenditure on education as a percentage of GDP, covering countries worldwide. For this project, only data from North American countries for the years 2016–2023 were extracted

### Datasource2: Worldbank (GDP growth (annual %))
* Metadata URL: https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG
* Data URL: https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=csv
* Data Type: Zip->CSV

This dataset contains GDP growth rates for countries worldwide. We focused on North American countries for the years 2016–2023.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Dataset selection
2. Building an automated data pipeline
3. Exploratory Data Analysis (EDA) and Feature Engineering
4. Statistical Modeling and Hyperparameter Tuning
5. Model Evaluation: performance, interpretation, and insights
6. Reporting on findings
