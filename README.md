# Autocheck 🚀

¡Bienvenido a Autocheck! Una herramienta de línea de comandos diseñada para simplificar la evaluación y revisión de archivos Java. Con Autocheck, puedes compilar archivos Java, ejecutar casos de prueba automáticamente y obtener retroalimentación instantánea sobre su funcionamiento.

## Características ✨

- **Compilación Automática:** Compila automáticamente archivos Java para garantizar que estén libres de errores.
- **Ejecución de Casos de Prueba:** Ejecuta casos de prueba automáticamente y compara las salidas generadas con las salidas esperadas.
- **Modo Examen:** Genera ejercicios aleatorios a partir de una lista conocida y evalúa las soluciones automáticamente.
- **Estado de Ejercicios:** Verifica el estado de los ejercicios, mostrando cuáles están en la carpeta donde se ejecuta el programa y cuáles no.

## Uso 🛠️

```bash
fideo [--help | --version | --download-checks | --exercise-status | --yt | --exam-mode]
```

- `--help | -h`: Muestra información de ayuda.
- `--version | -v`: Muestra la versión del programa.
- `--download-checks | -c`: Descarga los checks necesarios localmente para su uso offline. (Aún no disponible)
- `--exercise-status | -s`: Muestra el estado de los ejercicios. (Aún no disponible)
- `--yt | -y`: Abre el canal de YouTube de Flyz.
- `--exam-mode | -t`: Activa el modo examen. (Aún no disponible)
- `--descs <nombre_ejercicio> | -d <nombre_ejercicio>`: Muestra la descripción de un ejercicio específico.
- `--list | -l`: Muestra una lista de archivos .java conocidos.
 

## Requisitos 📋

- Python 3.x
- **Conexión a Internet para descargar los checks y los casos de prueba.**

## Versiones 🔄

| Versión | Fecha     |
|---------|-----------|
| 1.0.1   | 2023-05-04|
| 1.0.2   | 2023-05-05|
| 1.0.3   | 2024-05-06|
| 1.0.4   | 2024-05-07|

Autocheck simplifica el proceso de evaluación de archivos Java, proporcionando una forma eficiente de compilar, ejecutar pruebas y obtener retroalimentación rápida. ¡Espero que encuentres útil esta herramienta!


## Contribuciones y Problemas

¡Si encuentras algún problema o quieres contribuir con mejoras, no dudes en abrir un issue o enviar un pull request en el repositorio de GitHub!

## Creado por 🌟
Autocheck es una creación de [Devflyz](https://github.com/devflyz).


Aquí está el README mejorado con la información proporcionada:

---

# Autocheck

Autocheck es una herramienta de línea de comandos diseñada para facilitar la evaluación y revisión de archivos Java. Con Autocheck, puedes compilar archivos Java, ejecutar casos de prueba automáticamente y obtener retroalimentación sobre su funcionamiento.

## Características

- **Compilación Automática:** Compila automáticamente archivos Java para asegurar que estén libres de errores.
- **Ejecución de Casos de Prueba:** Ejecuta casos de prueba automáticamente y compara las salidas generadas con las salidas esperadas.
- **Modo Examen:** Genera ejercicios aleatorios a partir de una lista conocida y evalúa las soluciones automáticamente.
- **Estado de Ejercicios:** Verifica el estado de los ejercicios, mostrando cuáles están en la carpeta donde se ejecuta el programa y cuáles no.

## Uso

Para instalar Autocheck, ejecuta el siguiente script en tu terminal:

```bash
chmod +x install.sh
./install.sh
```

Este script verificará si tienes instalados los requisitos necesarios, como Python 3, pip3 y Java Development Kit (JDK). Si falta alguno de estos requisitos, el script los instalará automáticamente.

Una vez instalado, puedes ejecutar Autocheck con el comando `fideo`.
