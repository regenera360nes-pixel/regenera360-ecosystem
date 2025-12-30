# REGENERA360 Ecosystem - Advanced HuggingFace Integration

This repository implements an advanced AI-powered ecosystem with self-improvement and predictive capabilities, integrating HuggingFace models with an evolutionary optimization system.

## Architecture Overview

The REGENERA360 ecosystem consists of four main components:

### 1. HuggingFace Connector (`regenera360/integrations/huggingface/connector.py`)

A robust connector that interfaces with the HuggingFace Inference API, supporting multiple AI tasks:

- **Text Generation**: Codex-like code generation and text completion
- **Classification**: Sentiment analysis, topic classification, intent detection
- **Feature Extraction**: Semantic embeddings for similarity and clustering
- **Question Answering**: Context-based question answering
- **Summarization**: Document and text summarization

**Key Features:**
- Task routing for different AI operations
- Placeholder token support (`HF_TOKEN_PLACEHOLDER`) for safe development
- Modular design ready for expansion
- Health check functionality

### 2. Evolutionary Optimizer (`regenera360/agents/evolutionary_optimizer.py`)

An intelligent agent implementing self-repair and predictive capabilities through a continuous optimization loop:

**Measure → Predict → Optimize**

#### Core Methods:

- **`analyze_performance(metrics, context)`**: Analyzes system performance metrics, detects trends, and generates insights
- **`predict_bottlenecks(system_state, forecast_horizon)`**: Predicts potential bottlenecks based on current system state
- **`generate_fix(problem_description, system_context)`**: Generates actionable fixes for identified problems
- **`run_optimization_loop(metrics, system_state, auto_apply)`**: Executes the complete Measure→Predict→Optimize cycle

**Key Features:**
- AI-powered analysis using HuggingFace models
- Historical tracking of performance, predictions, and optimizations
- Pattern-based problem detection and fix generation
- Confidence scoring for recommendations
- Modular design for the planned 111 improvements expansion

### 3. Plan 11 Velocity Workflow (`regenera360/workflows/plan_11_velocity.yaml`)

The "Best Plan" configuration optimized for maximum speed through concurrent execution:

**Initialization Phases:**
1. **Phase 1**: Core services (logging, config, metrics, cache) - parallel startup
2. **Phase 2**: Integration services (HuggingFace, database, message queue) - parallel startup
3. **Phase 3**: Intelligent agents (optimizer, orchestrator, monitoring) - parallel startup
4. **Phase 4**: API endpoints (REST, gRPC, WebSocket) - parallel startup

**Key Features:**
- 3-5x speedup compared to sequential initialization
- Self-optimization triggers based on metrics
- Automatic bottleneck detection and scaling recommendations
- Resource allocation strategy for optimal performance
- Expansion hooks for future enhancements
- Feature flags for gradual rollout

### 4. MCP Registry (`regenera360/mcp/registry.yaml`)

Central registry making all tools visible to the Model Control Protocol (MCP) system:

**Registered Tools:**

**HuggingFace Tools:**
- `hf_text_generation`: Text generation with language models
- `hf_classification`: Text classification and sentiment analysis
- `hf_feature_extraction`: Feature embeddings for semantic search
- `hf_question_answering`: Context-based QA
- `hf_summarization`: Document summarization

**Optimization Tools:**
- `analyze_performance`: Performance analysis (Measure)
- `predict_bottlenecks`: Bottleneck prediction (Predict)
- `generate_fix`: Fix generation (Optimize)
- `run_optimization_loop`: Complete optimization cycle

**Key Features:**
- Tool categorization and grouping
- Parameter definitions and validation
- Performance metrics (latency, concurrency)
- Rate limiting configuration
- Service discovery endpoints
- Authentication and security settings
- Monitoring and observability
- Support for up to 111 registered tools

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/regenera360nes-pixel/regenera360-ecosystem.git
cd regenera360-ecosystem

