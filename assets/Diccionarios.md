Diccionario de Google Maps

     [X]  = Campos de los que vamos a prescindir

Explicación de Review-estados

user_id: El ID único del usuario que dejó la revisión.

name: El nombre del usuario que dejó la revisión 

time: La marca de tiempo en la que se dejó la revisión, en milisegundos desde la época Unix.

rating: La calificación dada por el usuario.

text: El texto de la revisión que dejó el usuario.

gmap_id: El ID de Google Maps asociado al lugar.

[X] pics: En caso de que el usuario haya adjuntado imágenes a su revisión.

[X] resp: Si el propietario del negocio ha respondido a la revisión, aquí se proporciona la marca de tiempo de la respuesta y el texto de la respuesta.



Explicación Metadata_sitios 

name: El nombre del comercio

address: La dirección del comercio.

gmap_id: La identificación en Google Maps del lugar.

latitude y longitude: Las coordenadas 
geográficas de la ubicación del comercio.

category: La categoría a la que pertenece el comercio 

avg_rating: El promedio de calificación del comercio.

num_of_reviews: El número de reseñas que ha recibido el comercio.

price: Un indicador del rango de precios del comercio.

hours: El horario de atención del comercio durante los diferentes días de la semana.




[X] description: Una breve descripción del comercio.

[X] MISC: Información adicional sobre opciones de servicio, salud y seguridad, accesibilidad, planificación y métodos de pago

[X] state: El estado actual del comercio

[X] relative_results: Información relacionada con los resultados relativos del comercio en Google Maps.

[X] url: El enlace de Google Maps al lugar.



Diccionario de Yelp!

Explicación 

business.pkl

business_id: Identificador único de 22 
caracteres para el negocio.

name: Nombre del negocio.

address: Dirección completa del negocio.

city: Ciudad donde se encuentra el negocio.

state: Código de 2 letras del estado donde se ubica el negocio.

postal code: Código postal del negocio.

latitude: Latitud geográfica del negocio.

longitude: Longitud geográfica del negocio.

stars: Puntuación del negocio en estrellas, redondeada a 0.5.

review_count: Número de reseñas que tiene el negocio.

is_open: Indica si el negocio está abierto (1) o cerrado (0).

attributes: Atributos del negocio, como si ofrece comida para llevar, estacionamiento, etc.

categories: Lista de categorías a las que pertenece el negocio.

hours: Horario de atención del negocio durante los diferentes días de la semana.
review.json

review_id: Identificador único de 22 caracteres para la reseña.

user_id: Identificador único de 22 caracteres para el usuario que escribió la reseña.

business_id: Identificador único de 22 caracteres para el negocio al que se refiere la reseña.

stars: Puntuación de la reseña en estrellas (1 al 5).

date: Fecha en formato YYYY-MM-DD en la que se escribió la reseña.

text: Texto completo de la reseña en inglés.

useful: Número de votos que indica cuántos usuarios encontraron útil la reseña.

funny: Número de votos que indica cuántos usuarios encontraron graciosa la reseña.

cool: Número de votos que indica cuántos usuarios encontraron genial la reseña.
user.parquet

user_id: Identificador único de 22 caracteres para el usuario.

name: Nombre del usuario.

review_count: Número de reseñas escritas por el usuario.

yelping_since: Fecha en formato YYYY-MM-DD en la que el usuario se unió a Yelp.

friends: Lista de identificadores de usuario que son amigos del usuario.

useful, funny, cool: Número de votos útiles, graciosos y geniales marcados por el usuario.

fans: Número de seguidores que tiene el usuario.

elite: Lista de años en los que el usuario fue miembro elite.

average_stars: Promedio de las calificaciones de las reseñas del usuario.

compliment_...: Diversos tipos de cumplidos recibidos por el usuario.

checkin.json

business_id: Identificador único de 22 caracteres para el negocio al que se refiere el registro.

date: Lista de fechas separadas por coma en formato YYYY-MM-DD HH:MM:SS, que indica los momentos en los que se realizó el check-in en el negocio.

tip.json

text: Texto del tip, un consejo o sugerencia corta.

date: Fecha en formato YYYY-MM-DD en la que se escribió el tip.

compliment_count: Número total de cumplidos recibidos por el tip.

business_id: Identificador único de 22 caracteres para el negocio al que se refiere el tip.

user_id: Identificador único de 22 caracteres para el usuario que escribió el tip.





