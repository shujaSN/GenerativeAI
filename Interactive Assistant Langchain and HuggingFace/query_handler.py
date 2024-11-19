from assistant import InteractiveAssistant

class QueryHandler:
    def __init__(self, assistant: InteractiveAssistant):
        self.assistant = assistant

    def handle_query(self, query: str) -> dict:
        """Handles the general query and returns the response."""
        try:
            prompt = f"You are a helpful assistant. Answer the following query: {query}"
            # Using the assistant to generate a response based on the query
            response = self.assistant.models["llm"].__call__(prompt)
            return {
                "response": response,
                "success": True
            }
        except Exception as e:
            return {
                "response": f"Error processing query: {str(e)}",
                "success": False
            }
