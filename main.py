import pandas as pd
import numpy  as np
from datetime import datetime
from fastapi import FastAPI

import uvicorn

from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.utils.extmath           import randomized_svd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise        import linear_kernel


app = FastAPI()
### PRESENTACION:
### Creaoms consulta como presentacion con nuestro nombre
@app.get('/')
def presentacion():
    return 'Carlos_Vargas'

df = pd.read_csv('anime2.csv', sep=',')
    
@app.get("/Recomendacion/{variable}")
def Recomendacion(variable):
    generos = df[df['tags'].apply(lambda x: all(tag in x for tag in variable))][['title', 'tags','rating','votes','description','eps','mediaType','watched']]
    valores = generos.nlargest(10, 'watched')[['title', 'tags','rating','votes','description','eps','mediaType','watched']]
    return valores
