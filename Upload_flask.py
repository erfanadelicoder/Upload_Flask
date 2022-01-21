from flask import Flask, request, redirect
username = "user0"
UPLOAD_FOLDER = 'UPLOAD_FOLDER/' + username


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "NOT FILE FIND"
        file_re = request.files['file']
        if file_re.filename == '':
            return "NOT FILE FIND"
        def allowed_file(FILENAME,ALLOWED_EXTENSIONS):
            return '.' in FILENAME and \
                FILENAME.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS    
        if file_re and allowed_file(file_re.filename,{"py","txt"}):
            print(f"{app.config['UPLOAD_FOLDER']}/{file_re.filename}")
            file_re.save(f"{app.config['UPLOAD_FOLDER']}/{file_re.filename}")#UPLOAD_FOLDER/user0\testflask.txt
            return redirect(request.url)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
app.run(debug="on")    