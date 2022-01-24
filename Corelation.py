import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    cups_of_coffe = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffe.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))

    return{"x":cups_of_coffe,"y":hours_of_sleep}        
def FindCoRelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation between cups of coffe and hours of sleep",corelation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    FindCoRelation(dataSource)

setup() 