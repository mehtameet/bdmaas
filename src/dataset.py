import subprocess

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
    