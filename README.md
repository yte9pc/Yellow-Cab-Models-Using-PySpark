# Yellow Cab Models Using PySpark
ML model for 2019 Yellow Cab payment type and tip amount using PySpark

# Code
- pullData.py -  Python script to retrieve trip record for 2019, look up table, and data dictionary
- explorationSummary.ipynb - Notebook of exploration of data, includes summary, graphs, and charts
- tipAmount.ipynb - Notebook contains importing, cleaning, and preprocessing data. Also, contains models (LR and Gradient-boosted) for predicting tip amount
- paidClassifier.ipynb - Notebook contains logistic models for predicting if trip was paid for

# Data
- Data can be found and downloaded from
  - https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Data definition 
  - https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
- Taxi Zone Lookup Table
  - https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
