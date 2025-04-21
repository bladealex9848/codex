# Instalación y Uso de Codex

Este repositorio contiene ejemplos y documentación sobre cómo instalar y usar Codex, una herramienta de línea de comandos para interactuar con modelos de OpenAI.

## Requisitos

- Python 3.13.3
- Node.js v22.14.0 o superior

## Instalación

Codex se ha instalado globalmente en el sistema usando:

```bash
sudo npm install -g @openai/codex
```

## Configuración

Se ha configurado Codex para usar el modelo 'gpt-4.1-nano' por defecto. La configuración se encuentra en:

```
~/.codex/config.yaml
```

También se han añadido instrucciones personalizadas en:

```
~/.codex/instructions.md
```

## Ejemplos

Este repositorio contiene los siguientes ejemplos:

1. **ejemplo-simple**: Un ejemplo básico que utiliza el modelo predeterminado 'gpt-4.1-nano' para crear un gráfico de barras con datos aleatorios.

2. **ejemplo-o4-mini**: Un ejemplo que utiliza el modelo 'o4-mini' para crear un gráfico de líneas con datos aleatorios de temperatura.

## Documentación

- **como-cambiar-modelo.md**: Explica cómo cambiar el modelo predeterminado de Codex a 'o4-mini' u otros modelos disponibles.

- **codex-para-augment.md**: Explica cómo configurar y usar Codex desde Augment.

## Uso básico

Para usar Codex, simplemente ejecuta:

```bash
codex "tu pregunta o instrucción aquí"
```

Para usar un modelo específico:

```bash
codex -m o4-mini "tu pregunta o instrucción aquí"
```

Para ejecutar en modo no interactivo (solo muestra la respuesta final):

```bash
codex -q "tu pregunta o instrucción aquí"
```

## Integración con Augment

Para usar Codex desde Augment, puedes crear un alias:

```bash
alias oi='codex'
```

Y luego mencionarle a Augment:

```
Usa Open Interpreter para [tarea]
```

o

```
Ejecuta en Open Interpreter: [comando]
```
