# Generador de Contenido para Redes Sociales usando Ollama
## Descripción General

Este proyecto implementa una herramienta de generación automática de publicaciones para Twitter, LinkedIn y blogs personales, a partir de un tema o artículo proporcionado por el usuario. Mediante un prompt adaptado, el modelo devuelve textos con el tono y formato adecuados para cada red social.

La solución fue desarrollada en Python, utilizando LangChain y el framework Ollama, que permite la ejecución local de modelos de lenguaje de gran escala (LLM). Con ello, se busca demostrar conocimientos en integración de IA, despliegue de modelos open-source y adaptación de herramientas a recursos limitados (CPU/RAM).

Este proyecto forma parte de mi portafolio personal, con el objetivo de evidenciar aprendizajes técnicos, experiencia práctica e interacción con modelos de IA en entornos reales de desarrollo.

## Tecnologías y Herramientas

**Lenguaje:** Python

**Entorno:** Visual Studio Code

**Frameworks/Modelos:** LangChain + Ollama (GPT-3.5/4 y LLM open-source: LLaMA 2, Mistral, Falcon, entre otros)

##cAprendizajes Clave

LLM con LangChain: Integración de modelos GPT-3.5/4 y alternativos open-source vía Hugging Face.

Ollama: Herramienta open-source que facilita la ejecución local de LLM, gestionando pesos, configuraciones y datasets en un paquete unificado (Modelfile).

Optimización de recursos: Selección de modelos adecuados según la memoria RAM disponible y configuración de prompts personalizados para distintos casos de uso.

## Objetivos del Proyecto

* Generar publicaciones para redes sociales con distintos estilos y longitudes.

* Implementar comunicación local con modelos a través de prompts prediseñados.

* Explorar configuraciones flexibles de LLM y evaluar su rendimiento en un entorno de escritorio.

## Referencias

LangChain Ollama [https://python.langchain.com/api_reference/ollama/llms/langchain_ollama.llms.OllamaLLM.html]