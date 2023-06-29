## Registro de la actividad física
Como se ha explicado anteriormente, en esta práctica los alumnos interactúan con las funciones para comprender la relación que hay entre estas, las gráficas y las realidades que representan. Para ello, se ha optado por las aplicaciones que registran la actividad física ya que es un recurso al que puede tener acceso cualquier alumno con un *smartphone* en la familia. También sería interesante hacer algo similar pero con aplicaciones biométricas, aunque generar y exportar este tipo de datos puede ser más difícil.

Para el caso del registro de la actividad mediante a la aplicación [Relive](https://www.relive.cc/), ésta te permite descargar el archivo `.gpx` donde vienen recogidos todos los datos necesarios para obtener las gráficas de nivel y de velocidad. El formato GPX es uno de las formas más extendidas de intercambio y almacenamiento de información georeferenciada. Los archivos con este formato pueden ser leídos e interpretados por multitud de programas ya que utilizan etiquetas XML, como `<time>`, `<trkpt>`, `<ele>`... Cuando un alumno abre la aplicación, le aparece la opción de registrar una nueva actividad, y después de activar el GPS de su móvil ya puede iniciar el registro de la misma (Figura 1). Al finalizar la actividad física, la aplicación nos deja guardarla con un nombre y descargar el archivo GPX resultante desde el área de usuario de su web.
![Descripción de la imagen](/images/picture.jpg)
![Utilización de la app Relive para registrar una actividad física.](/home/adan/Desktop/Master Prof UNED/2o Q/TFM/Redaccion/img/app2.jpeg)
![Utilización de la app Relive para registrar una actividad física.](img/app3.jpeg)
![Utilización de la app Relive para registrar una actividad física.](img/app4.jpeg)
![Utilización de la app Relive para registrar una actividad física.](img/app5.jpeg)

Cada alumno deberá mandar al profesor su archivo GPX para que pueda transformarlo en dos gráficas: una de elevaciones y otra de velocidad. Para ello se ha diseñado un programa para hacer esto automáticamente (Apéndice A).

El programa lee todos los archivos `.gpx` de una carpeta dada y extrae los tiempos, latitudes, longitudes y altitudes de cada registro mediante expresiones regulares. A partir de las latitudes y longitudes, se calculan las distancias recorridas utilizando la fórmula

