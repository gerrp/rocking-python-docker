import os
from flask import Flask, request
from werkzeug.utils import secure_filename

CARPETA = './Archivos' ### Carpeta para almacenar los archivos

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = CARPETA ### Definimos UPLOAD_FOLDER con la variable CARPETA 

@app.route('/', methods=['GET', 'POST']) ### Funcionalidad - Subir archivos
def upload():
    if request.method == 'POST':
        file = request.files['file'] 
        if file.filename == '':
            return("<h1> Archivo no seleccionado </h1>")
        fileS = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], fileS))
        return("<h1> Archivo subido exitosamente </h1>")
         
    return '''
    <!doctype html>
    <h1>Subir nuevo archivo</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Cargar>
    </form>
    '''

@app.route('/ls',methods=['GET']) ### Funcionalidad - Ver archivos
def list_files(): 
    if request.method == 'GET':
        fileList = os.listdir('./Archivos')
        filesJoin = '<br>'.join(fileList) 

        return '''
        <h1> Lista de archivos disponibles </h1>
        <p>{}</p>
        '''.format(filesJoin)


        
@app.route('/rm',methods=['GET','POST']) ### Funcionalidad - Borrar archivos
def remove_file():
    if request.method == 'POST':
     eliminar = request.form.get('eliminar')
     eliminar_dir = os.path.join(app.config['UPLOAD_FOLDER'],eliminar)
     if os.path.exists(eliminar_dir):
            os.remove(eliminar_dir)
            return ''' <h1> Archivo eliminado </h1> '''
     else:
            return ''' <h1> Archivo no encontrado </h1>'''
     
    return '''
        <h1> Eliminar archivos </h1>
        <br>
        <form method="POST">
            <div><label>Archivo a eliminar: <input type="text" name="eliminar"></label></div>
              <input type="submit" value="Submit">
          </form>
        <p> Ver archivos disponibles en: <strong> localhost:5000/ls </strong> </p>
          '''

