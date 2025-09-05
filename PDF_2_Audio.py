import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# Prompt user to select a PDF file
book_path = askopenfilename()

# Proceed only if a file was selected
if book_path:
    # 1. Use the new 'PdfReader' class
    pdf_reader = PyPDF2.PdfReader(book_path)
    
    # Initialize the text-to-speech engine ONCE (more efficient)
    player = pyttsx3.init()
    
    # 2. Loop directly through the pages
    for page in pdf_reader.pages:
        # 3. Use the new 'extract_text()' method
        text = page.extract_text()
        
        # Read the extracted text if it's not empty
        if text:
            player.say(text)
            player.runAndWait()
            
    # Stop the engine cleanly after finishing
    player.stop()