# ⚙️​🔧​🤖​ Modelo de Machine Learning: ⚙️​🔧​🤖​
Creamos las siguientes dos funciones basadas en modelos de Machine Learning 
### 1. Sistema de recomendación user-item: 😀​🏠​

- **def recomendacion_restaurante(user_id):**

> Ingresando el id de un usuario, deberíamos recibir una lista con 5 restaurantes recomendados para dicho usuario.

### 2.  Sistema de recomendación item-item: ​​🏠​​🏠​​

- **def recomendacion_item_item(busines_id):** 

> Ingresando el id de un negocio, deberíamos recibir una lista con 5 restaurantes recomendados similares a dicho negocio.

## 📋 **Tabla de contenidos**
- [Funcionamiento de la Funcion 1. Sistema de Recomendacion user-item](#Funcionamiento-de-la-Funcion-1-Sistema-de-Recomendacion-user-item)
- [Aplicaciones Comerciales](#Aplicaciones-Comerciales)
- [Funcionamiento de la Funcion 2. Sistema de Recomendacion item-item ](#Funcionamiento-de-la-Funcion-2-Sistema-de-Recomendacion-item-item )
- [Aplicaciones Comerciales](#Aplicaciones-Comerciales)

# Funcionamiento de la Funcion 1. Sistema de Recomendacion user-item 😀​🏠​
### Modelo de Filtrado Colaborativo 
#### 1. Importar bibliotecas:
 - Importa las bibliotecas necesarias, como pandas para el manejo de datos y surprise para el filtrado colaborativo.

#### 2. Cargar datos: 
- Carga un archivo CSV que contiene las reseñas de los usuarios sobre diferentes negocios en un DataFrame de pandas.

#### 3. Selección de columnas relevantes: 
- Selecciona las columnas 'name', 'category', 'rating' y 'user_id' del DataFrame de reseñas. Esto puede ser útil si solo estamos interesados en estas columnas para un análisis específico.

#### 4. Preprocesamiento de categorías: 
- Convierte las categorías de negocios en cadenas de texto y las guarda en una lista. Este preprocesamiento puede ser útil para análisis posteriores que requieran el manejo de categorías de negocios.

#### 5. Cálculo de similitud: 
- Utiliza el modelo de spaCy para calcular la similitud entre las palabras clave ('restaurant', 'food', 'cuisine') y las categorías de negocios. Esto es útil para agrupar categorías de negocios similares o para recomendar negocios basados en las preferencias de los usuarios.

#### 6. Filtrado de categorías relacionadas:
- Filtra las categorías de negocios que tienen una similitud superior a un umbral especificado con las palabras clave dadas. 

#### 7. Eliminación de columnas y renombrado:
- Elimina la columna 'category' del DataFrame y renombra la columna 'name' como 'business_id'. Esto sirve para simplificar el DataFrame o para prepararlo para análisis adicionales.

#### 8. Exportación de datos:
- Exporta el DataFrame procesado a un nuevo archivo CSV llamado 'data_user_item.csv'. Esto podría ser útil para compartir o para utilizar los datos procesados en otros análisis o aplicaciones.

#### 9. Entrenamiento de modelo de filtrado colaborativo: 
- Utiliza la biblioteca Surprise para entrenar un modelo de filtrado colaborativo basado en el algoritmo SVD (Descomposición en Valores Singulares). 

#### 10. Optimización de parámetros del modelo: 
- Utiliza GridSearchCV para encontrar los mejores parámetros del modelo SVD utilizando validación cruzada. Esto ayuda a mejorar el rendimiento del modelo de filtrado colaborativo.

#### 11. Guardado del modelo: 
- Guarda el mejor modelo entrenado en un archivo llamado 'modelo_user_item.pkl'. Esto permite reutilizar el modelo entrenado sin tener que entrenarlo nuevamente cada vez que se necesite hacer una recomendación.

#### 13. Función de recomendación de usuario: 
- Define una función que utiliza el modelo entrenado para hacer recomendaciones de negocios para un usuario específico. 

# Aplicaciones Comerciales 😀​​📉​📈​🏙️​
### * Sistemas de Recomendación Personalizados: 
Se puede utilizar para recomendar productos, servicios o contenido personalizado a los usuarios basándose en sus preferencias históricas.

### * Filtrado de Contenido: 
Puede utilizarse para filtrar contenido relevante para los usuarios en función de sus intereses y comportamientos pasados.

### * Personalización de la Experiencia del Usuario: 
Permite personalizar la experiencia del usuario en aplicaciones y plataformas en línea, lo que puede aumentar la satisfacción del usuario y la retención.

### * Optimización de Contenidos:
 Ayuda a las empresas a optimizar la distribución de contenido o productos, mejorando así la relevancia y la satisfacción del usuario.

# Funcionamiento de la Funcion 2. Sistema de Recomendacion item-item ​​🏠​​🏠​​
Por supuesto, aquí tienes un desglose más detallado del código y sus posibles aplicaciones comerciales:

#### 1. Importación de bibliotecas:
- Se importan varias bibliotecas populares para el análisis de datos y el aprendizaje automático, como pandas para la manipulación de datos, scikit-learn para el modelado de aprendizaje automático, y spaCy para procesamiento de lenguaje natural (NLP). Además, se importan módulos específicos como `KNeighborsTransformer` de scikit-learn y `SVD` de Surprise para recomendaciones.

#### 2. Lectura de datos:
- Se lee un archivo CSV que contiene información sobre restaurantes. Esto podría ser cualquier conjunto de datos que incluya detalles relevantes de los restaurantes, como nombre, categoría, calificación promedio y número de reseñas. Esta información es crucial para el análisis y la recomendación posterior.

#### 3. Procesamiento de datos:
- Se seleccionan las columnas relevantes del conjunto de datos, lo que ayuda a reducir el tamaño del conjunto de datos y a centrarse en la información necesaria para el análisis.
- Se convierten las categorías únicas en cadenas de texto. Esto podría ser útil para realizar operaciones de texto o análisis de similitud basado en texto en las categorías de los restaurantes.
- Se utiliza spaCy para calcular la similitud entre las categorías de los restaurantes y ciertas palabras clave como "restaurant", "food" y "cuisine". Esto ayuda a identificar qué categorías están más estrechamente relacionadas con estos términos, lo que podría ser útil para la clasificación de restaurantes o la recomendación basada en palabras clave.

#### 4. Modelado:
- Se utiliza `KNeighborsTransformer` de scikit-learn para encontrar restaurantes similares en función de sus características, como la calificación promedio y el número de reseñas. Este modelo encuentra restaurantes cercanos en un espacio de características multidimensionales, lo que permite identificar restaurantes similares en términos de popularidad y calidad.
- El modelo se entrena utilizando los datos de los restaurantes seleccionados y se guarda en un archivo `.pkl`. Este modelo puede ser utilizado posteriormente para hacer recomendaciones de restaurantes similares de manera eficiente.

#### 5. Función para encontrar restaurantes similares:
- Se define una función `restaurantes_similares(restaurant_name, n_restaurants)` que carga el modelo previamente entrenado y los datos de restaurantes.
- Utiliza el modelo para encontrar los restaurantes más similares al restaurante de entrada especificado, utilizando la distancia euclidiana en el espacio de características definido por el modelo.
- Devuelve una lista de nombres de restaurantes similares, lo que permite a los usuarios explorar otras opciones de restaurantes que puedan ser de su interés.

# Aplicaciones comerciales: 😀​​📉​📈​🏙️​

### Recomendación de restaurantes: 
El sistema puede ser utilizado por aplicaciones de reservas de restaurantes para recomendar restaurantes similares a los que un usuario ha disfrutado previamente. Esto mejora la experiencia del usuario y aumenta la probabilidad de que los usuarios encuentren restaurantes que se ajusten a sus preferencias.
  
### Análisis de mercado:
 Las empresas de análisis de datos pueden utilizar este sistema para comprender mejor el mercado de restaurantes y las tendencias de consumo. Esto puede ayudar a los propietarios de restaurantes y a los inversores a tomar decisiones informadas sobre dónde abrir nuevos restaurantes o cómo posicionar sus negocios en función de la demanda y la competencia en diferentes áreas.

### Optimización de ubicación: 
Los datos sobre la similitud entre restaurantes pueden ser utilizados para tomar decisiones sobre la ubicación óptima de nuevos establecimientos. Al identificar áreas con alta demanda de un tipo particular de restaurante y baja competencia, las empresas pueden maximizar sus oportunidades de éxito al abrir nuevos locales.
