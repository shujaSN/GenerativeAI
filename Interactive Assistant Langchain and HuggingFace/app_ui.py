from tkinter import Label, Button, Entry, Text, messagebox
from assistant import InteractiveAssistant
from query_handler import QueryHandler
from summarize_handler import SummarizeHandler

class AssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive AI Assistant")
        self.root.geometry("600x700")
        self.root.configure(bg="#2C3E50")  # Dark background color
        self.assistant = None
        self.query_handler = None
        self.summarize_handler = None

        # API Key Section
        self.api_key_label = Label(root, text="Enter Hugging Face API Token:", fg="white", bg="#2C3E50", font=("Roboto", 12))
        self.api_key_label.pack(pady=10)

        self.api_key_entry = Entry(root, width=50, show="*", font=("Roboto", 14), bg="#34495E", fg="white", bd=0, relief="flat", highlightthickness=2)
        self.api_key_entry.pack(pady=10)

        self.api_key_button = Button(root, text="Set API Key", command=self.initialize_assistant, font=("Roboto", 14), fg="white", bg="#1ABC9C", bd=0, relief="flat", highlightbackground="#16A085")
        self.api_key_button.pack(pady=20)

        # Response Section
        self.response_box = Text(root, height=15, width=70, wrap="word", font=("Roboto", 12), bg="#34495E", fg="white", bd=0, highlightthickness=1)
        self.response_box.pack(pady=10)
        self.response_box.config(state="disabled")

        # Query Section
        self.query_label = Label(root, text="Enter your query:", fg="white", bg="#2C3E50", font=("Roboto", 12))
        self.query_label.pack(pady=10)

        self.query_entry = Entry(root, width=50, font=("Roboto", 14), bg="#34495E", fg="white", bd=0, relief="flat", highlightthickness=2)
        self.query_entry.pack(pady=10)

        # Buttons for different functionalities
        self.general_button = Button(root, text="General Query", command=self.handle_general_query, font=("Roboto", 14), fg="white", bg="#2980B9", bd=0, relief="flat", highlightbackground="#3498DB")
        self.general_button.pack(pady=10)

        self.summarize_button = Button(root, text="Summarize Text", command=self.handle_summarization, font=("Roboto", 14), fg="white", bg="#2980B9", bd=0, relief="flat", highlightbackground="#3498DB")
        self.summarize_button.pack(pady=10)

    def initialize_assistant(self):
        api_key = self.api_key_entry.get()
        if not api_key:
            messagebox.showerror("Error", "API Key is required")
            return
        try:
            self.assistant = InteractiveAssistant(api_key)
            self.query_handler = QueryHandler(self.assistant)
            self.summarize_handler = SummarizeHandler(self.assistant)
            self.api_key_entry.config(state="disabled")
            self.api_key_button.config(state="disabled")
            messagebox.showinfo("Success", "Assistant Initialized Successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize assistant: {str(e)}")

    def handle_general_query(self):
        if not self.assistant:
            messagebox.showerror("Error", "Assistant is not initialized. Please set the API key.")
            return

        query = self.query_entry.get()
        if not query:
            messagebox.showerror("Error", "Query cannot be empty.")
            return

        self.response_box.config(state="normal")
        self.response_box.delete(1.0, "end")

        response = self.query_handler.handle_query(query)
        if response["success"]:
            self.response_box.insert("end", response["response"])
        else:
            self.response_box.insert("end", f"Error: {response['response']}")
        self.response_box.config(state="disabled")

    def handle_summarization(self):
        if not self.assistant:
            messagebox.showerror("Error", "Assistant is not initialized. Please set the API key.")
            return

        text = self.query_entry.get()
        if not text:
            messagebox.showerror("Error", "Text cannot be empty.")
            return

        self.response_box.config(state="normal")
        self.response_box.delete(1.0, "end")

        response = self.summarize_handler.summarize_text(text)
        if response["success"]:
            self.response_box.insert("end", response["summary"])
        else:
            self.response_box.insert("end", f"Error: {response['summary']}")
        self.response_box.config(state="disabled")
