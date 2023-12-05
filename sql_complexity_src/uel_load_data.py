import csv
import os
import pandas as pd

class LoadData():
    def __init__(self, file):
        self.working_path = os.getcwd()
        self.source_file = file
        self.oCSV_file = None
        self.oDF_file = None

    def getDF(self):
        if self.oDF_file is None:
            self.ReadFile2DF()
        return self.oDF_file

    def ReadFile(self):
        # opening the CSV file
        with open(self.source_file, mode ='r') as ofile:
            # reading the CSV file
            self.oCSV_file = csv.reader(ofile)
        return self.oCSV_file
    
    def ReadFile2DF(self):
        self.oDF_file = pd.read_csv(self.source_file, header=0)
        return self.oDF_file
    
    def PrintFile(self):
        for lines in self.oCSV_file:
            print(self.oCSV_file)

    def PrintDF(self):
        print(self.oDF_file)

if __name__ == '__main__':
    cwd = os.getcwd()
    file = cwd + '\data\qry_nodup_source.csv'

    oData = LoadData(file)
    oData.ReadFile2DF()
    oData.PrintDF()
    print(oData.getDF().columns)

    for index, it in oData.getDF().iterrows():
        print(it['query_out'])