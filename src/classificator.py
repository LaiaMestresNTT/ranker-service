from groq import Groq
import json

client = Groq(api_key="TU_API_KEY")

def obtener_estrategia(query_usuario, lista_categorias):
    prompt = (f"Producto: {query_usuario}. "
                  f"Categorías: {lista_categorias}. "
                  f"Responde solo JSON: {{'ids': [int], 'keywords': [str]}}")

    res = client.chat.completions.create(
        model="llama-3.2-3b-preview",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"})

    return json.loads(res.choices[0].message.content)