import os
import torch
from transformers import pipeline

class InteractiveAssistant:
    def __init__(self, huggingface_api_token: str):
        self._setup_environment(huggingface_api_token)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.models = {}
        self._initialize_models()

    def _setup_environment(self, token: str) -> None:
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = token

    def _initialize_models(self) -> None:
        # Initialize Summarizer model
        model_configs = {
            "summarizer": {
                "type": "summarization",
                "model": "facebook/bart-large-cnn"
            }
        }

        for model_name, config in model_configs.items():
            try:
                self.models[model_name] = pipeline(
                    config["type"],
                    model=config["model"],
                    device=0 if self.device == "cuda" else -1
                )
            except Exception as e:
                raise RuntimeError(f"Failed to initialize {model_name} model: {str(e)}")

        # Initialize LLM (Large Language Model) with corrected task for T5 model
        try:
            from langchain_huggingface.llms import HuggingFacePipeline
            self.models["llm"] = HuggingFacePipeline.from_model_id(
                model_id="google/flan-t5-large",  # Using a larger model
                task="text2text-generation"  # Corrected task for T5 model
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize LLM model: {str(e)}")
