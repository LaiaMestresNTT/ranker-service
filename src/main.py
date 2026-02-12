"""""
1. Lo que haremos será pasarle a la IA todas las categorías como RAG o system prompt, y decirle que según el nombre del producto 
    diga a que categoria o categorías de amazon pertenece... 
        ufff que complicado....va a salir mal seguro

2. Le preguntamos a la IA que nos de el nombre que vamos a usar como parámetro para buscar coincidencias 
        
3. Haremos un search query o lo que se para buscar el nombre del parámetro en el título solo en las categorías que nos ha dicho la IA
"""""

from fastapi import FastAPI

from src.classificator import obtener_estrategia
from src.analyzer import calcular_percentiles

app = FastAPI()


#@app.get("/analizar")
#async def analizar(query: str, precio: float, estrellas: float):
    # Suponiendo que 'resumen_categorias' y 'df_parquet' existen
#    estrategia = obtener_estrategia(query, resumen_categorias)
#    resultado = calcular_percentiles(df_parquet, precio, estrellas, estrategia)
#    return {"ia": estrategia, "analisis": resultado}
