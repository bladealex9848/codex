# Cómo cambiar el modelo en Codex

## Cambiar temporalmente el modelo para una sesión

Para cambiar temporalmente el modelo a 'o4-mini' para una sola sesión, puedes usar el flag `-m` o `--model`:

```bash
codex -m o4-mini "tu pregunta o instrucción aquí"
```

Ejemplo:
```bash
codex -m o4-mini "Crea un script en Python que genere un gráfico de barras"
```

## Cambiar permanentemente el modelo predeterminado

Si deseas cambiar permanentemente el modelo predeterminado, puedes editar el archivo de configuración de Codex:

1. Abre el archivo de configuración:
   ```bash
   nano ~/.codex/config.yaml
   ```

2. Cambia la línea `model: gpt-4.1-nano` a `model: o4-mini`:
   ```yaml
   model: o4-mini
   approvalMode: suggest
   notify: true
   ```

3. Guarda el archivo (en nano: Ctrl+O, Enter, Ctrl+X)

## Verificar el modelo actual

Para verificar qué modelo está configurado actualmente, puedes ejecutar:

```bash
cat ~/.codex/config.yaml | grep model
```

## Modelos disponibles

Algunos de los modelos disponibles son:
- gpt-4.1-nano (más rápido, menos potente)
- o4-mini (equilibrio entre velocidad y capacidad)
- gpt-4.1 (más potente, más lento)
- o3 (versión anterior, buena para tareas generales)

Elige el modelo según tus necesidades de rendimiento y complejidad de la tarea.