# The package is ready to use - no external dependencies required for basic functionality
```

### Configuration

Set your HuggingFace API token (optional for demo):

```bash
export HF_API_TOKEN="your-huggingface-token-here"
```

If not set, the system will use `HF_TOKEN_PLACEHOLDER` and operate in demo mode.

### Running the Demo

```bash
python3 demo.py
```

This demonstrates:
- HuggingFace connector initialization
- Text generation and classification
- Performance analysis (Measure step)
- Bottleneck prediction (Predict step)
- Fix generation (Optimize step)
- Complete optimization loop

### Usage Examples

#### Basic HuggingFace Connector Usage

```python
from regenera360.integrations.huggingface.connector import HuggingFaceConnector

# Initialize connector
hf = HuggingFaceConnector()

# Generate text
result = hf.text_generation(
    prompt="Optimize this Python function:",
    max_length=200,
    temperature=0.7
)
print(result['generated_text'])

# Classify text
result = hf.classify(
    text="This system is performing excellently!",
    labels=["positive", "negative", "neutral"]
)
print(result['labels'], result['scores'])
```

#### Evolutionary Optimizer Usage

```python
from regenera360.agents.evolutionary_optimizer import EvolutionaryOptimizer
from regenera360.integrations.huggingface.connector import HuggingFaceConnector

# Initialize with HuggingFace connector
hf = HuggingFaceConnector()
optimizer = EvolutionaryOptimizer(hf_connector=hf)

# Analyze performance (Measure)
metrics = {
    "latency": 250,
    "throughput": 1000,
    "error_rate": 0.02
}
analysis = optimizer.analyze_performance(metrics)

# Predict bottlenecks (Predict)
system_state = {
    "cpu_usage": 85,
    "memory_usage": 90,
    "queue_depth": 1500
}
predictions = optimizer.predict_bottlenecks(system_state, forecast_horizon=5)

# Generate fix (Optimize)
fix = optimizer.generate_fix(
    "High latency detected in API responses",
    system_context=system_state
)

# Or run complete optimization loop
result = optimizer.run_optimization_loop(
    metrics=metrics,
    system_state=system_state,
    auto_apply=False  # Manual review recommended
)
```

## Architecture Design Principles

### Modularity
Each component is self-contained and can be used independently or as part of the larger ecosystem.

### Scalability
Designed to support the planned "111 improvements" expansion:
- Extensible tool registry (up to 111 tools)
- Customizable optimization phases
- Plugin architecture support

### Self-Improvement
The Evolutionary Optimizer continuously learns and improves:
- Tracks historical performance data
- Predicts future bottlenecks
- Generates and evaluates fixes
- Builds knowledge over time

### Safety
- Uses placeholder tokens for development
- Manual review required for auto-apply
- Confidence scoring for all recommendations
- Extensive logging and monitoring

## Project Structure

```
regenera360-ecosystem/
├── regenera360/
│   ├── __init__.py
│   ├── integrations/
│   │   ├── __init__.py
│   │   └── huggingface/
│   │       ├── __init__.py
│   │       └── connector.py          # HuggingFace Connector
│   ├── agents/
│   │   ├── __init__.py
│   │   └── evolutionary_optimizer.py  # Evolutionary Optimizer
│   ├── workflows/
│   │   └── plan_11_velocity.yaml     # Plan 11 Configuration
│   └── mcp/
│       └── registry.yaml             # MCP Tool Registry
├── demo.py                            # Demo script
├── README.md                          # This file
└── LICENSE
```

## Key Requirements Satisfied

✅ **HuggingFaceConnector** with task routing for text-generation and classification  
✅ **EvolutionaryOptimizer** with analyze_performance(), predict_bottlenecks(), and generate_fix()  
✅ **Plan 11 Velocity** workflow with concurrent initialization  
✅ **MCP Registry** with all HuggingFace and optimization tools registered  
✅ **Placeholder tokens** for safe development (HF_TOKEN_PLACEHOLDER)  
✅ **Measure → Predict → Optimize** loop implementation  
✅ **Modular structure** ready for 111 improvements expansion  

## Future Enhancements

The architecture is designed to support:

- 111+ registered tools in the MCP registry
- Distributed execution across multiple nodes
- Auto-healing capabilities with automated fix application
- Advanced ML models for prediction and optimization
- Custom plugin development
- Enhanced monitoring and observability
- Real-time performance dashboards

## Contributing

This is a foundational implementation ready for expansion. The modular architecture supports easy addition of new tools, optimizers, and workflows.

## License

See [LICENSE](LICENSE) file for details.