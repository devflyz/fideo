#!/bin/bash

# Función para verificar si un paquete está instalado
package_installed() {
    dpkg -s "$1" &> /dev/null
}

# Función para instalar un paquete
install_package() {
    echo "Instalando $1..."
    sudo apt update
    sudo apt install -y $1
}

# Verificar si Python 3 y pip3 están instalados
if ! package_installed python3 || ! package_installed python3-pip; then
    install_package "python3 python3-pip"
fi

# Verificar si Java y JDK están instalados
if ! command -v javac &> /dev/null || ! command -v java &> /dev/null; then
    install_package "default-jdk"
fi

# Verificar si python3-requests está instalado
if ! package_installed python3-requests; then
    install_package "python3-requests"
fi

# Obtener la ruta actual
CURRENT_DIR=$(pwd)

# Ruta al archivo fideo.py
FIDEO_PY_PATH="$CURRENT_DIR/fideo.py"

# Comprobar si el archivo fideo.py existe
if [ ! -f "$FIDEO_PY_PATH" ]; then
    echo "El archivo fideo.py no existe en la ruta actual: $CURRENT_DIR"
    exit 1
fi

# Añadir alias a ~/.bashrc
echo "alias fideo='python3 $FIDEO_PY_PATH'" >> ~/.bashrc

# Agregar el alias a la sesión actual
source ~/.bashrc
