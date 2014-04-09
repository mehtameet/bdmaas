import subprocess
import requests
import json

class datasets:
    
    def upload(self,dataset_name):
        bashCommand='curl -i -X PUT "http://54.186.225.72:50070/webhdfs/v1/data/'+dataset_name+'?user.name=ubuntu&op=MKDIRS"'
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print ("output is "+output)
        print (error)
        
        bashCommand='$HADOOP_PREFIX/bin/hadoop fs -copyFromLocal ~/code/data/ /data/'+dataset_name+'/'
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        bashCommand='rm ~/code/data/*'
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()       
        
        return output
    
    def get_datasets(self,dataset_name):
        r = requests.get('http://54.186.225.72:50070/webhdfs/v1/data/'+dataset_name+'/data?op=LISTSTATUS')
        #print r.json()
#         for v in r.json():
#             print v
#         print r.json()['FileStatuses']['FileStatus']
        name_list=[]
        for v in r.json()['FileStatuses']['FileStatus']:
            if(v['type']=="FILE"):
                print v['pathSuffix']
                name_list.append(v['pathSuffix'])
        return name_list
#         bashCommand='curl -i "http://54.186.225.72:50070/webhdfs/v1/data/'+dataset_name+'/data?op=LISTSTATUS"'
#         process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#         output, error = process.communicate()
#         print ("output is "+output)
#         print (error)
#         return output
    