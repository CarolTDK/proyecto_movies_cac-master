#desde la terminal pip install mysql-connector-python
import mysql.connector 

def conectar():
    #mis credenciales
    conexion = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='C4r0ltdkd3v', #mi contraseña
        database='cacmovies' #nombre de la base de datos
    )
    return conexion

def desconectar(conexion):
    # Cerrar la conexión a la base de datos
    if conexion:
        conexion.close()

def agregar_pelicula(titulo, anioEstreno, duracion, categoriaId):
    try: #lo segundo que se ejecuta
        conexion = conectar()
        cursor = conexion.cursor()

        #insertar el producto en la tabla productos
        query = "INSERT INTO peliculas (titulo, anioEstreno, duracion, categoriaId) VALUES (%s, %s, %s, %s)"
        datos_pelicula = (titulo, anioEstreno, duracion, categoriaId)
        cursor.execute(query, datos_pelicula)

        conexion.commit()
        cursor.close()
        print("Pelicula agregada con exito!")

    except mysql.connector.Error as error: #si se produce algun error
        print(f"Error al agregar la pelicula -> {error}")

    finally: #lo primero que se ejecuta
        desconectar(conexion)

def ver_peliculas():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        #obtener todos los registros y todos los campos de la tabla peliculas
        query = "SELECT * FROM peliculas"
        cursor.execute(query)
        peliculas = cursor.fetchall() #guardamos el resultado de ejecutar la linea anterior

        cursor.close()
        return peliculas

    except mysql.connector.Error as error:
        print(f"Error al obtener las peliculas -> {error}")

    finally:
        desconectar(conexion)

def eliminar_pelicula(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # eliminar el producto de la tabla peliculas segun id
        query = "DELETE FROM productos WHERE id = %s"
        dato_pelicula = (id,)
        cursor.execute(query, dato_pelicula)

        conexion.commit()
        cursor.close()
        print(f"Pelicula con id {id} , eliminado con exito!")

    except mysql.connector.Error as error:
        print(f"Error al eliminar la pelicula -> {error}")

    finally:
        desconectar(conexion)

def actualizar_pelicula(id, titulo, anioEstreno, duracion, categoriaId):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Actualizar la pelicula en la tabla peliculas
        query = "UPDATE peliculas SET titulo = %s, anioEstreno = %s, duracion = %s, categoriaId = %s WHERE id = %s"
        datos_pelicula = (titulo, anioEstreno, duracion, categoriaId, id)
        cursor.execute(query, datos_pelicula)

        conexion.commit()
        cursor.close()
        print(f"Pelicula con ID {id} actualizada con exito!")

    except mysql.connector.Error as error:
        print(f"Error al actualizar la pelicula -> {error}")

    finally:
        desconectar(conexion)




###########PROGRAMA PPAL
    # Agregar y ver productos
# agregar_producto('Teclado USB 101 teclas', 10, 4500)
# agregar_producto('Mouse gamer', 15, 1500)
# agregar_producto('Monitor gamer', 5, 221500)

# productos = ver_productos()
# if productos:
#     print("Lista de productos:")
#     for producto in productos:
#         print(producto)

    # Eliminar un producto por ID
# eliminar_producto(1)  # Suponiendo que el ID del producto a eliminar es 1
# print(ver_productos())

#     # Actualizar un producto por ID
# actualizar_producto(2, 'Mouse gamer inalambrico', 20, 6000)  # Suponiendo que el ID del producto a actualizar es 2
# print(ver_productos())