# MCP Architect - Quick Start Guide

## 🚀 Ejecución Rápida

### Opción 1: Ejecutar Todo (Recomendado)
```bash
./run.sh
```

Este comando ejecuta toda la secuencia:
1. Instala dependencias
2. Ejecuta build (optimizado PLAN 11)
3. Ejecuta orquestación
4. Valida todos los planes
5. Genera reporte GREEN

### Opción 2: Ejecutar Solo MCP Architect
```bash
python3 mcp_architect.py
```

### Opción 3: Ejecutar Scripts Individuales
```bash
# Build
./build.sh

# Orchestración
./orchestrate.sh

# Validación
./validate.sh
```

## 📊 Resultados Esperados

### Console Output
```
==================================================================
  MCP ARQUITECTO - REGENERA360 ECOSYSTEM
  Apache-2.0 License
  Prioridad: PLAN 11 (Min Time)
==================================================================

...

==================================================================
  ✓ SECUENCIA COMPLETADA EXITOSAMENTE
==================================================================

Resumen de Ejecución:
  • 11 Planes: TODOS GREEN ✓
  • Credenciales: Detectadas/Mocks funcionales
  • Build: SUCCESS
  • Orquestación: SUCCESS
  • Reporte: mcp_architect_report.json

Estado General: VERDE ✓
```

### Archivo Generado
- `mcp_architect_report.json`: Reporte completo en JSON

## 🎯 Componentes Principales

1. **Master_Config.yaml**: Configuración completa del ecosistema
2. **mcp_architect.py**: Orquestador principal
3. **111_MEJORAS.md**: Lista de mejoras clasificadas
4. **Scripts Shell**: Automatización de build, orquestación y validación

## ✅ Verificación

Para verificar que todo funciona:

```bash
# Verificar Python
python3 --version  # Requiere 3.7+

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
./run.sh
```

Deberías ver:
- ✓ Todos los servicios iniciados
- ✓ 11/11 planes en GREEN
- ✓ Estado general: VERDE

## 📖 Más Información

Ver [README.md](README.md) para documentación completa.
