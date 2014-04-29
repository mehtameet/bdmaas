from bottle import route, run, template, static_file, get, request, FileUpload, TEMPLATE_PATH, TEMPLATES
import os
from dataset import datasets
datasetObj=datasets()

from algorithms import algorithms
algorithmObj=algorithms()

TEMPLATES.clear()
@route('/')
def home():
    TEMPLATE_PATH.insert(0,"../views")
    return template('index.tpl', msg="")

@route('/upload/<dataType>', method='POST')
def do_upload(dataType):
    TEMPLATE_PATH.insert(0,"../views")
    category = request.forms.category
    upload = request.files.data
    print category
    raw = upload.file.read()
    filename = upload.filename
    
    print "Directory: %s \nFilename: %s\nSize: %d bytes." %(category, filename, len(raw))
    
    if(dataType=="train"):
        save_path = "../data/{category}/data/train".format(category=category)
    else:
        save_path = "../data/{category}/data/test".format(category=category)
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        
    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    
    FileUpload.save(upload, file_path, overwrite=True, chunk_size=2*16)
    with open(file_path, 'w+') as open_file:
        open_file.write(raw)

    msg="file is uploaded"
    
    if(dataType=="test"):
        datasetObj.upload(category)
    
    return template('index.tpl', msg=msg)

@route('/get_dataset')
def get_datasets():
    datasetnames=datasetObj.get_datasets()
    innerHtml=""
    for i in datasetnames:
        innerHtml+='<div class="showDatasets"><a href="#">'+i+'</a></div>'

    return '''
        <script src="http://code.jquery.com/jquery-2.1.0.js"></script>
        <script>
        var header_link = $('.showDatasets');
        $('#datasetname1').val();
        header_link.bind('mousedown', function () {
            console.log($(this).find('a').text());
            var temp_dataset_name=$(this).find('a').text();
            console.log(temp_dataset_name);
            $.get(\'/get_columns/\'+temp_dataset_name,function(data){
                    $(\'#showColsTr\').html(data)
                    });
        });
        </script>
		<script>
        var header_link = $('.showDatasets');
        $('#datasetname2').val();
        header_link.bind('mousedown', function () {
            console.log($(this).find('a').text());
            var temp_dataset_name=$(this).find('a').text();
            console.log(temp_dataset_name);
            $.get(\'/get_columns/\'+temp_dataset_name,function(data){
                    $(\'#showColsRF\').html(data)
                    });
        });
        </script>
		'''+innerHtml
    
@route('/get_columns/<name>')
def get_columns(name):
    print name
    column_names=datasetObj.get_columns(name)
#     return '''
#         <div id="showColumns">
#         Hey<input type="checkbox" id="cb1" value="true" />
#         there<input type="checkbox" id="cb2" value="true" />
#         <div id="showCBs" style="display:none">
#             <p>IN COLUMNS _ CHECKBOX</p>
#         </div>
#         <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
#         <script>
#             $("#cb1").on('change',(function(){
#                 console.log($(this).prop('checked') == 'checked');
#         });
#         </script>
#         
#         ''' + name
    print "inside index.py"
    print column_names
    result='''
    <script src="http://code.jquery.com/jquery-2.1.0.js"></script>
        <script>
        $('#datasetname').val("'''+name+'''");
        $('#datasetname1').val("'''+name+'''");
        $('#datasetname2').val("'''+name+'''");
        </script>
			<div class="panel panel-default col-lg-4" align="center">
				<div class="panel-heading">
					<h3 class="panel-title">Columns</h3>
				</div>
				<div id="showingCols" style="text-align:center; overflow-y: auto; height:200px;">
				
	'''
    for columns in column_names:
        result+='<li>'+columns+"</li>"
    result+='</div></div>'
    return result
	
	#return '''
     #   <script src="http://code.jquery.com/jquery-2.1.0.js"></script>
      #  <script>
       # $('#datasetname').val("'''+name+'''");
       # $('#datasetname1').val("'''+name+'''");
       # $('#datasetname2').val("'''+name+'''");
       # </script>'''+result 

@route('/run_algorithms/<name>',method='POST')
def run_algorithms(name):
    predictor = request.forms.predictor
    target = request.forms.target
    dataset_name = request.forms.datasetname
    print predictor
    print target
    print dataset_name
    print name
    
    if(name=="train"):
        algorithmObj.trainlogistic(dataset_name, predictor.split(','), target)
        return algorithmObj.runlogistic(dataset_name)
    else:
        algorithmObj.trainrandomforest(dataset_name, predictor.split(','), target)
        algorithmObj.testrandomforest(dataset_name)
        return algorithmObj.runrandomforest(dataset_name)
    
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
	
@get('/<filename:re:.*\.gif>')
def stylesheets(filename):
    return static_file(filename, root='.')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='../views/scripts')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='../views/scripts')

run(host='0.0.0.0', port=8080)
