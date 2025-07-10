# Examen_Final
Cibertec Api_Developer /
Felix Fernandez Gonzales


# Desarrollo 

1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar brevemente
    
    Python es una de las herramientas más versátiles y potentes en el trabajo con datos, por su simplicidad, comunidad activa y variedad de librerías. Aquí cinco usos:

    1. Exploración y análisis de datos: Permite entender grandes volúmenes de información a través de gráficos, resúmenes estadísticos y análisis exploratorio.

    2. Modelado predictivo (Machine Learning): Se utiliza para entrenar modelos que identifican patrones y hacen predicciones, muy útil en áreas como finanzas, salud o marketing.

    3. Procesamiento de datos masivos (Big Data): Python puede integrarse con plataformas como Apache Spark para manejar datos que no caben en memoria.

    4. Obtención automática de datos (Web Scraping): Ideal para recolectar información de páginas web de forma automatizada, por ejemplo, precios, noticias o datos de mercado.

    5. Generación automatizada de reportes: Facilita la creación de informes y visualizaciones dinámicas que se actualizan sin intervención manual, ahorrando tiempo en tareas repetitivas.

2. ¿Cómo se diferencian Flask de Django? Argumentar.

    Flask y Django son dos frameworks de Python para desarrollo web, pero tienen enfoques muy distintos.

    Django es un framework completo, tipo “todo en uno”. Viene con muchas funcionalidades integradas, como autenticación de usuarios, panel de administración, ORM (para trabajar con bases de datos) y estructuras definidas. Esto lo hace ideal para proyectos grandes o cuando se quiere desarrollar rápido con una arquitectura clara desde el inicio.

    Por otro lado, Flask es un microframework: más liviano, flexible y minimalista. No impone una estructura fija y te da libertad para decidir qué librerías usar. Esto lo hace perfecto para proyectos pequeños, APIs o cuando el desarrollador necesita más control sobre cada componente.

    En mi opinión, la elección depende del tipo de proyecto y del nivel de personalización que se necesite. Si quiero rapidez y estructura, uso Django. Pero si busco construir algo a medida o solo una API sencilla, prefiero Flask.

3. ¿Qué es un API? Explicar en sus propias palabras

    Un API es como un mensajero entre programas. Imagina que tienes dos aplicaciones diferentes que necesitan trabajar juntas, pero no se entienden directamente. El API es ese “traductor” que les permite comunicarse de forma clara y segura.

    Por ejemplo, cuando usamos una app para pedir un taxi, esa app se conecta con Google Maps para mostrarte dónde estás. No necesita saber cómo está hecho Google Maps por dentro, solo hace una “pregunta” a través del API, y Google le responde con los datos necesarios.

    En otras palabras, un API es una forma ordenada de pedir y recibir información entre sistemas, sin complicarse con los detalles internos. Nos permite ahorrar tiempo, integrar servicios fácilmente y construir aplicaciones más útiles.

4. ¿Cuál es la principal diferencia entre REST y WebSockets?

    La diferencia principal está en cómo se comunican con el servidor.

    REST funciona como una conversación puntual: el cliente hace una petición y el servidor responde. Y ahí termina todo, hasta que el cliente vuelva a preguntar otra vez. Es ideal para cosas que no cambian todo el tiempo, como consultar datos o enviar formularios.

    En cambio, WebSockets es una comunicación en tiempo real. Es como abrir una llamada entre el cliente y el servidor, y ambos pueden hablar cuando quieran sin tener que colgar y volver a llamar. Esto es perfecto para chats, juegos en línea o notificaciones en vivo, donde los datos cambian constantemente.


5. Describir un ejemplo de API comercial y como funciona – usar otros ejemplos no vistos en el curso.

    Un API comercial que me parece interesante es el de Spotify. Esta API permite que otras aplicaciones accedan a su base de datos musical. Por ejemplo, si yo estoy desarrollando una app para hacer rutinas de ejercicio, puedo integrar el API de Spotify para que mis usuarios escuchen una playlist directamente desde mi app, sin necesidad de abrir Spotify por separado.

    ¿Cómo funciona? 
    Mi app le pide a Spotify algo específico, como “muéstrame las canciones del usuario” o “reproduce esta lista”. Spotify responde con la información solicitada, todo a través de peticiones web muy estructuradas.
    La ventaja es que yo no tengo que manejar archivos de música ni crear un reproductor desde cero. Solo uso las funciones que Spotify ya ofrece.

    Este tipo de APIs comerciales facilita mucho el trabajo, porque me permiten conectar mi app con servicios grandes, de forma segura, rápida y profesional.
