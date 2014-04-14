from bottle import route, run, template, static_file, get, request, FileUpload, TEMPLATE_PATH, TEMPLATES
import os
from dataset import datasets
datasetObj=datasets()


TEMPLATES.clear()
@route('/')
def home():
    TEMPLATE_PATH.insert(0,"../views")
    return template('index.tpl', msg="")

@route('/upload', method='POST')
def do_upload():
    TEMPLATE_PATH.insert(0,"../views")
    category = request.forms.category
    upload = request.files.data
    print category
    raw = upload.file.read() # This is dangerous for big files
    filename = upload.filename
    
    print "Directory: %s \nFilename: %s\nSize: %d bytes." %(category, filename, len(raw))
    
    save_path = "../data/{category}/data".format(category=category)
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        
    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    
    FileUpload.save(upload, file_path, overwrite=True, chunk_size=2*16)
    with open(file_path, 'w+') as open_file:
        open_file.write(raw)

    msg="file is uploaded"
    
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

        header_link.bind('mousedown', function () {
            console.log($(this).find('a').text());
            var temp_dataset_name=$(this).find('a').text();
            console.log(temp_dataset_name);
            $.get(\'/get_columns/\'+temp_dataset_name,function(data){
                    $(\'#showColumns\').html(data)
                    });
        });
        </script>'''+innerHtml
    
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
    print column_names
    result=""
    for columns in column_names:
        result+=columns
    return '<div id=selcols>'+result+'</div>' 

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='../views/scripts')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='../views/scripts')

run(host='0.0.0.0', port=8080)