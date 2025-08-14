# 1️⃣ Crear carpeta y moverse a ella
mkdir agenda
cd agenda

# 2️⃣ Crear entorno virtual (opcional pero recomendado)
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
# source venv/bin/activate

# 3️⃣ Instalar Django
pip install django

# 4️⃣ Crear proyecto Django en la carpeta actual
django-admin startproject agenda .

# 5️⃣ Crear app 'tareas'
python manage.py startapp tareas

# 6️⃣ Aplicar migraciones iniciales
python manage.py migrate

# 7️⃣ Crear superusuario
# Usuario: Yamir
# Email: kitikazis@gmail.com
# Contraseña: 1234
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('Yamir','kitikazis@gmail.com','1234')"

# 8️⃣ Levantar servidor de desarrollo
python manage.py runserver


✅ Próximos pasos

Abrir navegador:

CRUD principal: http://127.0.0.1:8000/

Admin Django: http://127.0.0.1:8000/admin

Yamir-1234
Crear tus modelos, formularios y plantillas como te mostré antes para el CRUD con Bootstrap y calendario.
