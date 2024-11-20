
# Proyecto: Simulador de Comandos SQL con Árbol B+

Este proyecto implementa un editor de texto muy básico que permite hacer operaciones de 
creacion, apertura y guardado de archivos. 

## Estructura del Proyecto

El proyecto se divide en los siguientes archivos:

- `main.py`: Implementa la clase ventana y abre la ventana del editor.
- `ventana.py` Implementa todas las operaciones necesarias para el editor, exceptuando la encriptación.
- `criptografia.py`: Implementa las funciones que permiten encriptar y desencriptar.
- `rc_Recursos.py`: Contiene los datos de los iconos del editor.
- `ui_form.py`: Contiene todos los elementos de la interfaz grafica.
## Compilación y Ejecución

1. Para compilar el proyecto, ubiquese en la carpeta donde descargó el proyecto y ejecute el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

2. Para ejecutar el programa, usa:

    ```bash
    py main.py (para Windows)
    ```

    ```bash
    python3 main.py (para Linux)
    ```

4. Para salir del programa, presione el boton que le permite salir.

## Requisitos

- Python version 3 o superior.
- Instalar las librerias necesarias para ejecutar el editor.
- Guardar los archivos con la extension .eda2 para que sean reconocidos por el editor, esto debe hacerlo en Linux, donde el archivo no obtiene extension automaticamente.
- Actualizar su sistema a la última versión (Especialmente en equipos linux, donde los repositorios no están actualizados con las versiones de las librerias más recientes).

## Agradecimientos

Este proyecto va dedicado a nuestro amigo Brayan Gonzalez quien tuvo que retirarse de la institución por problemas médicos.

## Autores

- Maria Acevedo Suárez
- Juan Pablo Avendaño Bustamante