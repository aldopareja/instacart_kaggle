# instacart_kaggle

In this repo we will predict products to be bought by a customer in a future purchase session.

## Python Version

miniconda3 python distribution was used as the base distribution for this project: this is the output of python -V:

Python 3.6.1 :: Continuum Analytics, Inc.

The packages used are found in dependencies.txt

## directory structure

Data: it contains *raw*, *interim*, *processed* and *external* directories. Raw is an empty folder where we should put the data from the competition (not added to the repo). Interim is a folder where we store intermediate states of preprocessed data. External will contain all external data that will be used. Processed will contain final databases that will be used for training. 

The raw directory should contain the following files:
* aisles.csv.zip
* order_products__prior.csv.zip  
* orders.csv.zip    
* sample_submission.csv.zip
* departments.csv.zip  
* order_products__train.csv.zip  
* products.csv.zip
