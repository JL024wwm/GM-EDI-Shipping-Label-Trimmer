from PyPDF2 import PdfWriter, PdfReader,Transformation
import tkinter as tk
from tkinter import filedialog as fd
import re
import os


def open_pdf_file(): 

    root = tk.Tk()
    root.title = ('GM Label Processor')
    root.geometry('600x350')
  
    # Specify the file types 
    filetypes = (('pdf files', '*.pdf'), 
                 ('All files', '*.*')) 
    # Show the open file dialog by specifying path 
    root.filename = fd.askopenfilename(filetypes=filetypes, 
                       initialdir="D:/Downloads",title="Select the GM Label") 

    root.mainloop()

    return root.filename

def extract_directory_from_text(input_text):
    # Regular expression to find the file path
    match = re.search(r"'(.*?)'", input_text)

    # Extract the directory if a match is found
    if match:
        file_path = match.group(1)
        directory = os.path.dirname(file_path)
        return directory
    else:
        return "No file path found in the text."

a=str(open_pdf_file())
#b=extract_directory_from_text(a)
#print(b)

reader = PdfReader(a)
writer = PdfWriter()
totalPages = len(reader.pages)

for i in range(0,totalPages,1):
        page = reader.pages[i]
    
        page.cropbox.lower_left = (135,495)
        page.cropbox.upper_right = (579,792)

        writer.add_page(page)
        writer.add_page(page)

with open(a, "wb") as fp: 
        writer.write(fp)




    
    
