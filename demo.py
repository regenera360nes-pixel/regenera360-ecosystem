#!/usr/bin/env python3
"""
REGENERA360 Ecosystem Demo

This script demonstrates the integration of HuggingFace connector
with the Evolutionary Optimizer in the Measure->Predict->Optimize loop.
"""

import sys
from regenera360.integrations.huggingface.connector import HuggingFaceConnector
from regenera360.agents.evolutionary_optimizer import EvolutionaryOptimizer


def main():
    print("=" * 70)
    print("REGENERA360 Ecosystem - Advanced HuggingFace Integration Demo")
    print("=" * 70)
    print()
    
    # Initialize HuggingFace Connector
    print("1. Initializing HuggingFace Connector...")
    hf_connector = HuggingFaceConnector()
    
    if hf_connector.health_check():
        print("   ✓ Connector initialized (using production token)")
    else:
        print("   ⚠ Connector initialized (using placeholder token)")
    print()
    
    # Initialize Evolutionary Optimizer
    print("2. Initializing Evolutionary Optimizer...")
    optimizer = EvolutionaryOptimizer(hf_connector=hf_connector)
    status = optimizer.get_status()
    print(f"   ✓ Optimizer ready: {status['ready']}")
    print(f"   ✓ HF Connector available: {status['hf_connector_available']}")
    print(f"   ✓ Capabilities: {', '.join(status['capabilities'][:3])}...")
    print()
    
    # Demo: Text Generation
    print("3. Demo: HuggingFace Text Generation")
    print("-" * 70)
    result = hf_connector.text_generation(
        prompt="Optimize the following code for performance:",
        max_length=150
    )
    print(f"   Prompt: Optimize the following code for performance:")
    print(f"   Generated: {result['generated_text']}")
    print(f"   Model: {result['model']}")
    print()
    
    # Demo: Classification
    print("4. Demo: HuggingFace Text Classification")
    print("-" * 70)
    result = hf_connector.classify(
        text="This system is running exceptionally well!",
        labels=["positive", "negative", "neutral"]
    )
    print(f"   Text: This system is running exceptionally well!")
    print(f"   Labels: {result['labels']}")
    print(f"   Scores: {result['scores']}")
    print()
    
    # Demo: Performance Analysis (Measure)
    print("5. Demo: Performance Analysis (MEASURE step)")
    print("-" * 70)
    metrics = {
        "latency": 250,
        "throughput": 1000,
        "error_rate": 0.02,
        "cpu_usage": 75
    }
    analysis = optimizer.analyze_performance(metrics, context="Production environment")
    print(f"   Metrics analyzed: {', '.join(analysis['metrics_analyzed'])}")
    print(f"   Insights: {len(analysis['insights'])} generated")
    for insight in analysis['insights']:
        print(f"     - {insight}")
    print()
    
    # Demo: Bottleneck Prediction (Predict)
    print("6. Demo: Bottleneck Prediction (PREDICT step)")
    print("-" * 70)
    system_state = {
        "cpu_usage": 82,
        "memory_usage": 88,
        "queue_depth": 1200,
        "active_connections": 500
    }
    predictions = optimizer.predict_bottlenecks(system_state, forecast_horizon=5)
    print(f"   Forecast horizon: {predictions['forecast_horizon']} time steps")
    print(f"   Bottlenecks predicted: {len(predictions['predicted_bottlenecks'])}")
    for bottleneck in predictions['predicted_bottlenecks']:
        print(f"     - {bottleneck['resource']}: {bottleneck['prediction']} "
              f"(severity: {bottleneck['severity']})")
    print(f"   Recommendations: {len(predictions['recommendations'])}")
    for rec in predictions['recommendations']:
        print(f"     - {rec}")
    print()
    
    # Demo: Fix Generation (Optimize)
    print("7. Demo: Fix Generation (OPTIMIZE step)")
    print("-" * 70)
    problem = "System experiencing high latency and memory pressure"
    fix = optimizer.generate_fix(problem, system_context=system_state)
    print(f"   Problem: {problem}")
    print(f"   Proposed actions ({len(fix['proposed_actions'])}):")
    for i, action in enumerate(fix['proposed_actions'][:3], 1):
        print(f"     {i}. {action}")
    print(f"   Expected impact: {fix['expected_impact']}")
    print(f"   Confidence: {fix['confidence']:.0%}")
    print()
    
    # Demo: Full Optimization Loop
    print("8. Demo: Complete Optimization Loop (Measure->Predict->Optimize)")
    print("-" * 70)
    loop_result = optimizer.run_optimization_loop(
        metrics=metrics,
        system_state=system_state,
        auto_apply=False
    )
    print(f"   ✓ Loop completed: {loop_result['loop_completed']}")
    print(f"   ✓ Analysis performed: {len(loop_result['analysis']['metrics_analyzed'])} metrics")
    print(f"   ✓ Predictions made: {len(loop_result['predictions']['predicted_bottlenecks'])} bottlenecks")
    print(f"   ✓ Fixes generated: {len(loop_result['fixes'])}")
    print(f"   ✓ Consolidated recommendations: {len(loop_result['recommendations'])}")
    print()
    print("   Top recommendations:")
    for i, rec in enumerate(loop_result['recommendations'][:3], 1):
        print(f"     {i}. {rec}")
    print()
    
    # Summary
    print("=" * 70)
    print("Demo Complete!")
    print("=" * 70)
    print()
    print("Summary:")
    print(f"  • HuggingFace tasks demonstrated: text-generation, classification")
    print(f"  • Optimization loop executed: Measure -> Predict -> Optimize")
    print(f"  • Performance records stored: {len(optimizer.performance_history)}")
    print(f"  • Optimization records stored: {len(optimizer.optimization_history)}")
    print(f"  • Prediction records stored: {len(optimizer.bottleneck_predictions)}")
    print()
    print("The system is ready for the 111 improvements expansion!")
    print()


if __name__ == "__main__":
    main()
