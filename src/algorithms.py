import subprocess
import requests
import json
from dataset import datasets
from fileFormatting import fileformatting
fileformattingObj=fileformatting()
datasetObj=datasets()

class algorithms:
    
    
    
    def trainlogistic(self,dataset_name,predictors,target):
        str_predictor=""
        count=0
        for i in predictors:
            count+=1
            str_predictor+=i+" "
        #datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        bashCommand="$MAHOUT_HOME/bin/mahout trainlogistic  --input ~/code/bdmaas/data/"+dataset_name+"/data/train/"+dataset_files[0]+"  --output ~/code/bdmaas/data/"+dataset_name+"/model  --target "+target+"   --categories 2  --predictors "+str_predictor+"   --types word  --features 20   --passes 100 --rate 50"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is "+output)
        print (error)
        return "trainlogistic done"
    
    def runlogistic(self,dataset_name):
        #datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilenametest(dataset_name)
        bashCommand="$MAHOUT_HOME/bin/mahout runlogistic  --input ~/code/bdmaas/data/"+dataset_name+"/data/test/"+dataset_files[0]+"  --model ~/code/bdmaas/data/"+dataset_name+"/model --auc --confusion"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is "+output)
        print (error)
        result=output.split("AUC")[1]
        return "AUC"+result
    
    def trainrandomforest(self,dataset_name,predictor,target):
        
        #Commented for initial testing
        #datasetObj=datasets()
        #dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        #bashCommand="$HADOOP_PREFIX/bin/hadoop jar SMAHOUT_HOME/core/target/mahout-core-1.0-SNAPSHOT-job.jar org.apache.mahout.classifier.df.tools.Describe -p /data/"+dataset_name+"/data/train/"+dataset_files[0]+" -f /data/"+dataset_name+"/data/KDDTrain+.info -d N 3 C 2 N C 4 N C 8 N 2 C 19 N L"
        #predictor=predictors.split(",")
        
        randomForestLabelString=fileformattingObj.randomForestLabelString(dataset_name, predictor, target)
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        
        bashCommand='curl -i -X DELETE "http://54.186.225.72:50070/webhdfs/v1/data/'+dataset_name+'/data/train/'+dataset_files[0]+'.info?op=DELETE&user.name=ubuntu"'
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is testrandomforest" +output)
        print (error)
        
        
        print "randomForestLabelString is : "+randomForestLabelString
        bashCommand="$HADOOP_PREFIX/bin/hadoop jar $MAHOUT_HOME/core/target/mahout-core-1.0-SNAPSHOT-job.jar org.apache.mahout.classifier.df.tools.Describe -p /data/"+dataset_name+"/data/train/"+dataset_files[0]+" -f /data/"+dataset_name+"/data/train/"+dataset_files[0]+".info -d "+randomForestLabelString
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is of trainrandomforest" +output)
        print (error)
        return "randomforestTrainDataset done"
    
    def testrandomforest(self,dataset_name):
        
        datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        dataset_filestest=datasetObj.get_datasetsFirstFilenametest(dataset_name)
        #to do remove nsl-forest & predictor
        #bashCommand="$HADOOP_PREFIX/bin/hadoop fs -rmr /user/ubuntu/nsl-forest"
        bashCommand='curl -i -X DELETE "http://54.186.225.72:50070/webhdfs/v1/user/ubuntu/nsl-forest?op=DELETE&user.name=ubuntu&recursive=true"'
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is testrandomforest" +output)
        print (error)

        #bashCommand="$HADOOP_PREFIX/bin/hadoop fs -rmr /user/ubuntu/predictions"
        bashCommand='curl -i -X DELETE "http://54.186.225.72:50070/webhdfs/v1/user/ubuntu/predictions?op=DELETE&user.name=ubuntu&recursive=true"'
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is testrandomforest" +output)
        print (error)

        
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        bashCommand="$HADOOP_PREFIX/bin/hadoop jar $MAHOUT_HOME/examples/target/mahout-examples-1.0-SNAPSHOT-job.jar org.apache.mahout.classifier.df.mapreduce.BuildForest -Dmapred.max.split.size=1874231 -d /data/"+dataset_name+"/data/test/"+dataset_filestest[0]+" -ds /data/"+dataset_name+"/data/train/"+dataset_files[0]+".info -sl 5 -p -t 100 -o nsl-forest"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is testrandomforest" +output)
        print (error)
        return "randomforestTestDataset done"
    
    def runrandomforest(self,dataset_name):
        
        datasetObj=datasets()
        dataset_files=datasetObj.get_datasetsFirstFilename(dataset_name)
        dataset_filestest=datasetObj.get_datasetsFirstFilenametest(dataset_name)
        bashCommand="$HADOOP_PREFIX/bin/hadoop jar $MAHOUT_HOME/examples/target/mahout-examples-1.0-SNAPSHOT-job.jar org.apache.mahout.classifier.df.mapreduce.TestForest -i /data/"+dataset_name+"/data/test/"+dataset_filestest[0]+" -ds /data/"+dataset_name+"/data/train/"+dataset_files[0]+".info -m nsl-forest -a -mr -o predictions"
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is runrandomforest" +output)
        print (error)
        result=output
        print "result is "+result
        return result
    
    
