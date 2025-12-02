# 🖼️ Conversor Rápido de Imágenes

Una aplicación de escritorio moderna y sencilla construida con Python para convertir imágenes entre formatos comunes (PNG, JPEG) y crear iconos (ICO) rápidamente.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet)

## 📋 Descripción

Este proyecto es una herramienta gráfica (GUI) que permite a los usuarios seleccionar imágenes desde su ordenador y convertirlas a diferentes formatos con un solo clic. Utiliza **CustomTkinter** para una interfaz moderna y **Pillow (PIL)** para el procesamiento de imágenes.

## ✨ Características

* **Interfaz Moderna:** Diseño limpio y amigable (Modo sistema / Tema Azul).
* **Soporte de Formatos:**
    * PNG
    * JPEG (Manejo automático de transparencias RGBA -> RGB).
    * ICO (Redimensionamiento automático a 256x256 para compatibilidad).
* **Selección de Ruta:** El usuario puede elegir guardar el archivo nuevo en la misma carpeta o seleccionar un destino personalizado.
* **Validaciones:** Sistema de alertas para evitar errores si no se ha cargado una imagen.

## 🛠️ Tecnologías Utilizadas

* [Python](https://www.python.org/)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (UI)
* [Pillow](https://python-pillow.org/) (Procesamiento de imágenes)

## 🚀 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git](https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git)
    cd NOMBRE_DEL_REPO
    ```

2.  **Instala las dependencias:**
    Es recomendable usar un entorno virtual. Luego ejecuta:
    ```bash
    pip install customtkinter pillow
    ```

3.  **Ejecuta la aplicación:**
    ```bash
    python conversor.py
    ```
    u utiliza el .exe del repostorio

## 📸 Capturas de Pantalla

<img width="548" height="139" alt="image" src="https://github.com/user-attachments/assets/396014fd-02ef-4f79-a7b5-dc8b6b5f7956" />
<img width="603" height="532" alt="image" src="https://github.com/user-attachments/assets/dee3ea88-7467-44d2-9b7e-68e4d8cb619a" />



## 📄 Estructura del Código

El script principal `conversor.py` contiene:
* `ConversorApp`: La clase principal que hereda de `ctk.CTk`.
* Manejo de eventos para la carga de archivos y selección de carpetas.
* Lógica de conversión específica para cada formato (ej. redimensionado `LANCZOS` para iconos).

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la interfaz o añadir más formatos, siéntete libre de hacer un fork y enviar un pull request.

## 📝 Licencia

Este proyecto es de uso libre.
