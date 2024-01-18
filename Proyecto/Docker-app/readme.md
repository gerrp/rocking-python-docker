# Aplicación web flask
Hice uso de las librerias:                                                              

**flask**, para el cuerpo base de la aplicación                                                          
                                                                            
**os**, para guardar/eliminar los archivos subidos                                        
                                                                                    
**werkzeug.utils**, para seguridad en la carga de archivos                                       
## Primer paso (Variable CARPETA)                                                                
Como primer paso definí la ubicación de almacenamiento de archivos en la variable **CARPETA**, se la asigno a **app.config['UPLOAD_FOLDER']** para utilizarla más adelante                          
## Segundo paso (Funcionalidad "/" - subir archivos)
La funcionalidad guarda el archivo seleccionado por el usuario en la variable **file** , si no se sube nada retorna un mensaje de **Archivo no seleccionado**. Llamo a la función **secure_filename** para comprobar la seguridad del nombre del archivo y finalmente este se guarda con ayuda de **os**
utilizando la variable **CARPETA** ( ./Archivos/ejemplo.txt )
## Tercer paso (Funcionalidad "/ls" - ver archivos)
La funcionalidad utiliza **os** para obtener información del nombre de los archivos sobre el directorio de almacenamiento, luego los ordena y los muestra
## Cuarto paso (Funcionalidad "/rm" - borrar archivos)
La funcionalidad guarda el texto introducido por el usuario y **os** une ese nombre con el del directorio de almacenamiento, verifica su existencia y lo elimina, caso contrario retorna un mensaje de **Archivo no encontrado**
                                      
