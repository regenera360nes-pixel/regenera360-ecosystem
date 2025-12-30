"""
Evolutionary Optimizer for REGENERA360 Ecosystem

This module implements self-repair and predictive logic for the system,
following the Measure -> Predict -> Optimize loop pattern.
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)


class EvolutionaryOptimizer:
    """
    Evolutionary Optimizer implementing Self-Repair and Predictive capabilities.
    
    This agent uses the HuggingFace connector to "think" and make intelligent
    decisions about system optimization, bottleneck prediction, and self-repair.
    
    Pattern: Measure -> Predict -> Optimize
    """
    
    def __init__(self, hf_connector=None):
        """
        Initialize the Evolutionary Optimizer.
        
        Args:
            hf_connector: HuggingFaceConnector instance for AI-powered analysis.
                         If None, creates a placeholder that logs actions.
        """
        self.hf_connector = hf_connector
        self.performance_history: List[Dict[str, Any]] = []
        self.optimization_history: List[Dict[str, Any]] = []
        self.bottleneck_predictions: List[Dict[str, Any]] = []
        logger.info("EvolutionaryOptimizer initialized")
    
    def analyze_performance(
        self,
        metrics: Dict[str, Any],
        context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Analyze system performance metrics.
        
        This is the "Measure" step of the optimization loop.
        
        Args:
            metrics: Dictionary of performance metrics (e.g., latency, throughput, error_rate)
            context: Optional context about the system state
            
        Returns:
            Analysis results including insights and recommendations
        """
        timestamp = datetime.utcnow().isoformat()
        
        logger.info(f"Analyzing performance metrics: {list(metrics.keys())}")
        
        # Store in history
        analysis_record = {
            "timestamp": timestamp,
            "metrics": metrics,
            "context": context
        }
        self.performance_history.append(analysis_record)
        
        # Calculate basic statistics
        analysis = {
            "timestamp": timestamp,
            "metrics_analyzed": list(metrics.keys()),
            "summary": {},
            "insights": []
        }
        
        # Analyze each metric
        for metric_name, metric_value in metrics.items():
            if isinstance(metric_value, (int, float)):
                # Get historical values for this metric
                historical_values = [
                    record["metrics"].get(metric_name)
                    for record in self.performance_history[-10:]
                    if metric_name in record["metrics"]
                    and isinstance(record["metrics"][metric_name], (int, float))
                ]
                
                if len(historical_values) > 1:
                    avg = sum(historical_values) / len(historical_values)
                    trend = "increasing" if metric_value > avg else "decreasing"
                    
                    analysis["summary"][metric_name] = {
                        "current": metric_value,
                        "average": avg,
                        "trend": trend
                    }
                    
                    # Generate insights
                    if metric_name in ["latency", "error_rate"] and trend == "increasing":
                        analysis["insights"].append(
                            f"{metric_name} is trending upward - potential performance degradation"
                        )
                    elif metric_name in ["throughput", "success_rate"] and trend == "decreasing":
                        analysis["insights"].append(
                            f"{metric_name} is trending downward - optimization may be needed"
                        )
        
        # Use HF connector for advanced analysis if available
        if self.hf_connector:
            try:
                analysis_prompt = self._build_analysis_prompt(metrics, context)
                ai_analysis = self.hf_connector.text_generation(
                    prompt=analysis_prompt,
                    max_length=200,
                    temperature=0.3
                )
                analysis["ai_insights"] = ai_analysis.get("generated_text", "")
            except Exception as e:
                logger.warning(f"AI analysis failed: {e}")
                analysis["ai_insights"] = None
        
        return analysis
    
    def predict_bottlenecks(
        self,
        system_state: Dict[str, Any],
        forecast_horizon: int = 5
    ) -> Dict[str, Any]:
        """
        Predict potential system bottlenecks.
        
        This is the "Predict" step of the optimization loop.
        
        Args:
            system_state: Current state of the system (resources, load, etc.)
            forecast_horizon: Number of time steps to predict ahead
            
        Returns:
            Predictions including likely bottlenecks and confidence scores
        """
        timestamp = datetime.utcnow().isoformat()
        
        logger.info(f"Predicting bottlenecks with horizon: {forecast_horizon}")
        
        predictions = {
            "timestamp": timestamp,
            "forecast_horizon": forecast_horizon,
            "predicted_bottlenecks": [],
            "recommendations": []
        }
        
        # Analyze resource utilization
        resource_warnings = []
        if "cpu_usage" in system_state and system_state["cpu_usage"] > 80:
            resource_warnings.append({
                "resource": "cpu",
                "current_usage": system_state["cpu_usage"],
                "severity": "high",
                "prediction": "CPU saturation imminent"
            })
        
        if "memory_usage" in system_state and system_state["memory_usage"] > 85:
            resource_warnings.append({
                "resource": "memory",
                "current_usage": system_state["memory_usage"],
                "severity": "high",
                "prediction": "Memory exhaustion risk"
            })
        
        if "queue_depth" in system_state and system_state["queue_depth"] > 1000:
            resource_warnings.append({
                "resource": "queue",
                "current_depth": system_state["queue_depth"],
                "severity": "medium",
                "prediction": "Queue backlog building"
            })
        
        predictions["predicted_bottlenecks"] = resource_warnings
        
        # Generate recommendations based on predictions
        for warning in resource_warnings:
            if warning["resource"] == "cpu":
                predictions["recommendations"].append(
                    "Scale horizontally or optimize CPU-intensive operations"
                )
            elif warning["resource"] == "memory":
                predictions["recommendations"].append(
                    "Implement memory caching strategies or increase allocation"
                )
            elif warning["resource"] == "queue":
                predictions["recommendations"].append(
                    "Increase worker pool size or implement batch processing"
                )
        
        # Use HF connector for predictive analysis if available
        if self.hf_connector and self.performance_history:
            try:
                prediction_prompt = self._build_prediction_prompt(system_state, forecast_horizon)
                ai_prediction = self.hf_connector.text_generation(
                    prompt=prediction_prompt,
                    max_length=250,
                    temperature=0.4
                )
                predictions["ai_prediction"] = ai_prediction.get("generated_text", "")
            except Exception as e:
                logger.warning(f"AI prediction failed: {e}")
                predictions["ai_prediction"] = None
        
        # Store prediction
        self.bottleneck_predictions.append(predictions)
        
        return predictions
    
    def generate_fix(
        self,
        problem_description: str,
        system_context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate a fix for identified problems.
        
        This is the "Optimize" step of the optimization loop.
        
        Args:
            problem_description: Description of the problem to fix
            system_context: Optional context about the system state
            
        Returns:
            Fix proposal including actions and expected impact
        """
        timestamp = datetime.utcnow().isoformat()
        
        logger.info(f"Generating fix for: {problem_description[:100]}")
        
        fix_proposal = {
            "timestamp": timestamp,
            "problem": problem_description,
            "proposed_actions": [],
            "expected_impact": {},
            "confidence": 0.0
        }
        
        # Pattern matching for common problems
        problem_lower = problem_description.lower()
        
        if "latency" in problem_lower or "slow" in problem_lower:
            fix_proposal["proposed_actions"].extend([
                "Enable response caching for frequently accessed data",
                "Implement connection pooling",
                "Add database query indexing"
            ])
            fix_proposal["expected_impact"]["latency_reduction"] = "30-50%"
            fix_proposal["confidence"] = 0.75
        
        if "memory" in problem_lower or "leak" in problem_lower:
            fix_proposal["proposed_actions"].extend([
                "Implement proper resource cleanup in finally blocks",
                "Review object lifecycle management",
                "Add memory profiling instrumentation"
            ])
            fix_proposal["expected_impact"]["memory_usage_reduction"] = "20-40%"
            fix_proposal["confidence"] = 0.70
        
        if "error" in problem_lower or "failure" in problem_lower:
            fix_proposal["proposed_actions"].extend([
                "Add retry logic with exponential backoff",
                "Implement circuit breaker pattern",
                "Enhance error logging and monitoring"
            ])
            fix_proposal["expected_impact"]["error_rate_reduction"] = "40-60%"
            fix_proposal["confidence"] = 0.80
        
        if "bottleneck" in problem_lower or "throughput" in problem_lower:
            fix_proposal["proposed_actions"].extend([
                "Implement parallel processing",
                "Add load balancing",
                "Optimize critical path operations"
            ])
            fix_proposal["expected_impact"]["throughput_increase"] = "2-3x"
            fix_proposal["confidence"] = 0.65
        
        # Use HF connector for AI-powered fix generation
        if self.hf_connector:
            try:
                fix_prompt = self._build_fix_prompt(problem_description, system_context)
                ai_fix = self.hf_connector.text_generation(
                    prompt=fix_prompt,
                    max_length=300,
                    temperature=0.5
                )
                fix_proposal["ai_generated_fix"] = ai_fix.get("generated_text", "")
                # Boost confidence if AI provides additional insight
                if fix_proposal["ai_generated_fix"]:
                    fix_proposal["confidence"] = min(fix_proposal["confidence"] + 0.1, 0.95)
            except Exception as e:
                logger.warning(f"AI fix generation failed: {e}")
                fix_proposal["ai_generated_fix"] = None
        
        # Store in optimization history
        self.optimization_history.append(fix_proposal)
        
        return fix_proposal
    
    def run_optimization_loop(
        self,
        metrics: Dict[str, Any],
        system_state: Dict[str, Any],
        auto_apply: bool = False
    ) -> Dict[str, Any]:
        """
        Run complete optimization loop: Measure -> Predict -> Optimize.
        
        Args:
            metrics: Performance metrics to analyze
            system_state: Current system state
            auto_apply: Whether to automatically apply optimizations (default: False)
            
        Returns:
            Complete optimization cycle results
        """
        logger.info("Starting optimization loop: Measure -> Predict -> Optimize")
        
        # Step 1: Measure
        analysis = self.analyze_performance(metrics)
        
        # Step 2: Predict
        predictions = self.predict_bottlenecks(system_state)
        
        # Step 3: Optimize (generate fixes for predicted issues)
        fixes = []
        for bottleneck in predictions.get("predicted_bottlenecks", []):
            problem_desc = f"{bottleneck['resource']} bottleneck: {bottleneck['prediction']}"
            fix = self.generate_fix(problem_desc, system_state)
            fixes.append(fix)
        
        optimization_result = {
            "loop_completed": True,
            "analysis": analysis,
            "predictions": predictions,
            "fixes": fixes,
            "auto_applied": auto_apply,
            "recommendations": self._consolidate_recommendations(analysis, predictions, fixes)
        }
        
        if auto_apply:
            logger.warning("Auto-apply enabled but not implemented - manual review required")
            optimization_result["auto_apply_status"] = "pending_implementation"
        
        return optimization_result
    
    def _build_analysis_prompt(self, metrics: Dict[str, Any], context: Optional[str]) -> str:
        """Build prompt for AI-powered performance analysis."""
        prompt = f"Analyze the following system performance metrics:\n{json.dumps(metrics, indent=2)}\n"
        if context:
            prompt += f"Context: {context}\n"
        prompt += "Provide insights and identify potential issues:"
        return prompt
    
    def _build_prediction_prompt(self, system_state: Dict[str, Any], horizon: int) -> str:
        """Build prompt for AI-powered bottleneck prediction."""
        prompt = f"Based on current system state:\n{json.dumps(system_state, indent=2)}\n"
        prompt += f"Predict potential bottlenecks in the next {horizon} time steps:"
        return prompt
    
    def _build_fix_prompt(self, problem: str, context: Optional[Dict[str, Any]]) -> str:
        """Build prompt for AI-powered fix generation."""
        prompt = f"Problem: {problem}\n"
        if context:
            prompt += f"System context: {json.dumps(context, indent=2)}\n"
        prompt += "Generate specific actions to resolve this problem:"
        return prompt
    
    def _consolidate_recommendations(
        self,
        analysis: Dict[str, Any],
        predictions: Dict[str, Any],
        fixes: List[Dict[str, Any]]
    ) -> List[str]:
        """Consolidate recommendations from all optimization steps."""
        recommendations = []
        
        # From analysis
        if "insights" in analysis:
            recommendations.extend(analysis["insights"])
        
        # From predictions
        if "recommendations" in predictions:
            recommendations.extend(predictions["recommendations"])
        
        # From fixes (top actions)
        for fix in fixes[:3]:  # Limit to top 3 fixes
            if fix.get("proposed_actions"):
                recommendations.append(f"Priority fix: {fix['proposed_actions'][0]}")
        
        return list(set(recommendations))  # Remove duplicates
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current status of the optimizer.
        
        Returns:
            Status information including history sizes and readiness
        """
        return {
            "ready": True,
            "hf_connector_available": self.hf_connector is not None,
            "performance_records": len(self.performance_history),
            "optimization_records": len(self.optimization_history),
            "prediction_records": len(self.bottleneck_predictions),
            "capabilities": [
                "analyze_performance",
                "predict_bottlenecks",
                "generate_fix",
                "run_optimization_loop"
            ]
        }
