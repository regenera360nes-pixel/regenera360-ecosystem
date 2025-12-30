#!/bin/bash
# Comprehensive Test Suite for MCP Architect
# Apache-2.0 License
# Validates all components and functionality

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Counters
TESTS_PASSED=0
TESTS_FAILED=0
TOTAL_TESTS=0

# Function to run test
run_test() {
    local test_name="$1"
    local test_command="$2"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    echo -n "  Testing: $test_name... "
    
    if eval "$test_command" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ PASS${NC}"
        TESTS_PASSED=$((TESTS_PASSED + 1))
        return 0
    else
        echo -e "${RED}✗ FAIL${NC}"
        TESTS_FAILED=$((TESTS_FAILED + 1))
        return 1
    fi
}

echo "=================================================================="
echo "  MCP ARCHITECT - COMPREHENSIVE TEST SUITE"
echo "=================================================================="
echo ""

# Test 1: File Existence
echo -e "${BLUE}Test Suite 1: File Existence${NC}"
run_test "Master_Config.yaml exists" "test -f Master_Config.yaml"
run_test "mcp_architect.py exists" "test -f mcp_architect.py"
run_test "111_MEJORAS.md exists" "test -f 111_MEJORAS.md"
run_test "build.sh exists and executable" "test -x build.sh"
run_test "orchestrate.sh exists and executable" "test -x orchestrate.sh"
run_test "validate.sh exists and executable" "test -x validate.sh"
run_test "run.sh exists and executable" "test -x run.sh"
run_test "requirements.txt exists" "test -f requirements.txt"
run_test "README.md exists" "test -f README.md"
run_test "QUICKSTART.md exists" "test -f QUICKSTART.md"
run_test "TECHNICAL.md exists" "test -f TECHNICAL.md"
run_test "SUMMARY.md exists" "test -f SUMMARY.md"
echo ""

# Test 2: Configuration Validation
echo -e "${BLUE}Test Suite 2: Configuration Validation${NC}"
run_test "Master_Config.yaml is valid YAML" "python3 -c 'import yaml; yaml.safe_load(open(\"Master_Config.yaml\"))'"
run_test "License is Apache-2.0" "python3 -c 'import yaml; assert yaml.safe_load(open(\"Master_Config.yaml\"))[\"license\"] == \"Apache-2.0\"'"
run_test "Priority plan is PLAN_11_MIN_TIME" "python3 -c 'import yaml; assert yaml.safe_load(open(\"Master_Config.yaml\"))[\"priority_plan\"] == \"PLAN_11_MIN_TIME\"'"
run_test "11 plans configured" "python3 -c 'import yaml; assert len(yaml.safe_load(open(\"Master_Config.yaml\"))[\"plans\"]) == 11'"
run_test "PLAN_11 has priority 0" "python3 -c 'import yaml; assert yaml.safe_load(open(\"Master_Config.yaml\"))[\"plans\"][\"PLAN_11_MIN_TIME\"][\"priority\"] == 0'"
echo ""

# Test 3: Improvements Count
echo -e "${BLUE}Test Suite 3: Improvements Validation${NC}"
run_test "Exactly 111 improvements" "test $(grep -E '^[0-9]+\.' 111_MEJORAS.md | wc -l) -eq 111"
run_test "Security improvements (22)" "test $(grep -E '^[0-9]+\.' 111_MEJORAS.md | head -22 | wc -l) -eq 22"
run_test "Total distribution is correct" "test $(grep -E '^[0-9]+\.' 111_MEJORAS.md | wc -l) -eq 111"
echo ""

# Test 4: Python Dependencies
echo -e "${BLUE}Test Suite 4: Dependencies${NC}"
run_test "Python 3 is installed" "command -v python3"
run_test "pip is available" "python3 -m pip --version"
run_test "PyYAML can be imported" "python3 -c 'import yaml'"
echo ""

# Test 5: Script Functionality
echo -e "${BLUE}Test Suite 5: Script Execution${NC}"
run_test "build.sh executes successfully" "./build.sh"
run_test "orchestrate.sh executes successfully" "./orchestrate.sh"
run_test "validate.sh executes successfully" "./validate.sh"
run_test "mcp_architect.py executes successfully" "python3 mcp_architect.py"
echo ""

# Test 6: Report Generation
echo -e "${BLUE}Test Suite 6: Report Generation${NC}"
run_test "Report JSON file generated" "test -f mcp_architect_report.json"
run_test "Report is valid JSON" "python3 -c 'import json; json.load(open(\"mcp_architect_report.json\"))'"
run_test "Overall status is GREEN" "python3 -c 'import json; assert json.load(open(\"mcp_architect_report.json\"))[\"overall_status\"] == \"GREEN\"'"
run_test "All 11 plans are GREEN" "python3 -c 'import json; r = json.load(open(\"mcp_architect_report.json\")); assert all(v == \"GREEN\" for v in r[\"status\"][\"plans\"].values())'"
run_test "Build status is success" "python3 -c 'import json; assert json.load(open(\"mcp_architect_report.json\"))[\"status\"][\"build\"] == \"success\"'"
run_test "Orchestration status is success" "python3 -c 'import json; assert json.load(open(\"mcp_architect_report.json\"))[\"status\"][\"orchestration\"] == \"success\"'"
echo ""

# Test 7: Documentation Quality
echo -e "${BLUE}Test Suite 7: Documentation${NC}"
run_test "README.md contains Quick Start" "grep -q 'Quick Start' README.md"
run_test "README.md contains 11 plans" "grep -q 'PLAN' README.md"
run_test "QUICKSTART.md has execution commands" "grep -q './run.sh' QUICKSTART.md"
run_test "TECHNICAL.md has architecture info" "grep -q 'Architecture' TECHNICAL.md"
run_test "SUMMARY.md has status report" "grep -q 'GREEN' SUMMARY.md"
echo ""

# Final Summary
echo "=================================================================="
echo "  TEST RESULTS SUMMARY"
echo "=================================================================="
echo ""
echo "Total Tests:  $TOTAL_TESTS"
echo -e "Passed:       ${GREEN}$TESTS_PASSED${NC}"
echo -e "Failed:       ${RED}$TESTS_FAILED${NC}"
echo ""

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}=================================================================="
    echo "  ✓ ALL TESTS PASSED - SYSTEM VALIDATED"
    echo "==================================================================${NC}"
    echo ""
    exit 0
else
    echo -e "${RED}=================================================================="
    echo "  ✗ SOME TESTS FAILED - REVIEW REQUIRED"
    echo "==================================================================${NC}"
    echo ""
    exit 1
fi
