import os
import pandas as pd
import uel_load_data
from uel_load_data import LoadData

import uel_parser_query
from uel_parser_query import SQLParser

current_path = os.getcwd()
qry_source_file = current_path + '\data\imdb\querys.csv'

qryData = LoadData(qry_source_file)
qryDataFrame = qryData.getDF();
qryDataFrame['complexity'] = 0;

for index, itQryDF in qryDataFrame.iterrows():
    sqlParse = SQLParser(itQryDF['query_out'])
    sqlParse.parser()
    qryTables = sqlParse.getTables()
    qryOutVars = sqlParse.getOutPutVars()
    qryQtJoins = sqlParse.getJoinsQty()

    qryComplex = sqlParse.calcComplexity(len(qryTables), len(qryOutVars), qryQtJoins)
    qryDataFrame.at[index, 'complexity'] = qryComplex

qryDataFrameSorted = qryDataFrame.sort_values(by='complexity')

#print(qryDataFrameSorted.describe())
#print(qryDataFrameSorted)

for index, itQryDF in qryDataFrameSorted.iterrows():
    print(itQryDF['query_out'], "|", itQryDF['complexity'])

print(qryDataFrameSorted.describe())