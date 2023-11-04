import pymysql
from sqlalchemy import create_engine

# Crear conexion a bd
conexion = pymysql.connect(
    host="localhost",
    port= 3306,
    user= "root",
    passwd= "pasa_perra",
    database= "Telecomunicaciones",
)
# Crear cursor
cursor = conexion.cursor()

# Crear conexio con create_engine
host = "localhost"
port = 3306
user = "root"
password = "pasa_perra"
database = "Telecomunicaciones"

conexion_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(conexion_string)
