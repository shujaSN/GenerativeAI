from langchain.prompts import PromptTemplate
from langchain_huggingface.llms import HuggingFacePipeline

class TextSummarizer:
    def __init__(self):
        # Initialize the Hugging Face model pipeline for summarization
        self.llm = HuggingFacePipeline.from_model_id(
            model_id="facebook/bart-large-cnn",  # Model designed for summarization
            task="summarization",  # Summarization task
            pipeline_kwargs={"max_length": 250, "min_length": 50, "do_sample": False},  # Adjust max_length to 250
        )
        
        # Define a prompt template for summarization
        summarization_prompt = """
        Summarize the following document:
        {document}
        """
        self.prompt = PromptTemplate(input_variables=["document"], template=summarization_prompt)

    def summarize_text(self, article_text):
        # Format the prompt
        prompt_input = self.prompt.format(document=article_text)
        
        # Use the __call__ method for inference
        summary = self.llm.__call__(prompt_input)
        return summary

