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

algorithmObj.trainlogistic("contract1", ["seller_company_name","customer_company_name"], "point_of_delivery_specific_location")