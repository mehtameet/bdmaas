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

        name_list=[]
        for v in r.json()['FileStatuses']['FileStatus']:
            if(v['type']=="FILE"):
                print v['pathSuffix']
                name_list.append(v['pathSuffix'])
        return name_list


    def get_columns(self,dataset_name):
        dataset_files=datasets.get_datasets(self, dataset_name)
        print (dataset_files[0])
        
        bashCommand="$HADOOP_PREFIX/bin/hadoop fs -cat /data/"+dataset_name+"/data/"+dataset_files[0]+" | awk 'NR==1'"
        
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        #print ("output is "+output)
        original_line=output.split("\n")
        column_names=original_line[0].replace("\r","").split(",")
        print column_names
        return column_names
        
    