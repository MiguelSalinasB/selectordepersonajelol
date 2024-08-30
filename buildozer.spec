[app]
# Nombre de la aplicación
title = League of Legends Champion Selector

# Paquete de la aplicación (debe ser único en la Play Store/App Store)
package.name = lol_champion_selector
package.domain = org.example

# Versión de la aplicación
version = 1.0

# Versión de la aplicación en la Play Store/App Store
version.code = 1

# Título de la aplicación en la pantalla de inicio
name = LeagueOfLegends

# Arquitecturas soportadas (ARM, x86, etc.)
# Puede ser necesario ajustar según el dispositivo de destino
android.arch = armeabi-v7a arm64-v8a x86 x86_64

# Plataforma (android o ios)
platforms = android, ios

# Inclusión de archivos de la aplicación
source.include_exts = py,png,jpg,kv,atlas,json

# Paquetes adicionales para el entorno de ejecución
requirements = python3,kivy,sqlite3

# Configuración de icono
icon.filename = %(source.dir)s/assets/images/icon.png

# Configuración de permisos
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Configuración para iOS (solo para iOS)
ios.kivy_version = 2.0.0
ios.bundle_id = org.example.lol_champion_selector

# Configuración de versión de Kivy (ajustar si es necesario)
kivy_version = 2.0.0

# Reglas para la construcción de APK
android.gradle_dependencies = 
    implementation 'androidx.appcompat:appcompat:1.3.1'
    implementation 'androidx.core:core:1.6.0'

# Configuración de compilación
# La mayoría de estos valores pueden quedarse como están
[buildozer]
# Las siguientes configuraciones afectan el comportamiento de la construcción
# Pueden ser modificadas según sea necesario
clean = 1
release = 0
log_level = 2

# Configuración para la construcción de la aplicación
# Puedes ajustar el tiempo de construcción y el número de hilos
build_number = 1
build_on_release = 0

# Configuración de la ruta de salida
output_dir = bin

# Otros parámetros opcionales
# Añade cualquier otra configuración específica para tu proyecto aquí
