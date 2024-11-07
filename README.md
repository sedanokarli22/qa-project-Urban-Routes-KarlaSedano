# PROYECTO DEL SPRINT 8 "URBAN ROUTES"
## SEDANO SANCHEZ KARLA GUADALUPE 
### COHORT 14.

## DESCRIPCION DEL PROYECTO
El proyecto se realizo a partir de la implementacion de Selenium Webdriver, como herramienta para automatizar pruebas para la aplicación de viajes "Urban Routes", que permitio controlar el navegador simulando la interacción del usuario con la aplicación.

## DOCUMENTACIÓN 
- URL DEL SERVIRDOR URBAN ROUTES. 
- DEVTOOLS
- LISTA DE COMPROBACIÓN

## TECNOLOGIAS UTILIZADAS
- PYTHON

- PYCHARM


- PYTEST:

Para la ejecución de las pruebas.

Instalación de Pytest
- Abre PyCharm o una terminal (como Git Bash o el CMD de Windows).
- Verifica que Python esté instalado ejecutando python --version.
- Instala pytest ejecutando el siguiente comando en la terminal o consola de PyCharm: pip install pytest.
- Verifica la instalación ejecutando: pytest --version


- SELENIUM WEBDRIVER:

Instalación de Selenium WebDriver:

Para trabajar con Selenium WebDriver, necesitas conectarlo con tu IDE.

- Instala el controlador del navegador
- Acceder al sitio oficial de Selenium donde se encuentran los drivers
- Selecciona la versión del controlador que coincida con tu versión de navegador.
- Hay varios archivos comprimidos en la carpeta. Descarga el que coincida con tu sistema operativo.
Descomprime el archivo. Crea una carpeta llamada WebDriver/bin y guarda el archivo allí.
- Agrega la ruta a bin a la variable de entorno PATH. El algoritmo depende del sistema operativo.
- Instala Selenium para Python
- Abrir la Consola o Terminal Terminal desde las aplicaciones o usando el buscador de aplicaciones.
- Ejecutar el Comando de Instalación
- Escribe el siguiente comando para instalar el paquete de Selenium: pip install selenium
- Abre el navegador con PyCharm
- Importa el paquete Selenium WebDriver: from selenium import webdriver
- Importa el paquete time: import time
- Activa el controlador del navegador. 


## EJECUCION DE LAS PRUEBAS 
* Para ejecutar las pruebas, asegúrate de tener instalados los paquetes pytest y Selenium. 
   - pip install pytest
   - pip install selenium
* Las pruebas utilizarán el navegador Chrome, así que asegúrate de tenerlo instalado.
  (Puedes ajustar las configuraciones del navegador en el método setup_class de la clase TestUrbanRoutes.)
* Para ejecutar las Pruebas Asegúrate de estar en el directorio "main.py", donde se encuentran las pruebas.
Luego, ejecuta las pruebas utilizando pytest
* Al finalizar las pruebas, pytest mostrará un resumen de los resultados en la terminal.

## FUNCIONALIDAD DE LAS PRUEBAS
Las pruebas automatizadas cubren los siguientes pasos del flujo de solicitud de un taxi:

1. Configurar la dirección.
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito: Se simula la interacción con el modal de "Agregar una tarjeta" y se asegura que el 
campo CVV (id="code" class="card-input") pierda el enfoque para habilitar el botón de enlace.
5. Escribir un mensaje para el conductor.
6. Solicitar una manta y pañuelos.
7. Pedir 2 helados.
8. Esperar la búsqueda de un taxi: Se asegura que el modal de búsqueda de conductor aparezca correctamente y que la 
cuenta regresiva se inicie.

