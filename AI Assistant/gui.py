import tkinter as tk
from tkinter import filedialog, messagebox
from summarizer import TextSummarizer
from file_loader import FileLoader

class TextSummarizerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Summarizer Using Langchain & Hugging Face")
        self.root.geometry("900x600")
        self.root.configure(bg="#282c34")  # Dark background color for a modern look

        # Initialize Summarizer and FileLoader
        self.summarizer = TextSummarizer()
        self.file_loader = FileLoader()

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Font settings for a modern look
        font_large = ("Helvetica Neue", 15, "bold")
        font_medium = ("Helvetica Neue", 12)

        # Header Label
        instructions_label = tk.Label(
            self.root, text="Text Summarizer", font=font_large,
            bg="#282c34", fg="#61dafb", pady=10
        )
        instructions_label.pack(pady=(20, 10))

        # Input Text Area with Frame and Scrollbar
        text_input_frame = tk.Frame(self.root, bg="#282c34", highlightbackground="#61dafb", highlightthickness=1, bd=0)
        text_input_frame.pack(pady=(10, 20), padx=20, fill=tk.BOTH, expand=True)
        
        self.text_input = tk.Text(
            text_input_frame, height=10, wrap=tk.WORD, font=font_medium,
            bg="#353a42", fg="#ffffff", insertbackground="white",
            relief="flat", padx=10, pady=10, bd=0
        )
        self.text_input.pack(fill=tk.BOTH, expand=True)

        # Buttons Frame for alignment
        buttons_frame = tk.Frame(self.root, bg="#282c34")
        buttons_frame.pack(pady=(10, 10))

        # Summarize Button with hover effect
        summarize_button = tk.Button(
            buttons_frame, text="Summarize", command=self.summarize_text,
            font=font_medium, bg="#61dafb", fg="#282c34",
            activebackground="#21a1c1", activeforeground="#ffffff",
            relief="flat", padx=20, pady=10, cursor="hand2"
        )
        summarize_button.grid(row=0, column=0, padx=(0, 10))

        # Load File Button with hover effect
        load_button = tk.Button(
            buttons_frame, text="Upload File (pdf)", command=self.load_file,
            font=font_medium, bg="#61dafb", fg="#282c34",
            activebackground="#21a1c1", activeforeground="#ffffff",
            relief="flat", padx=20, pady=10, cursor="hand2"
        )
        load_button.grid(row=0, column=1)

        # Output Label
        output_label = tk.Label(self.root, text="Summary", font=font_large, bg="#282c34", fg="#61dafb")
        output_label.pack(pady=(20, 10))

        # Summary Text Area with Frame and Scrollbar
        summary_frame = tk.Frame(self.root, bg="#282c34", highlightbackground="#61dafb", highlightthickness=1, bd=0)
        summary_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.summarized_text = tk.Text(
            summary_frame, height=10, wrap=tk.WORD, font=font_medium,
            bg="#353a42", fg="#ffffff", insertbackground="white",
            relief="flat", padx=10, pady=10, bd=0
        )
        self.summarized_text.pack(fill=tk.BOTH, expand=True)

    def summarize_text(self):
        article_text = self.text_input.get("1.0", "end-1c")
        if article_text.strip():
            try:
                summary = self.summarizer.summarize_text(article_text)
                self.summarized_text.delete("1.0", "end")
                self.summarized_text.insert("1.0", summary)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during summarization: {str(e)}")
        else:
            self.summarized_text.delete("1.0", "end")
            self.summarized_text.insert("1.0", "Please enter some text to summarize.")

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Upload File (pdf)", filetypes=[ ("PDF Files", "*.pdf")])
        if file_path:
            if file_path.endswith(".pdf"):
                article_text = self.file_loader.load_pdf(file_path)
                self.text_input.delete("1.0", "end")
                self.text_input.insert("1.0", article_text)

    def run(self):
        self.root.mainloop()
