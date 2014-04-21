import subprocess
import requests
import json

from fileFormatting import fileformatting
fileformattingObj=fileformatting()


class datasets:
    
    def upload(self,dataset_name):
        bashCommand='curl -i -X PUT "http://54.186.225.72:50070/webhdfs/v1/data/'+dataset_name+'?user.name=ubuntu&op=MKDIRS"'
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is "+output)
        print (error)
        
        fileformattingObj.format(dataset_name,"train")
        fileformattingObj.format(dataset_name,"test")
                
        bashCommand='$HADOOP_PREFIX/bin/hadoop fs -copyFromLocal ~/code/bdmaas/data/'+dataset_name+'/temp/data/ /data/'+dataset_name+'/'
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

#         bashCommand='rm ~/code/data/*'
#         process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#         output, error = process.communicate()       
        
        return output
    
    def get_datasets(self):
        r = requests.get('http://54.186.225.72:50070/webhdfs/v1/data?op=LISTSTATUS')

        name_list=[]
        for v in r.json()['FileStatuses']['FileStatus']:
            if(v['type']=="DIRECTORY"):
                #print v['pathSuffix']
                name_list.append(v['pathSuffix'])
        return name_list
    
    def get_datasetsFirstFilename(self,dataset_name):
        url='http://54.186.225.72:50070/webhdfs/v1/data/'+dataset_name+'/data/train?op=LISTSTATUS'
        r = requests.get(url)
        print r.json()
        name_list=[]
        for v in r.json()['FileStatuses']['FileStatus']:
            if(v['type']=="FILE"):
                print v['pathSuffix']
                name_list.append(v['pathSuffix'])
        return name_list
    
    def get_datasetsFirstFilenametest(self,dataset_name):
        url='http://54.186.225.72:50070/webhdfs/v1/data/'+dataset_name+'/data/test?op=LISTSTATUS'
        r = requests.get(url)
        print r.json()
        name_list=[]
        for v in r.json()['FileStatuses']['FileStatus']:
            if(v['type']=="FILE"):
                print v['pathSuffix']
                name_list.append(v['pathSuffix'])
        return name_list


    def get_columns(self,dataset_name):
#         dataset_files=datasets.get_datasetsFirstFilename(self, dataset_name)
#         print (dataset_files[0])
#         
#         bashCommand="$HADOOP_PREFIX/bin/hadoop fs -cat /data/"+dataset_name+"/data/train/"+dataset_files[0]+" | awk 'NR==1'"
#         
#         process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#         output, error = process.communicate()
#         #print ("output is "+output)
#         original_line=output.split("\n")
#         column_names=original_line[0].replace("\r","").split(",")
#         print column_names

        filename=fileformattingObj.getfirstfilename(dataset_name)
        f=open("/home/ubuntu/code/bdmaas/data/"+dataset_name+"/data/train/"+filename)
        line=f.readline();
        return line.split(",")
        
    