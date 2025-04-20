# Cómo usar Codex desde Augment

Puedes utilizar Codex directamente desde Augment siguiendo estos pasos:

## 1. Crear un alias para Codex

Para facilitar el uso de Codex desde Augment, puedes crear un alias en tu archivo `.bashrc`, `.zshrc` o el que corresponda a tu shell:

```bash
# Añade esta línea a tu archivo de configuración de shell
alias oi='codex'
```

## 2. Usar Codex desde Augment

Cuando quieras utilizar Codex desde Augment, simplemente menciona:

```
Usa Open Interpreter para [tarea]
```

o

```
Ejecuta en Open Interpreter: [comando]
```

Augment entenderá que debe sugerir un comando usando Codex.

## 3. Ejemplos de uso

- Si dices: "Usa Open Interpreter para analizar este CSV"
  Augment responderá con: "Puedo ayudarte con eso. Ejecuta: oi \"Analiza el archivo CSV y crea visualizaciones apropiadas\""

- Si dices: "Ejecuta en Open Interpreter: genera un script para descargar imágenes"
  Augment responderá con: "Puedo ayudarte con eso. Ejecuta: oi \"Crea un script en Python para descargar imágenes de una URL\""

## 4. Cambiar el modelo para tareas específicas

Si necesitas usar un modelo más potente para una tarea específica, puedes especificarlo:

```
Usa Open Interpreter con el modelo o4-mini para [tarea compleja]
```

Augment responderá con: "Puedo ayudarte con eso. Ejecuta: oi -m o4-mini \"[instrucción detallada]\""
