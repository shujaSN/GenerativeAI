from assistant import InteractiveAssistant

class SummarizeHandler:
    def __init__(self, assistant: InteractiveAssistant):
        self.assistant = assistant

    def summarize_text(self, text: str, max_length: int = 130, min_length: int = 30) -> dict:
        """Summarizes the given text and returns the summary."""
        try:
            summary = self.assistant.models["summarizer"](
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )
            return {
                "summary": summary[0]['summary_text'],
                "success": True
            }
        except Exception as e:
            return {
                "summary": f"Error generating summary: {str(e)}",
                "success": False
            }
