from langchain.prompts import PromptTemplate
from langchain_huggingface.llms import HuggingFacePipeline

class TextSummarizer:
    def __init__(self):
        # Initialize the Hugging Face model pipeline for summarization
        self.llm = HuggingFacePipeline.from_model_id(
            model_id="facebook/bart-large-cnn",  # Model designed for summarization
            task="summarization",  # Summarization task
            pipeline_kwargs={"max_length": 250, "min_length": 50, "do_sample": False},  # Adjust max_length to 50
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
        
        # Use the invoke method instead of __call__
        summary = self.llm.invoke(prompt_input)
        return summary
