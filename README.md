# Micro-resta

Código Python (resta.py)
Este código es un microservicio que realiza la operación de resta utilizando Flask:

### Importaciones:

- Flask para crear la aplicación web.
- jsonify para formatear las respuestas JSON.
- request para acceder a los datos de la solicitud.
- CORS para permitir solicitudes de recursos cruzados (Cross-Origin Resource Sharing).

### Inicialización de la Aplicación:

Se crea una instancia de Flask llamada app.
Se habilita CORS en la aplicación para permitir solicitudes desde cualquier origen.
Ruta /api/resta:

Define una ruta en /api/resta que solo acepta solicitudes POST.
Extrae dos números (n1 y n2) del cuerpo de la solicitud JSON.
Realiza la operación de resta y devuelve el resultado como una cadena.
Ejecución de la Aplicación:

La aplicación se configura para ejecutarse en host='0.0.0.0' y port='4040'.

---

### Dockerfile
Este Dockerfile se utiliza para crear una imagen Docker del microservicio de resta:

. FROM python:3.6: Utiliza Python 3.6 como imagen base.
- EXPOSE 4040: Indica que el contenedor expondrá el puerto 4040, donde la aplicación Flask estará escuchando.
- WORKDIR /app: Establece el directorio de trabajo dentro del contenedor en /app.
- COPY requirements.txt /app: Copia el archivo requirements.txt al directorio de trabajo del contenedor.
- RUN pip install -r requirements.txt: Instala las dependencias de Python listadas en requirements.txt.
- COPY resta.py /app: Copia el archivo resta.py al directorio de trabajo del contenedor.
- CMD python resta.py: Define el comando por defecto para ejecutar el archivo resta.py.

