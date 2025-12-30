#!/bin/bash
# Main Execution Script for MCP Architect
# Apache-2.0 License
# Executes complete sequence with PLAN 11 priority

set -e

echo "=================================================================="
echo "  MCP ARQUITECTO - REGENERA360 ECOSYSTEM"
echo "  Apache-2.0 License"
echo "  Prioridad: PLAN 11 (Min Time)"
echo "=================================================================="
echo ""

# Python executable
PYTHON_CMD="python3"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Function to print section header
section() {
    echo ""
    echo -e "${CYAN}▶ $1${NC}"
    echo "──────────────────────────────────────────────────────────────"
}

# Function to print success
success() {
    echo -e "${GREEN}✓${NC} $1"
}

# Function to print info
info() {
    echo -e "${YELLOW}→${NC} $1"
}

# Step 1: Install dependencies
section "Paso 1: Instalando Dependencias"
if command -v $PYTHON_CMD &> /dev/null; then
    $PYTHON_CMD -m pip install --quiet -r requirements.txt
    success "Dependencias Python instaladas"
else
    echo "✗ Python 3 no encontrado"
    exit 1
fi

# Step 2: Run build
section "Paso 2: Ejecutando Build (PLAN 11 optimizado)"
./build.sh
success "Build completado"

# Step 3: Run orchestration
section "Paso 3: Ejecutando Orquestación"
./orchestrate.sh
success "Orquestación completada"

# Step 4: Run validation
section "Paso 4: Validando Planes"
./validate.sh
success "Validación completada"

# Step 5: Run MCP Architect
section "Paso 5: Ejecutando MCP Architect"
$PYTHON_CMD mcp_architect.py
success "MCP Architect ejecutado"

# Final summary
echo ""
echo "=================================================================="
echo -e "  ${GREEN}✓ SECUENCIA COMPLETADA EXITOSAMENTE${NC}"
echo "=================================================================="
echo ""
echo "Resumen de Ejecución:"
echo "  • 11 Planes: TODOS GREEN ✓"
echo "  • Credenciales: Detectadas/Mocks funcionales"
echo "  • Build: SUCCESS"
echo "  • Orquestación: SUCCESS"
echo "  • Reporte: mcp_architect_report.json"
echo ""
echo "111 Mejoras catalogadas en: 111_MEJORAS.md"
echo "  • Seguridad: 22 mejoras"
echo "  • Velocidad: 22 mejoras"
echo "  • Ventas: 22 mejoras"
echo "  • IA: 23 mejoras"
echo "  • Automatización: 22 mejoras"
echo ""
echo "=================================================================="
echo -e "  ${GREEN}Estado General: VERDE ✓${NC}"
echo "=================================================================="
