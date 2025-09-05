# 📖 PDF to Audiobook Converter

A simple Python script that converts text from a PDF file into spoken audio, effectively turning any PDF into an audiobook.

This project uses a graphical file picker to select the PDF, making it easy and intuitive to use.

---

## ✨ Features

-   **PDF Text Extraction**: Reads text directly from PDF files page by page.
-   **Text-to-Speech (TTS)**: Converts the extracted text into clear, spoken audio.
-   **Simple GUI**: Uses Tkinter to provide a native file selection dialog.
-   **Cross-Platform**: Should work on Windows, macOS, and Linux with the required libraries installed.

---

## 🛠️ Requirements

-   Python 3.x
-   `PyPDF2` library
-   `pyttsx3` library

---

## 🚀 Installation

1.  **Clone the repository (or download the `main.py` file).**

2.  **Install the required Python libraries using pip:**
    ```bash
    pip install PyPDF2 pyttsx3
    ```

---

## ▶️ How to Use

1.  **Run the script from your terminal:**
    ```bash
    python main.py
    ```
2.  **A file selection window will open.** Navigate to and select the PDF file you want to listen to.

3.  **Click "Open".** The script will immediately start reading the text from the PDF, page by page.

---

## 💡 How It Works

-   **`tkinter.filedialog`**: This standard library module is used to create the graphical file picker dialog.
-   **`PyPDF2`**: A powerful Python library used to extract text content from each page of the selected PDF file.
-   **`pyttsx3`**: An offline, cross-platform text-to-speech library that converts the extracted text string into spoken words.

---

## 🔮 Future Enhancements

-   [ ] Save the output audio to an MP3 or WAV file.
-   [ ] Add a GUI with play, pause, and stop controls.
-   [ ] Allow users to select a specific voice or change the speech rate.
-   [ ] Add support for other document formats (e.g., .docx, .txt).
