import pandas as pd
import  requests
import io

# Extraer archivos API
def extraer_caonjunto(url):
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.content.decode("utf-8")
        df = pd.read_csv(io.StringIO(datos), encoding="utf-8")
        return df
    else:
        raise Exception(response.status_code)
    
# Verificar tipo de dtos de los dataframe
def verificar_datos(df):
    # Comprobamos que el dataframe sea valido
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El parámetro df, debe ser un dataframe de pandas")
    
    # Obtenemos un resumen de tipos de datos y valores nulos 
    resume = {"columna": [], "tipo_dato": [], "datos_nulos": [],
              "porcentaje_nulos": [], "porcentaje_no_nulos": []}
    
    for colum in df.columns:
        no_nulos = (df[colum].count()/len(df)) * 100
        # Advertimos si la columna tiene valores nulos
        if df[colum].isnull().sum():
            print(f"Advertencia: la columna {colum}, tiene valores nulos")
            
        resume["columna"].append(colum)
        resume["tipo_dato"].append(df[colum].apply(lambda x: type(x)).unique())
        resume["datos_nulos"].append(df[colum].isnull().sum())
        resume["porcentaje_nulos"].append(round(100-no_nulos, 2))
        resume["porcentaje_no_nulos"].append(round(no_nulos, 2))
        
    salida = pd.DataFrame(resume)
    return salida

# Función para encontrar valores duplicados
def valores_duplicados(df, columnas):
    # Se filtran las filas duplicadas
    duplicated_rows = df[df.duplicated(subset = columnas, keep = False)]
    
    # Numero de filas duplicadas
    numero_duplicados = duplicated_rows.shape[0]
    
    return duplicated_rows