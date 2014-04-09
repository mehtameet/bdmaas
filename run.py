from bottle import request,response,route,run
import os 

@route('/upload', method='GET')
#@route('/upload', method='POST')
def do_upload():
    #category   = request.forms.get('filename')
    upload     = request.files.get('myfile').filename
    #name, ext = os.path.splitext(upload.filename)
    #print category
    print upload
    return 'OK'

run(host='localhost', port=8080, debug=True)