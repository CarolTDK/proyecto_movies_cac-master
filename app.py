from flask import Flask, jsonify , request 
import mysql.connector
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 


#Consulta de películas
@app.route('/peliculas', methods=['GET'] )
def ver_peliculas():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Gaston372!',
        database='CacMovies'
    )
    
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM peliculas")
    
    peliculas = cursor.fetchall()
    
    cursor.close()
    return jsonify(peliculas)

#Baja de película
@app.route('/eliminar_pelicula/<int:id>', methods=['DELETE'] )
def eliminar_pelicula(id):
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Gaston372!',
        database='CacMovies'
    )
    
    cursor = db.cursor()
    cursor.execute("DELETE FROM peliculas WHERE id = %s",(id,))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"ELIMINADO!"})


#Alta de película
@app.route('/nueva_pelicula', methods=['POST'] )
def agregar_pelicula():
    info = request.json
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Gaston372!',
        database='CacMovies'
    )
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO peliculas (titulo,anioEstreno,categoriaId,duracion) VALUES (%s,%s,%s,%s)", (info["titulo"],info["anioEstreno"],info["categoriaId"],info["duracion"]))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"AGREGADA CON EXITO!"})

#Modificación de datos de película
@app.route('/actualizar_pelicula/<int:id>', methods=['PUT'] )
def modificar_pelicula(id):
    info = request.json
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Gaston372!',
        database='CacMovies'
    )
    
    cursor = db.cursor()
    cursor.execute("UPDATE peliculas SET titulo= %s , anioEstreno = %s, categoriaId= %s, duracion= %s WHERE id = %s", (info["titulo"],info["anioEstreno"],info["categoriaId"],info["duracion"],id))
    db.commit() 
    cursor.close()
    return jsonify({"mensaje":"ACTUALIZADA CON EXITO!"})

if __name__ == '__main__':
    app.run(debug=True)
    