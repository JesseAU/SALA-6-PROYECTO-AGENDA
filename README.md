
<<<<<<< HEAD
=======
# 1️⃣ Crear carpeta y moverse a ella
mkdir agenda
cd agenda
=======

>>>>>>> 41630bff711b74f429ccf4afba3bf738d6cb2c15
# 📅 Agenda de Tareas Personales (Python + Tkinter)


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

<<<<<<< HEAD
📁 agenda-tareas/  
- `gui.py` → Interfaz gráfica (Frontend)  
- `logic.py` → Lógica y manejo de datos (Backend)  
- `tareas.json` → Archivo donde se guardan las tareas  
- `README.md` → Este archivo  
=======
# 7️⃣ Crear superusuario
# Usuario: Yamir
# Email: kitikazis@gmail.com
# Contraseña: 1234
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('Yamir','kitikazis@gmail.com','1234')"
>>>>>>> 41630bff711b74f429ccf4afba3bf738d6cb2c15

# 8️⃣ Levantar servidor de desarrollo
python manage.py runserver
=======
📁 agenda-tareas/  
- `gui.py` → Interfaz gráfica (Frontend)  
- `logic.py` → Lógica y manejo de datos (Backend)  
- `tareas.json` → Archivo donde se guardan las tareas  
- `README.md` → Este archivo  



✅ Próximos pasos

Abrir navegador:

CRUD principal: http://127.0.0.1:8000/

Admin Django: http://127.0.0.1:8000/admin


Yamir-1234
Crear tus modelos, formularios y plantillas como te mostré antes para el CRUD con Bootstrap y calendario.
=======
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/agenda-tareas.git
   cd agenda-tareas
   python gui.py

# SALA-6-PROYECTO-AGENDA

## 🧪 Proyecto: Agenda de tareas 
---
## 🎯 Objetico del sprint (Sprint goal)

**Crear una aplicación de escritorio sencilla en Python que permita gestionar una agenda personal de tareas (Crear, Leer, Actualizar, Eliminar) con interfaz gráfica y almacenamiento persistente.** 

---

## 👥 ROLES DEL EQUIPO



|  Rol           | Nombre del integrante  | 
|---------------|------------------------|
| Scrum Master  | Zaid uriarte           | 
| Product Owner | Daniel Torres           | 
| Developer 1   | Yamir Huallcca      | 
| Developer 2   | Kevin Yupanqui          |         |
| Developer 3   | Juan Soiis      |  
| Developer 4  | Rossy Quispe         |                  | 


---
## HISTORIA DE USUARIO

**HU-1 Como usuario, quiero añadir una nueva tarea con título, descripción y fecha límite, para organizar mis pendientes**

**Criterio de aceptacion**

**HU-2 Como usuario, quiero ver todas mis tareas en una lista con su estado, para llevar control de mis pendientes.**

**criterio de aceptacion**

**HU-3 Como usuario, quiero que las tareas se guarden incluso si cierro el programa, para no perder información.**

**Criterio de aceptacion**

**HU-4 Como usuario, quiero editar una tarea existente, para corregir o actualizar su información.**

**Criterio de aceptacion**

**HU-5 Como usuario, quiero eliminar una tarea, para quitarla de la agenda cuando ya no sea necesaria.**

**Criterio de Aceptacion**

**HU-6 Como usuario, quiero una interfaz gráfica amigable, para que sea fácil de usar.**

**Criterio de aceptacion**

**HU-7 Como desarrollador, quiero poder visualizar todo el programa terminado fusionado en la rama principal para su despliegue**

**Criterio de aceptacionn**

**HU-8 Como Scrum Master, debo visualizar el avance de cada desarrollador en su rama asignada para poder controlar el desarollo y realizar pruebas**

**Criterio de aceptacion**

## HERRAMIENTAS USADAS.




