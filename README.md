Este trabajo práctico fue desarrollado utilizando Jupyter Notebook. Para poder ejecutarlo correctamente, hay que seguir los siguientes pasos:

Primero, asegurarse de tener instalado Python en tu sistema (al menos la versión 3.8) y pip, que es el gestor de paquetes de Python. Para verificarlo, se puede abrir una terminal o consola y ejecutar los comandos python --version y pip --version.

Después de hacer esa verificación, hay que instalar las dependencias del proyecto. Si el repositorio incluye un archivo llamado requirements.txt, se debe abrir una terminal, ubicarse en la carpeta donde está el archivo y ejecutar el comando pip install -r requirements.txt

Si ese archivo no existe, se pueden instalar las librerías necesarias de manera individual utilizando el comando pip install nombre_paquete.

Después, para ejecutar el archivo Jupyter Notebook, que tiene la extensión .ipynb, se debe iniciar el servidor de Jupyter con el siguiente comando: jupyter notebook
Lo que hace este comando es abrir una nueva pestaña en el navegador con la interfaz de Jupyter. Desde ahí se va a poder navegar hasta el archivo .ipynb y abrirlo. Para ejecutar cada celda del notebook, hay que hacer clic sobre la celda y presionar Shift + Enter.

Como otra opción, si no se quiere instalar nada en la computadora, se puede utilizar Google Colab, que es una plataforma gratuita de Google para trabajar con notebooks directamente desde el navegador. Para eso, se ingresa a esta página https://colab.research.google.com, presionar la pestaña "Subir" y cargar el archivo .ipynb. Una vez abierto, se pueden ejecutar las celdas de la misma manera: seleccionándolas y presionando Shift + Enter.

En caso de que el notebook utilice archivos adicionales como imágenes, datos u otros recursos, es importante colocarlos en la misma carpeta del proyecto o ajustar las rutas dentro del código para que se encuentren correctamente. También, si durante la ejecución aparece un error indicando que falta una librería, se puede instalar con el comando pip install nombre_paquete.