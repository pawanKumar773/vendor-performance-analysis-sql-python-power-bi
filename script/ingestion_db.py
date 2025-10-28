import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging config
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
engine=create_engine('sqlite:///inventory.db')
def load_raw_data():
   
   start=time.time()
   for file in os.listdir("inventory dataset"):
     if ('.csv') in file:
        df=pd.read_csv('inventory dataset/'+file)
        logging.info(f'Ingesting {file} in db')  
        ingest_db(df,file[:-4],engine)
   end= time.time()
   total_time = (end-start)/60
   logging.info('Ingestion Complete')
   logging.info(f'\nTotal time Taken :{total_time} minutes')
def ingest_db(df,table_name,engine):
    df.to_sql(table_name,con=engine,if_exists='replace',index=False)
if __name__ == '__main__':
    load_raw_data() 
"""folder = "delivery data"

for file in os.listdir(folder):
    if file.lower().endswith(".csv"):   # sirf csv files
        full_path = os.path.join(folder, file)  # safe path join
        df = pd.read_csv(full_path)
        print(file, "=>", df.shape)
        ingest_db(df,file[:-4],engine)"""