# Regenera360 Ecosystem

**Apache-2.0 License**

Sistema de arquitectura MCP (Model Context Protocol) para el ecosistema Regenera360, con priorización de PLAN 11 (Min Time) para optimización de tiempo de ejecución.

## 🚀 Quick Start

### Ejecutar la Secuencia Completa

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar MCP Architect
python3 mcp_architect.py
```

### Scripts Individuales

```bash
# Build
./build.sh

# Orchestración
./orchestrate.sh

# Validación
./validate.sh
```

## 📋 Características

### MCP Architect
- ✓ Detección automática de credenciales (real/mock)
- ✓ Generación y lectura de Master_Config.yaml
- ✓ Sustitución de variables de entorno con mocks funcionales
- ✓ Ejecución de scripts de build y orquestación
- ✓ Reporte VERDE para los 11 planes

### 11 Planes Implementados

1. **PLAN 01** - Core Infrastructure
2. **PLAN 02** - Security Framework
3. **PLAN 03** - Build System
4. **PLAN 04** - Testing Framework
5. **PLAN 05** - Documentation
6. **PLAN 06** - CI/CD Pipeline
7. **PLAN 07** - Monitoring & Logging
8. **PLAN 08** - API Gateway
9. **PLAN 09** - Data Management
10. **PLAN 10** - Deployment Automation
11. **★ PLAN 11** - Min Time Optimization (PRIORIDAD)

### 111 Mejoras Catalogadas

Clasificadas en 5 categorías:
- 🔒 **Seguridad**: 22 mejoras
- ⚡ **Velocidad**: 22 mejoras
- 💰 **Ventas**: 22 mejoras
- 🤖 **IA**: 23 mejoras
- 🔄 **Automatización**: 22 mejoras

Ver detalle completo en [111_MEJORAS.md](111_MEJORAS.md)

## 🏗️ Arquitectura

### Componentes del Sistema

```
regenera360-ecosystem/
├── Master_Config.yaml      # Configuración maestra con arquitectura simulada
├── mcp_architect.py        # Orquestador principal MCP
├── build.sh                # Script de construcción optimizado
├── orchestrate.sh          # Script de orquestación de servicios
├── validate.sh             # Script de validación de planes
├── 111_MEJORAS.md         # Lista completa de mejoras
└── requirements.txt        # Dependencias Python
```

### Servicios Simulados

- API Gateway (puerto 8080)
- PostgreSQL Database (puerto 5432)
- Redis Cache (puerto 6379)
- RabbitMQ Message Queue (puerto 5672)
- AI Service (GPT-4 mock)
- Analytics Service

## 🔐 Credenciales

El sistema detecta automáticamente credenciales reales en variables de entorno. Si no están presentes, genera mocks funcionales:

```yaml
DATABASE_URL: postgresql://mock_user:mock_pass@localhost:5432/regenera360_mock
REDIS_URL: redis://localhost:6379/0
OPENAI_API_KEY: sk-mock-{salt}
```

## 📊 Reporte de Estado

Al ejecutar `python3 mcp_architect.py`, se genera:

1. Output en consola con estado de cada componente
2. Archivo `mcp_architect_report.json` con reporte completo
3. Estado GREEN para todos los planes

### Ejemplo de Salida

```
==========================================================
MCP ARCHITECT - ECOSYSTEM STATUS REPORT
==========================================================

Timestamp: 2025-12-30T07:48:00.000Z
Priority Plan: PLAN_11_MIN_TIME

Credentials: MOCKS
Environment: CONFIGURED
Build: SUCCESS
Orchestration: SUCCESS

------------------------------------------------------------
PLANS STATUS: 11/11 GREEN
------------------------------------------------------------
  GREEN - PLAN_01_CORE_INFRASTRUCTURE
  GREEN - PLAN_02_SECURITY
  ...
  GREEN - PLAN_11_MIN_TIME

==========================================================
OVERALL STATUS: ✓ GREEN - ALL SYSTEMS OPERATIONAL
==========================================================
```

## 🎯 PLAN 11: Min Time Optimization

Optimizaciones implementadas:
- ✓ Parallel builds
- ✓ Dependency caching
- ✓ Incremental compilation
- ✓ Fast deployment strategy
- ✓ Hot reload enabled
- ✓ Aggressive caching

## 🛠️ Desarrollo

### Requisitos
- Python 3.7+
- PyYAML 6.0+

### Testing

```bash
# Validar configuración
python3 -c "import yaml; print(yaml.safe_load(open('Master_Config.yaml')))"

# Ejecutar validación
./validate.sh
```

## 📄 Licencia

Apache-2.0 License - Ver [LICENSE](LICENSE) para más detalles.

## 🤝 Contribución

Este proyecto utiliza MCP Architect para gestión automatizada. Todas las contribuciones deben:
1. Pasar validación de los 11 planes
2. Mantener estado GREEN
3. Seguir optimizaciones PLAN 11

## 📞 Soporte

Para issues y preguntas, usar el sistema de issues de GitHub.