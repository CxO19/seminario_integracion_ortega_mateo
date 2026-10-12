# Seminario de Integración: FastAPI y Angular

Bienvenido al repositorio oficial de la materia **Seminario de Integración**. Este espacio está diseñado para consolidar los conocimientos de programación avanzada, integrando un backend moderno de alto rendimiento con un framework robusto de frontend para el desarrollo de aplicaciones web full-stack.

---

## 🚀 Tecnologías del Curso

### 1. Repaso de Python
Python es un lenguaje de programación de alto nivel, interpretado y multiparadigma, conocido por su sintaxis limpia y su legibilidad. En este seminario utilizaremos características avanzadas del lenguaje esenciales para el desarrollo web moderno:
* **Tipado estático opcional (`typing`):** Uso de anotaciones de tipos para mejorar la mantenibilidad y la documentación del código.
* **Programación Asíncrona (`async/await`):** Manejo de operaciones concurrentes de E/S de manera eficiente.
* **Gestión de Entornos Modernos (`uv`):** Utilización de herramientas de gestión de paquetes y entornos virtuales ultrarrápidas.

### 2. FastAPI (Backend)
**FastAPI** es un framework web moderno y de alto rendimiento para construir APIs con Python, basado en las anotaciones de tipos estándar del lenguaje.
* **Alto Rendimiento:** Está a la par de NodeJS y Go gracias a Starlette (para la parte web) y Pydantic (para la gestión de datos).
* **Validación Automática:** Valida los datos de entrada y salida automáticamente utilizando esquemas de Pydantic, reduciendo errores de código.
* **Documentación Interactiva:** Genera automáticamente documentación interactiva basada en estándares OpenAPI (Swagger UI y ReDoc) accesible de forma nativa.

### 3. Angular (Frontend)
**Angular** es una plataforma y framework de desarrollo de aplicaciones web de una sola página (SPA) basado en TypeScript, desarrollado y respaldado por Google.
* **Arquitectura Basada en Componentes:** Facilita la reutilización de código, la modularidad y el mantenimiento de interfaces de usuario escalables.
* **Inyección de Dependencias:** Un sistema integrado que promueve código desacoplado, modular y altamente testeable.
* **Tipado Robusto con TypeScript:** Permite detectar errores en tiempo de desarrollo gracias a su fuerte tipado estático y características orientadas a objetos.

---

## 📂 Estructura del Repositorio

El repositorio está organizado en subproyectos para mantener separados el backend y el frontend:

```text
/
├── backend/          # API desarrollada con FastAPI y gestionada con uv
│   ├── .venv/        # Entorno virtual de Python
│   ├── app/          # Lógica de la API, modelos y rutas
│   └── main.py       # Punto de entrada de la aplicación
│
├── frontend/         # Aplicación de interfaz de usuario con Angular
│   ├── src/          # Código fuente, componentes y servicios
│   └── angular.json  # Configuración del proyecto Angular
│
└── README.md         # Documentación general de la materia