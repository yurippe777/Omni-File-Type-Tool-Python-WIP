from tkinter import *
from tkinter import Tk, Label
from tkinter.filedialog import askopenfilename
import os
import PyPDF2
from PyPDF2 import PdfReader

def ppt_function():
    #turn buttons off and ask for ppt file
    toggle_buttons()
    label = Label(root, text="Select a .ppt or .pptx file", font=("Arial", 20), fg="white", bg='black')
    label.place(relx=0.5, rely=0.1, anchor="center", bordermode="outside")
    # Show a file dialog for the user to select a .ppt or .pptx file
    file_path = askopenfilename(title="Select a .ppt or .pptx file", filetypes=[("PowerPoint Files", "*.ppt;*.pptx")])

    if file_path:
        # Check if the selected file has a valid file extension
        file_extension = os.path.splitext(file_path)[1]
        if file_extension.lower() == '.ppt' or file_extension.lower() == '.pptx':
            print("Interacting with PPT file:", file_path)
            label.destroy()
            # Code for interacting with PPT files goes here
            # Open the file, read its contents, and display them in the Python program
        else:
            print("Error: Please select a .ppt or .pptx file.")
    else:
        print("No file selected.")
        label.destroy()
        toggle_buttons()
    #root.after(5000, label.destroy)
def obj_function():
    # Turn buttons off and ask for OBJ file
    toggle_buttons()
    label = Label(root, text="Select an .obj file", font=("Arial", 20), fg="white", bg='black')
    label.place(relx=0.5, rely=0.1, anchor="center", bordermode="outside")

    # Show a file dialog for the user to select an .obj file
    file_path = askopenfilename(title="Select an .obj file", filetypes=[("OBJ Files", "*.obj")])

    if file_path:
        # Check if the selected file has a valid file extension
        file_extension = os.path.splitext(file_path)[1]
        if file_extension.lower() == '.obj':
            print("Interacting with OBJ file:", file_path)
            label.destroy()
            # Code for interacting with OBJ files goes here
            # Open the file, read its contents, and display them in the Python program
        else:
            print("Error: Please select an .obj file.")
    else:
        print("No file selected.")
        label.destroy()
        toggle_buttons()


def pdf_function():
    # Turn buttons off and ask for PDF file
    toggle_buttons()
    label = Label(root, text="Select a PDF file", font=("Arial", 20), fg="white", bg='black')
    label.place(relx=0.5, rely=0.1, anchor="center", bordermode="outside")
    # Show a file dialog for the user to select a PDF file
    file_path = askopenfilename(title="Select a PDF file", filetypes=[("PDF Files", "*.pdf")])

    if file_path:
        # Check if the selected file has a valid file extension
        file_extension = os.path.splitext(file_path)[1]
        if file_extension.lower() == '.pdf':
            print("Interacting with PDF file:", file_path)
            label.destroy()

            # Create a new window to display the PDF file contents
            pdf_window = Toplevel(root)
            pdf_window.title("PDF Viewer")
            pdf_window.geometry("800x600")

            # Create a text widget to display the PDF file contents
            text_widget = Text(pdf_window, font=("Arial", 12))
            text_widget.pack(expand=True, fill=BOTH)

            # Code for interacting with PDF files goes here
            # Open the file, read its contents, and display them in the Python program
            with open(file_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                for page in range(len(pdf_reader.pages)):
                    text_widget.insert(END, pdf_reader.pages[page].extract_text())

        else:
            print("Error: Please select a PDF file.")
    else:
        print("No file selected.")
        label.destroy()
        toggle_buttons()
def on_enter(event):
    event.widget.config(bg='light green', fg='black', font=("Arial", 24, "bold"), height=int(event.widget["height"]*1.7), width=int(event.widget["width"]*1.7))
    for child in button_frame.winfo_children():
        if child != event.widget:
            child.config(height=int(child["height"]*0.3), width=int(child["width"]*0.3))

def on_leave(event):
    event.widget.config(bg='dark green', fg='white', font=("Arial", 20), height=int(event.widget["height"]/1.7), width=int(event.widget["width"]/1.7))
    for child in button_frame.winfo_children():
        if child != event.widget:
            child.config(height=int(child["height"]/0.3), width=int(child["width"]/0.3))
def toggle_buttons():
    # toggle the visibility of buttons
    if ppt_button.winfo_ismapped():
        ppt_button.grid_remove()
        obj_button.grid_remove()
        pdf_button.grid_remove()
    else:
        ppt_button.grid()
        obj_button.grid()
        pdf_button.grid()

root = Tk()

# Set the background color to dark green
root.configure(bg='dark green')

# Set the window size and minimum size
root.geometry("800x600")
root.minsize(400, 300)

# Create a frame to hold the buttons
button_frame = Frame(root, bg='#000000')
button_frame.pack(expand=True, fill=BOTH)

# Create the main menu buttons
ppt_button = Button(button_frame, text="PPT", command=ppt_function, bg='dark green', fg='white', font=("Arial", 20))
obj_button = Button(button_frame, text="OBJ", command=obj_function, bg='dark green', fg='white', font=("Arial", 20))
pdf_button = Button(button_frame, text="PDF", command=pdf_function, bg='dark green', fg='white', font=("Arial", 20))

# Bind the <Enter> and <Leave> events of the buttons to the on_enter and on_leave functions
ppt_button.bind("<Enter>", on_enter)
ppt_button.bind("<Leave>", on_leave)
obj_button.bind("<Enter>", on_enter)
obj_button.bind("<Leave>", on_leave)
pdf_button.bind("<Enter>", on_enter)
pdf_button.bind("<Leave>", on_leave)

# Add the buttons to the frame using grid layout manager
ppt_button.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
obj_button.grid(row=0, column=1, padx=10, pady=10, sticky=NSEW)
pdf_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=NSEW)

# Configure the grid to scale with the window size
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.rowconfigure(0, weight=1)
button_frame.rowconfigure(1, weight=1)


root.mainloop()