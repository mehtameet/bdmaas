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
        bashCommand="$MAHOUT_HOME/bin/mahout trainlogistic  --input ~/code/bdmaas/data/"+dataset_name+"/data/train/"+dataset_files[0]+"  --output ~/code/bdmaas/data/"+dataset_name+"/model  --target "+target+"   --categories "+str(count)+"  --predictors "+str_predictor+"   --types word  --features 20   --passes 100 --rate 50"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is "+output)
        print (error)
        return "trainlogistic done"
    
    def runlogistic(self,dataset_name):
        datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilenametest(dataset_name)
        bashCommand="$MAHOUT_HOME/bin/mahout runlogistic  --input ~/code/bdmaas/data/"+dataset_name+"/data/test/"+dataset_files[0]+"  --model ~/code/bdmaas/data/"+dataset_name+"/model --auc --confusion"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is "+output)
        print (error)
        return output
    
    def trainrandomforest(self,dataset_name):
        
        datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        bashCommand="$HADOOP_PREFIX/bin/hadoop jar SMAHOUT_HOME/core/target/mahout-core-1.0-SNAPSHOT-job.jar org.apache.mahout.classifier.df.tools.Describe -p /data/"+dataset_name+"/data/train/"+dataset_files[0]+" -f /data/"+dataset_name+"/data/KDDTrain+.info -d N 3 C 2 N C 4 N C 8 N 2 C 19 N L"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is" +output)
        print (error)
        return "randomforestTrainDataset done"
    
    def testrandomforest(self,dataset_name):
        
        datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        bashCommand="$HADOOP_PREFIX/bin/hadoop jar SMAHOUT_HOME/examples/target/mahout-examples-1.0-SNAPSHOT-job.jar org.apache.mahout.classifier.df.mapreduce.BuildForest -Dmapred.max.split.size=1874231 -d /data/"+dataset_name+"/data/test/"+dataset_files[0]+" -ds /data/"+dataset_name+"/data/KDDTrain+.info -sl 5 -p -t 100 -o nsl-forest12"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is" +output)
        print (error)
        return "randomforestTestDataset done"
    
    def runrandomforest(self,dataset_name):
        
        datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        bashCommand="$$HADOOP_PREFIX/bin/hadoop jar $MAHOUT_HOME/examples/target/mahout-examples-1.0-SNAPSHOT-job.jar org.apache.mahout.classifier.df.mapreduce.TestForest -i /data/"+dataset_name+"/data/test/"+dataset_files[0]+" -s /data/"+dataset_name+"/data/KDDTrain+.info -m nsl-forest12 -a -mr -o predictions12"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is" +output)
        print (error)
        return output
    
    