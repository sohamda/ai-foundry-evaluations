import os
import json
from pathlib import Path
from dotenv import load_dotenv
from azure.ai.evaluation import (
    evaluate,
    RelevanceEvaluator,
    CoherenceEvaluator,
    IntentResolutionEvaluator,
    AzureOpenAIModelConfiguration
)

from summarize import summarize_results

load_dotenv()  # Loads variables from a .env file in the same directory (optional)

model_config = AzureOpenAIModelConfiguration(
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_KEY"),
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
)

# Initialize the Groundedness evaluator:
data_path = "../../.github/.test_files/eval-input-3.jsonl"

eval_results = evaluate(
    data=data_path,
    evaluators={
        "coherence":          CoherenceEvaluator(model_config=model_config),
        "relevance":          RelevanceEvaluator(model_config=model_config),
        "intent_resolution":  IntentResolutionEvaluator(model_config=model_config),
    }
)


summarize_results(eval_results, Path(__file__, "..", "results/summary.md").resolve())
