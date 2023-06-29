## Registro de la actividad física
Como se ha explicado anteriormente, en esta práctica los alumnos interactúan con las funciones para comprender la relación que hay entre estas, las gráficas y las realidades que representan. Para ello, se ha optado por las aplicaciones que registran la actividad física ya que es un recurso al que puede tener acceso cualquier alumno con un *smartphone* en la familia. También sería interesante hacer algo similar pero con aplicaciones biométricas, aunque generar y exportar este tipo de datos puede ser más difícil.

Para el caso del registro de la actividad mediante a la aplicación [Relive](https://www.relive.cc/), ésta te permite descargar el archivo `.gpx` donde vienen recogidos todos los datos necesarios para obtener las gráficas de nivel y de velocidad. El formato GPX es uno de las formas más extendidas de intercambio y almacenamiento de información georeferenciada. Los archivos con este formato pueden ser leídos e interpretados por multitud de programas ya que utilizan etiquetas XML, como `<time>`, `<trkpt>`, `<ele>`... Cuando un alumno abre la aplicación, le aparece la opción de registrar una nueva actividad, y después de activar el GPS de su móvil ya puede iniciar el registro de la misma (Figura 1). Al finalizar la actividad física, la aplicación nos deja guardarla con un nombre y descargar el archivo GPX resultante desde el área de usuario de su web.

![Utilización de la app Relive para registrar una actividad física.](/app2.jpeg)
![Utilización de la app Relive para registrar una actividad física.](/app3.jpeg)
![Utilización de la app Relive para registrar una actividad física.](/app4.jpeg)
![Utilización de la app Relive para registrar una actividad física.](/app5.jpeg)

Cada alumno deberá mandar al profesor su archivo GPX para que pueda transformarlo en dos gráficas: una de elevaciones y otra de velocidad. Para ello se ha diseñado un programa para hacer esto automáticamente (Apéndice A).

El programa lee todos los archivos `.gpx` de una carpeta dada y extrae los tiempos, latitudes, longitudes y altitudes de cada registro mediante expresiones regulares. A partir de las latitudes y longitudes, se calculan las distancias recorridas utilizando la fórmula

Δ(x1,x2) = R * 2 * arctan(sqrt((1-a)/a))


siendo

a = sin(Δlat/2)^2 + cos(lat1) * cos(lat2) * sin(Δlon/2)^2
Δlat = lat2 - lat1 (en radianes)
Δlon = lon2 - lon1 (en radianes)


y R el radio de la tierra en kilómetros.

Con las distancias entre cada par de registros sucesivos y los tiempos de éstos podemos calcular la velocidad. Para evitar una excesiva variabilidad en ésta se exporta la velocidad después de haber aplicado una media móvil. Esto es:

v̄i = (1 / (w + 1)) * ∑(vj) para i = 1, ..., n-w


Siendo v el vector de velocidades original, n su longitud, v̄ el resultado de la transformación y w el tamaño elegido para hacer la media (1 ≤ w ≤ n). Esta transformación es necesaria ya que la baja precisión del GPS hace que los registros tengan mucho ruido haciéndose especialmente molesto en el caso de la velocidad (Figura 2).

![Velocidad registrada por el GPS (en gris) y media móvil de ésta (en azul), con w=60.](media_movil.png)

Para el gráfico de alturas no es necesario hacer ningún tipo de transformación.

Ambas gráficas son representadas con el paquete `matplotlib` y exportadas en formato `.pdf` con el mismo nombre que tenía el archivo `.gpx`.
