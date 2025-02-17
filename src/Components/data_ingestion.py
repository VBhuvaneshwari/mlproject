import os
import sys
# from src.exception import CustomException
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass


@dataclass
class DataIngesionConfig():
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path : str = os.path.join('artifacts', 'data.csv')

class DataIngestion():
    def __init__(self):
        self.DataIngestionConfig = DataIngesionConfig()

    def initiate_data_ingestion(self):
        logging.info ('Entered the data ingestion component')
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("train test split initiated.")
            train_set, test_set = train_test_split(df, train_size=0.2, random_state=42)
            os.makedirs(os.path.dirname(self.DataIngestionConfig.train_data_path), exist_ok=True)
            train_set.to_csv(self.DataIngestionConfig.train_data_path, index= False, header = True)
            test_set.to_csv(self.DataIngestionConfig.test_data_path, index = False, header = True)
            df.to_csv(self.DataIngestionConfig.raw_data_path,index = False, header = True )
            logging.info('data ingestion completed.')
            return(
                self.DataIngestionConfig.train_data_path,
                self.DataIngestionConfig.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    DataIngestion.initiate_data_ingestion(obj)