CataldoProyect
===============

Proyecto desarrollado en Django como parte del curso de CODERHOUSE. Permite gestionar socios mediante un sistema CRUD (Crear, Leer, Actualizar, Eliminar).

GUÍA PARA LEVANTAR EL PROYECTO
-------------------------------

1. Clonar el repositorio

    git clone <url-del-repositorio>
    cd CataldoProyect

2. Crear y activar el entorno virtual

    # En Windows
    python -m venv .venv
    . .venv/Scripts/activate

    # En Linux/Mac
    python3 -m venv .venv
    source .venv/bin/activate

    Nota: Agregar `.venv/` al archivo `.gitignore`.

3. Instalar dependencias

    pip install -r requirements.txt

4. Crear y aplicar migraciones

    python manage.py makemigrations
    python manage.py migrate

5. Crear un superusuario

    python manage.py createsuperuser

    Elegí nombre de usuario, email y contraseña cuando se te solicite.

6. Levantar el servidor

    python manage.py runserver

7. Acceder a la app

    - http://localhost:8000     -> para ver la app
    - http://localhost:8000/admin -> para el panel de administración

ESTRUCTURA DEL PROYECTO
-------------------------

- CataldoProyect/      -> Configuración general del proyecto
- CataldoApp/          -> App principal con vistas, modelos, formularios, templates, etc.
- templates/           -> Carpeta general de templates
- static/              -> Archivos estáticos (CSS, JS, imágenes) (opcional)

REQUERIMIENTOS Y ACTUALIZACIONES
---------------------------------

Para actualizar el archivo de dependencias luego de instalar nuevos paquetes:

    pip freeze > requirements.txt

RECOMENDACIONES
----------------

- Usar entornos virtuales para mantener el entorno aislado.
- Registrar modelos en admin.py para facilitar la administración.
- Usar el patrón MVT separando bien vistas, modelos y templates.
- Documentar las rutas correctamente en urls.py y asegurarse de incluirlas.

