<h1 align="center">🍽️ **`YELP & GOOGLE MAPS REVIEWS `** 🗺️</h1>

## 📋 **Tabla de contenidos**
- [Contexto](#Contexto)
- [Objetivos](#objetivos)
- [MPV](#mpv)
- [Alcance](#fuera-de-alcance)
- [Fuera de alcance](#fuera-de-alcance)
- [KPI's](#kpi´s)
- [Metodología de Trabajo](#metodologia-del-trabajo)
- [Stack Tecnológico](#Stack-Tecnológico)

<!-- Contexto section -->
##  **Contexto**

Como parte de una consultora de data, nos han contratado para poder realizar un análisis del mercado estadounidense. Nuestro cliente es parte de un conglomerado de empresas de restaurantes y afines, y desean tener un análisis detallado de la opinión de los usuarios en Yelp y cruzarlos con los de Google Maps sobre hoteles, restaurantes y otros negocios afines al turismo y ocio, utilizando análisis de sentimientos, predecir cuáles serán los rubros de los negocios que más crecerán o decaerán. Además, desean saber dónde es conveniente emplazar los nuevos locales de restaurantes y afines, y desean poder tener un sistema de recomendación de restaurantes para los usuarios de ambas plataformas para darle al usuario, por ejemplo, la posibilidad de poder conocer nuevos sabores basados en sus experiencias previas.

<!-- objetivos section -->
## **🎯 Objetivos**
### **🌟 Objetivo General**

Desarrollar, implementar y lanzar al mercado un sistema de recomendación de restaurantes utilizando el análisis de las opiniones de los clientes en las plataformas Yelp y Google Maps.

### **🔍 Objetivos específicos**

1. **Análisis de Sentimientos:** Emplearemos técnicas de procesamiento de lenguaje natural para evaluar las opiniones sobre restaurantes y detectar las tendencias actuales en base a estas reseñas.

2. **Identificación de Restaurantes:** Buscaremos aquellos establecimientos con altas puntuaciones pero con un número reducido de reseñas, ya que representan lugares potenciales por descubrir.

3. **Recomendaciones de Calidad:** Proporcionaremos a nuestros usuarios recomendaciones de restaurantes que consistentemente han mantenido un alto estándar de calidad a lo largo del tiempo, asegurando así recomendaciones confiables.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<!-- mpv section -->
## **🚀 MPV**  

El Producto Mínimo Viable (MVP) es una plataforma de recomendación de restaurantes que proporciona las siguientes características:

**Selección de criterio de restaurantes:** Los clientes pueden seleccionar el tipo de restaurantes que desean descubrir. Pueden optar por los mejores restaurantes, lugares por descubrir o restaurantes que garantizan calidad.

**Visualización de resultados:** La plataforma proporcionará una lista de tres restaurantes basada en el criterio seleccionado por el cliente. También aquí pueden incluirse filtros del tipo "por precio", "más antiguo", etc..

<!-- Alcance section -->
## **🌐 Alcance**

**Extracción de Datos:** Recopilaremos y utilizaremos datos de plataformas de reseñas como Google Maps y Yelp.

**Análisis de Datos:** El sistema utilizará técnicas avanzadas de Aprendizaje Automático y Big Data para analizar las reseñas de los usuarios. Este análisis permitirá al sistema identificar tendencias y recomendar lugares consistentemente.

**Cobertura Geográfica:** El sistema se centrará específicamente en los locales de comida en los estados de California, Florida y Nueva York en los Estados Unidos. Sin embargo, el marco subyacente puede ser escalado para incluir otras regiones en el futuro.

**Visualización y Sistema de Recomendación:** El sistema proporcionará una interfaz de usuario intuitiva que permite a los usuarios iniciar sesión, seleccionar su criterio de restaurantes, visualizar los resultados de la recomendación y proporcionar retroalimentación.

**Iteración y Mejora:** Con la retroalimentación de los usuarios, el sistema será iterado y mejorado continuamente para satisfacer mejor las necesidades de los usuarios.

<!-- Fuera de alcance section -->
## **❌ Fuera de alcance**

**Datos en tiempo real:** Dependiendo de las limitaciones de las API de Google Maps y Yelp, puede que no podamos obtener datos en tiempo real. Esto podría afectar la capacidad del sistema para identificar las tendencias más recientes.

**Personalización profunda:** Si bien podemos personalizar las recomendaciones basándonos en las reseñas, puede que no podamos personalizarlas en función de las preferencias dietéticas individuales o las restricciones alimentarias de los usuarios por falta de datos.

**Escalabilidad:** Aunque el sistema está diseñado para escalar y cubrir otras regiones, la implementación inicial se limitará a California, Florida y Nueva York. La expansión geográfica podría estar fuera del alcance inicial del proyecto. Lo mismo vale para extrapolar el modelo a otros rubros comerciales o áreas afines.

 <!-- KPI section -->
## **📊 KPI´s:**

• **Tasa de crecimiento de reseñas:** para medir la rapidez con la que las reseñas de los usuarios están aumentando en las plataformas de Yelp y Google Maps.

$$
\mathrm{KPI}=\dfrac{R_{final} - R_{inicial}}{R_{inicial}}\cdot100
$$

<br>

• **Sentimiento promedio de las reseñas:** para evaluar la satisfacción general de los usuarios con los negocios analizados, se puede aplicar filtrando por rubro o categoría.

$$
\mathrm{KPI}=\dfrac{1}{n}\sum_{i=1}^{n} S_i
$$

*n = Cantidad de reseñas*<br>
*Si = Valor del sentimiento*

<br>

• **Precisión del modelo de recomendación:** para medir qué tan precisas son las recomendaciones que se ofrecen a los usuarios en función de sus experiencias previas.

$$
\mathrm{KPI}=\dfrac{R_{relevantes}}{Total}\cdot100
$$

<br>

<!-- metodología section -->
## **🔧 Metodología del Trabajo**

La metodología Scrum divide el trabajo en partes pequeñas y manejables llamadas "sprints". Cada sprint dura un período de tiempo corto, en este caso una semana, durante el cual el equipo se enfoca en completar un conjunto específico de tareas. Al final de cada sprint, se realizará una demo (sprint review meeting) en la que se hará una demostración de los entregables desarrollados, esperando una retroalimentación. Se ajusta así la planificación para el siguiente sprint según lo que se haya aprendido. Además, cada día se realizarán reuniones diarias de seguimiento (Daily Standup), para discutir el progreso diario y posibles inconvenientes. Todo esto permite una adaptación continua a medida que el equipo avanza.

![metodología scrum](https://robertotouza.com/wp-content/uploads/2023/07/Manual-Metodologia-Scrum-Roberto-Touza-3.png)

**Sprint 1 - Comprensión del Negocio y de los Datos**:

**Sprint 2 - Preparación de los Datos y Modelado**: 

**Sprint 3 - Evaluación y Despliegue**: 

<!-- stack section -->
## **💻 Stack Tecnológico**

**Visual Studio Code:** Software para trabajar de forma local en el proyecto.

- **Bases de datos:** Azure o PostgreSQL para almacenar los datos, MongoDB para datos no estructurados como reseñas de usuarios.

- **Lenguajes de programación:** Python para análisis de datos y desarrollo de modelos de machine learning.

- **Bibliotecas y frameworks:** pandas, scikit-learn, TensorFlow / PyTorch para machine learning, Flask o FastAPI para desarrollar APIs.

- **Herramientas de visualización:** Matplotlib, Seaborn, Plotly para visualización de datos.


<!-- team section -->
## **👥 Miembros del Equipo**

| Rol            |  Nombre              | LinkedIn | GitHub |
| -------------- |--------------------- | -------- |-|
| Data Engineer  | Nazareno Fantin      | [![LinkedIn][linkedin-shield]][linkedin-Naza]  | [![GitHub][github-shield]][github-Naza]  |
| Data Scientist | Sebastian Rosenblunn | [![LinkedIn][linkedin-shield]][linkedin-Sebas] | [![GitHub][github-shield]][github-Sebas] |
| Data Scientist | Alejo Diez Gomez     | [![LinkedIn][linkedin-shield]][linkedin-Alejo]   | [![GitHub][github-shield]][github-Alejo]   |
| Data Analyst   | Keyla Serna          | [![LinkedIn][linkedin-shield]][linkedin-Keyla] | [![GitHub][github-shield]][github-Keyla] |
| Data Analyst   | Tomás Basovich       | [![LinkedIn][linkedin-shield]][linkedin-Tom] | [![GitHub][github-shield]][github-Tom] |
<!-- | Project Management  | Scrum Master   |  |Maximiliano Vaca Coll |       ||-->

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[github-shield]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white

[linkedin-Naza]: https://www.linkedin.com/in/nazareno-fantin/
[linkedin-Sebas]:https://github.com/Nazario3482/Proyecto-Grupal-Google-yelp  
[linkedin-Alejo]:https://www.linkedin.com/in/alejo-gabriel-diez-gomez-402b93254/
[linkedin-Keyla]:www.linkedin.com/in/keyla-elyneth
[linkedin-Tom]:https://github.com/Nazario3482/Proyecto-Grupal-Google-

[github-Naza]: https://github.com/Nazario3482
[github-Sebas]:https://github.com/Nazario3482/Proyecto-Grupal-Google-yelp
[github-Alejo]:https://github.com/AlejoDiezGomez
[github-Keyla]:https://github.com/KeylaSernaB
[github-Tom]:https://github.com/Nazario3482/Proyecto-Grupal-Google-yelp
