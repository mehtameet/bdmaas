import subprocess
import requests
import json
from dataset import datasets

class algorithms:
    
    
    
    def trainlogistic(self,dataset_name,predictors,target):
        str_predictor=""
        count=0
        for i in predictors:
            count+=1
            str_predictor+=i+" "
        datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        bashCommand="$MAHOUT_HOME/bin/mahout trainlogistic  --input ~/code/bdmaas/data/"+dataset_name+"/data/"+dataset_files[0]+"  --output ~/code/bdmaas/data/"+dataset_name+"/model  --target "+target+"   --categories "+str(count)+"  --predictors "+str_predictor+"   --types word  --features 20   --passes 100 --rate 50"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is "+output)
        print (error)
        return "trainlogistic done"
    
    def runlogistic(self,dataset_name):
        datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        bashCommand="$MAHOUT_HOME/bin/mahout runlogistic  --input ~/code/bdmaas/data/"+dataset_name+"/data/"+dataset_files[0]+"  --model ~/code/bdmaas/data/"+dataset_name+"/model --auc --confusion"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is "+output)
        print (error)
        return "runlogistic done"