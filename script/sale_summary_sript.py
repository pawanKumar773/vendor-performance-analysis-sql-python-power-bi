import sqlite3
import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time
from ingestion_db import ingest_db

# Logging config
logging.basicConfig(
    filename="logs/sale_summary_script.log",
    level=logging.INFO,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_sale_summary(conn):
    ''' this function will merge different tables to get hte overall vendor sumary and adding new collumns in the resultant data '''
    sale_summary = pd.read_sql_query("""
WITH 
freight_summary AS (SELECT 
                               VendorNumber,
                               SUM(Quantity) AS total_quantity_invoice,
                               SUM(Dollars) AS total_dollar_invoice,
                               SUM(Freight) AS total_freight_cost
                               FROM vendor_invoice
                               GROUP BY VendorNumber),
purchase_summary AS (
    SELECT
        t1.VendorNumber,
        t1.VendorName,
        t1.Brand,
        t2.Description,
        t2.Volume,
        t2.Price AS actual_price,
        t2.PurchasePrice,	
        SUM(t1.Quantity) AS total_quantity_purchase,
        SUM(t1.Dollars) AS total_dollar_purchase
    FROM purchases t1
    JOIN purchase_price t2
        ON t1.VendorNumber = t2.VendorNumber 
        AND t1.Brand = t2.Brand
    WHERE t1.PurchasePrice > 0
    GROUP BY t1.VendorNumber, t1.Brand, t1.VendorName, t2.Volume, t2.Price, t2.PurchasePrice,t2.Description
),
sale_summary AS (
    SELECT 
        VendorNo,
        Brand,
        SUM(SalesQuantity) AS total_Quantity_sale,
        SUM(SalesDollars) AS total_sale_dollar,
        SUM(SalesPrice) AS total_sale_price,
        SUM(ExciseTax) AS total_excise_tax
    FROM sales
    GROUP BY VendorNo, Brand
)
SELECT
    p.VendorNumber,
    p.VendorName,
    p.Brand,
    p.Description,
    p.Volume,
    p.actual_price,
    p.PurchasePrice,
    p.total_quantity_purchase,
    p.total_dollar_purchase,
    s.total_Quantity_sale,
    s.total_sale_price,
    s.total_sale_dollar,
    s.total_excise_tax,
    f.total_quantity_invoice,
    f.total_dollar_invoice,
    f.total_freight_cost
FROM purchase_summary p
LEFT JOIN sale_summary s
    ON p.VendorNumber = s.VendorNo AND p.Brand = s.Brand
LEFT JOIN freight_summary f
    ON p.VendorNumber = f.VendorNumber;
""", conn)
    return sale_summary

def clean_data(df):
    ''' this function will clean the data'''
    #changing data type to float
    sale_summary['Volume']=sale_summary['Volume'].astype(float)
    # fill null value--> 0   beacouse  vendor purchase the product but not sale 
    sale_summary.fillna(0,inplace=True)
    # apply feasure enginnering 
    sale_summary['gross_profit']=sale_summary['total_sale_dollar']-sale_summary['total_dollar_purchase']
    sale_summary['margin']=sale_summary['gross_profit']/sale_summary['total_sale_dollar']
    sale_summary['turnOver']=sale_summary['total_quantity_purchase']/sale_summary['total_Quantity_sale']
    sale_summary['sale_to_purchase_ratio']=sale_summary['total_sale_dollar']/sale_summary['total_dollar_purchase']

    return df

if __name__=='__main__':
    #creating database connection
    conn=sqlite3.connect('inventory.db')

    logging.info('Creating Vendor Summary Table .....')
    summary_df=create_sale_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data ............')
    clean_df=clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data.....')
    ingest_db(clean_df,'sale_summary',conn)
    logging.info('Completed')