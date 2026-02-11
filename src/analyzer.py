import pandas as pd

def calcular_percentiles(df, precio_usuario, estrellas_usuario, estrategia):
    # Filtro por IDs
    subset = df[df['category_id'].isin(estrategia['ids'])]
    # Filtro por Keywords

    if estrategia['keywords']:
        regex = '|'.join(estrategia['keywords'])
        subset = subset[subset['title'].str.contains(regex, case=False, na=False)]

        if len(subset) < 5: return {"error": "pocos datos"}
        # Percentiles ....
        p_precio = (subset['price'] < precio_usuario).mean() * 100
        p_estrellas = (subset['stars'] < estrellas_usuario).mean() * 100

    return { "percentil_precio": round(p_precio, 2), "percentil_estrellas": round(p_estrellas, 2),"comparado_con": len(subset) }
