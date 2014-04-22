from dataset import datasets

datasetObj=datasets()

#str1=datasetObj.upload("dataset1")
#jsondata=datasetObj.get_datasets("dataset1")
# jsondata=datasetObj.get_datasets()
#jsondata=datasetObj.get_columns("dataset7")
# print (type(jsondata))
# innerhtml=""
# for i in jsondata:
#     innerhtml+=i
#     
# print innerhtml
#print jsondata

from algorithms import algorithms
algorithmObj=algorithms()
# 
# algorithmObj.trainlogistic("contract1", ["seller_company_name","customer_company_name"], "point_of_delivery_specific_location")
# algorithmObj.runlogistic("contract1")

from fileFormatting import fileformatting
fileformattingObj=fileformatting()
# fileformattingObj.format("contract6","train")
# fileformattingObj.format("contract6","test")
# fileformattingObj.fetchColumnNumber("contract7", "customer_duns_number")
# 
# print fileformattingObj.randomForestLabelString("contract7", "customer_company_name", "customer_duns_number")

algorithmObj.trainrandomforest("contract7", "customer_company_name", "customer_duns_number")
algorithmObj.testrandomforest("contract7")
algorithmObj.runrandomforest("contract7")