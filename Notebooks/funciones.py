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