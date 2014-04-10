from dataset import datasets

datasetObj=datasets()

#str1=datasetObj.upload("dataset1")
#jsondata=datasetObj.get_datasets("dataset1")
jsondata=datasetObj.get_columns("dataset1")
print (jsondata)