import tkinter as tk
from tkinter.constants import *

from ressources.type_converter_tool.type_converter_functions import *


BTN_PARAMS = {
    "activebackground":"#bb3d00",
    "activeforeground":"#000000",
    "bg":"#f4a261",
    "compound":"left",
    "disabledforeground":"#a3a3a3",
    "font":"-family {Times New Roman} -size 18 -weight bold",
    "fg":"#414141",
    "highlightbackground":"#d9d9d9",
    "highlightcolor":"black",
    "pady":0,
}

class TypeConverterMenu:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("277x429+723+166")
        top.minsize(270, 420)
        top.maxsize(280, 440)
        top.title("Type Converter Tool")
        top.configure(background="#264653")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.btn_string = tk.Button(self.top)
        self.btn_string.place(relx=0.253, rely=0.047, height=44, width=137)
        self.btn_string.configure(BTN_PARAMS)
        self.btn_string.configure(command=main_string)
        self.btn_string.configure(text='''string''')
                
        self.btn_object = tk.Button(self.top)
        self.btn_object.place(relx=0.253, rely=0.186, height=44, width=137)
        self.btn_object.configure(BTN_PARAMS)
        self.btn_object.configure(command=main_object)
        self.btn_object.configure(text='''object''')
        
        self.btn_int = tk.Button(self.top)
        self.btn_int.place(relx=0.253, rely=0.326, height=44, width=137)
        self.btn_int.configure(BTN_PARAMS)
        self.btn_int.configure(command=main_int)
        self.btn_int.configure(text='''int''')
        
        self.btn_float = tk.Button(self.top)
        self.btn_float.place(relx=0.253, rely=0.466, height=44, width=137)
        self.btn_float.configure(BTN_PARAMS)
        self.btn_float.configure(command=main_float)
        self.btn_float.configure(text='''float''')
        
        self.btn_bool = tk.Button(self.top)
        self.btn_bool.place(relx=0.253, rely=0.606, height=44, width=137)
        self.btn_bool.configure(BTN_PARAMS)
        self.btn_bool.configure(command=main_bool)
        self.btn_bool.configure(text='''bool''')
        
        self.btn_date = tk.Button(self.top)
        self.btn_date.place(relx=0.253, rely=0.746, height=44, width=137)
        self.btn_date.configure(BTN_PARAMS)
        self.btn_date.configure(command=main_date)
        self.btn_date.configure(text='''date''')
        
        # Pin Button
        self.pinned_var = tk.StringVar()
        self.pinned_var.set("   Pin   ")

        self.pin_button = tk.Button(
            self.top,
            textvariable=self.pinned_var,
            command=self.toggle_pin,
            bg="#444444", 
            fg="white"   
        )
        self.pin_button.place(relx=0.5, rely=0.92, anchor=tk.CENTER)

    def toggle_pin(self):
        if self.top.attributes('-topmost'):
            self.top.attributes('-topmost', 0)
            self.pinned_var.set("   Pin   ")
        else:
            self.top.attributes('-topmost', 1)
            self.pinned_var.set("  Unpin  ")


"""
Functions & Main
"""
root = None

def type_converter_main():
    global root
    if root is not None:
        root.destroy()  # Close the window if it already exists
    root = tk.Toplevel()
    root.iconbitmap('ressources/type_converter_tool/type_converter_icon.ico')
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = TypeConverterMenu(_top1)
    root.mainloop()

def app_theme():
    root.tk_setPalette(background='#444444', foreground='white')
    
""" 
Type Converter Functions
""" 
def main_string():
    app_theme()
    string_converter()
    
def main_object():
    app_theme()
    object_converter()
    
def main_int():
    app_theme()
    int_converter()
    
def main_float():
    app_theme()
    float_converter()
    
def main_bool():
    app_theme()
    bool_converter()
    
def main_date():
    app_theme()
    date_converter()
    
    
if __name__ == '__main__':
    type_converter_main()