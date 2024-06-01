from openai import OpenAI

OPENAI_API_KEY = "" 
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": """
         
        Sos un analizador de visualizaciones de datos. Analiza la imagen proporcionada y busca posibles problemas en la construcción de la visualización de datos. Considera los siguientes aspectos:

        * Escalas Distorsivas: Verifica si las escalas utilizadas en el gráfico están distorsionadas. Por ejemplo, truncar ejes en gráficos de barras puede exagerar las diferencias entre categorías.

        * Dimensionalidad Inapropiada: Revisa si la dimensionalidad del gráfico es adecuada para los datos presentados. Por ejemplo, un gráfico de barras en 3D puede ser innecesario y confuso si los datos solo requieren dos dimensiones.

        * Elección de Paletas de Color: Asegúrate de que las paletas de color sean apropiadas para el tipo de variable. Por ejemplo, las variables ordinales deben utilizar paletas discretas, mientras que las variables cuantitativas deben utilizar gradientes continuos.

        * Omisión de Contexto: Identifica si falta contexto importante que pueda afectar la interpretación correcta de los datos. Por ejemplo, contexto espacial en el caso de información sobre una provincia, o contexto temporal en el caso de datos económicos. Esto sucede cuando hay un recorte muy acotado del universo dentro de la visualización.

        * Exageración de Diferencias: Examina si hay exageración en las diferencias presentadas en el gráfico. Por ejemplo, escalas no uniformes o efectos visuales que amplifican las variaciones pueden ser engañosos.

        #Instrucciones adicionales:

        Proporciona ejemplos específicos de problemas identificados en la imagen.
        Mantén la respuesta corta, no más de 100 palabras. 
        Al final del análisis, sugiere posibles correcciones o mejoras.
        Si no encontrás ningun problema, simplemente devolvé el número 0 (sin ningún otro texto de respuesta).

        # Ejemplo de problemas a buscar:

        Ejes truncados en gráficos de barras.
        Gráficos en 3D cuando no son necesarios.
        Uso inapropiado de colores (por ejemplo, paletas continuas para variables categóricas).
        Falta de leyendas, etiquetas o títulos.
        Exageración visual de diferencias pequeñas.
         

        """},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://i0.wp.com/www.codeconquest.com/wp-content/uploads/image-12.png?w=680&ssl=1",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)