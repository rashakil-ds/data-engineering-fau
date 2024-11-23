# Project Plan

## Title
<!-- Give your project a short title. -->
Socio-Economic and Law Enforcement Impact on Crime Rates: A Cross-Community Analysis

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do socio-economic conditions and law enforcement metrics impact violent and property crime rates in U.S. communities?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The study analyzes the relationships between socioeconomic conditions (e.g., income levels, population demographics, unemployment) and community crime rates (violent and property crimes) across U.S. communities. By comparing normalized and unnormalized datasets, the study seeks to assess how preprocessing impacts the interpretation of these relationships, focusing on uncovering key factors associated with crime prevalence.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Communities and Crime
* Metadata URL: https://archive.ics.uci.edu/dataset/183/communities+and+crime
* Data URL: https://archive.ics.uci.edu/dataset/183/communities+and+crime.zip
* Data Type: Zip->CSV

The Communities and Crime dataset combines socio-economic, demographic, and crime data from U.S. communities, integrating variables from the 1990 Census, FBI crime reports, and law enforcement surveys. It contains 1,994 instances with 127 attributes, offering insights into factors influencing violent and property crime rates.

### Datasource2: Communities and Crime Unnormalized
* Metadata URL: https://archive.ics.uci.edu/dataset/211/communities+and+crime+unnormalized
* Data URL: https://archive.ics.uci.edu/dataset/211/communities+and+crime+unnormalized.zip
* Data Type: Zip->CSV

The Communities and Crime Unnormalized dataset provides raw, unprocessed socio-economic, demographic, and crime data for U.S. communities, sourced from the 1990 Census and FBI crime reports. It contains 2,215 instances with 125 attributes, allowing analysis without the effects of normalization or preprocessing.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Dataset selection
2. Building an automated data pipeline
3. Exploratory Data Analysis (EDA) and Feature Engineering
4. Statistical Modeling and Hyperparameter Tuning
5. Model Evaluation: performance, interpretation, and insights
6. Reporting on findings
