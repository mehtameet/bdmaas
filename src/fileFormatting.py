import os

class fileformatting:
    
    def getfirstfilename(self,dataset_name):
#         for files in os.listdir("/home/meet/workspace/bdmaas/data/"+dataset_name):
#             print files 
        return os.listdir("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/data/train")[0]
        
    def format(self,dataset_name,type):
        filename=os.listdir("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/data/"+type)[0]
        if not os.path.exists("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/temp/data"+"/"+type):
            os.makedirs("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/temp/data"+"/"+type)
        f=open("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/data/"+type+"/"+filename)
        f1=open("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/temp/data/"+type+"/"+filename,"w")
        i=0
        for line in f:
            if (i==0):
                i+=1
                continue
            line=line.replace(" ","")
            line=line.replace("'","")
            data=line.split("\"")
            j=0;
            for j in range(0,len(data)):
                if (j%2!=0):
                    data[j]=data[j].replace(",","")
                f1.write(data[j])
        f1.close()
        f.close()
        
    #@staticmethod    
    def fetchColumnNumber(self,dataset_name,column_name):
        filename=os.listdir("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/data/train")[0]
        f=open("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/data/train/"+filename)
        line=f.readline()
        columns=line.split(",")
        for i in range(0,len(columns)):
            if(column_name==columns[i]):
                print "column number is "+ str(i+1)
                return i+1
                break;
    
    def fetchTotalRowNumber(self,dataset_name):
        filename=os.listdir("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/data/train")[0]
        f=open("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/data/train/"+filename)
        line=f.readline()
        columns=line.split(",")
        print "total no. of columns is "+(len(columns))
        return len(columns)+1
    
    def randomForestLabelString(self,dataset_name,predictor,target):
        categoryNumber=fileformatting.fetchColumnNumber(self, dataset_name, predictor)
        labelNumber=fileformatting.fetchColumnNumber(self, dataset_name, target)
        randomforeststring=""
        for i in range(1,fileformatting.fetchTotalRowNumber(self, dataset_name)):
            if (i==categoryNumber):
                randomforeststring+=" C"
            elif (i==labelNumber):
                randomforeststring+=" L"
            else:
                randomforeststring+=" I"
        return randomforeststring