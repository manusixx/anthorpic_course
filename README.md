# 🤖 Building with the Claude API
> Ejercicios prácticos del curso **Building with the Claude API** de Anthropic Academy  
> Autor: **Manuel Alejandro Pastrana Pardo** — Profesor Investigador, Universidad del Valle

---

## 📋 Descripción

Repositorio de aprendizaje que documenta los ejercicios del curso oficial de Anthropic para construir aplicaciones con la API de Claude. Cada módulo corresponde a una unidad del curso e incluye ejemplos funcionales en Python usando Jupyter Notebooks.

---

## 🗂️ Estructura del repositorio

```
anthorpic_course/
├── 001_requests/          # Primeras llamadas a la API
├── 002_system_promt/      # System prompts y control de comportamiento
├── 003_Temperature/       # Control de temperatura y aleatoriedad
├── 004_streaming/         # Respuestas en streaming
├── .gitignore             # Archivos excluidos del repositorio
└── README.md              # Este archivo
```

---

## 🧩 Módulos

### 001 — Requests
Introducción a la API de Claude. Cubre la autenticación, creación del cliente, envío de mensajes y manejo del historial de conversación para mantener contexto entre turnos.

**Conceptos clave:** `client.messages.create`, roles `user`/`assistant`, historial de mensajes, variables de entorno.

### 002 — System Prompt
Control del comportamiento del modelo mediante system prompts. Incluye técnicas de prefill para controlar el formato de salida y uso de `stop_sequences`.

**Conceptos clave:** `system prompt`, `prefill`, `stop_sequences`, control de formato de salida.

### 003 — Temperature
Control del parámetro de temperatura para ajustar la aleatoriedad y creatividad de las respuestas del modelo según el caso de uso.

**Conceptos clave:** `temperature`, determinismo, creatividad, casos de uso por nivel de temperatura.

### 004 — Streaming
Implementación de respuestas en tiempo real usando streaming, mejorando la experiencia del usuario en aplicaciones conversacionales.

**Conceptos clave:** `stream=True`, manejo de eventos, respuestas incrementales.

---

## ⚙️ Configuración del entorno

### Requisitos
- Python 3.10+
- VS Code con extensión Jupyter
- Cuenta en [Anthropic Console](https://console.anthropic.com)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/manusixx/anthorpic_course.git
cd anthorpic_course

# Instalar dependencias
pip install anthropic python-dotenv
```

### Variables de entorno

Cree un archivo `.env` en la carpeta del módulo que desea ejecutar:

```
ANTHROPIC_API_KEY=su_api_key_aqui
```

> ⚠️ **Nunca comparta su API Key ni la incluya directamente en el código.** El archivo `.env` está incluido en `.gitignore` para evitar exposición accidental.

---

## 🌿 Estrategia de ramas

| Rama | Propósito |
|------|-----------|
| `main` | Versión estable y revisada — solo por Pull Request |
| `develop` | Integración continua — solo por Pull Request |
| `mpastrana` | Rama de desarrollo activo |

---

## 📚 Recursos

- [Anthropic Academy](https://anthropic.skilljar.com/)
- [Documentación oficial de la API](https://docs.anthropic.com)
- [Anthropic Console](https://console.anthropic.com)

---

## 📄 Licencia

Este repositorio es de uso educativo y personal. Los ejercicios están basados en el material oficial del curso de Anthropic.