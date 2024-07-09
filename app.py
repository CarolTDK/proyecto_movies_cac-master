'''En la terminal
pip install mysql-connector-python
python.exe -m pip install --upgrade pip
pip install Flask
pip install flask-cors
pip install Werkzeug'''

from flask import Flask, jsonify, request 
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/peliculas', methods=['GET'])
def ver_peliculas():
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='C4r0ltdkd3v', #mi contraseña
        database='cacmovies' #nombre de la base de datos
    )
    
    cursor=db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM peliculas')
    
    peliculas=cursor.fetchall()
    
    cursor.close()
    return jsonify(peliculas)

if __name__ == '__main__':
    app.run(debug=True) 
    
     