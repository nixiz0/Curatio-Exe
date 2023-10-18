import tkinter as tk
from tkinter.constants import *

from ressources.scraper_tool.scrap_tool_functions import *


BTN_PARAMS = {
    "activebackground":"#753131",
    "activeforeground":"#ffffff",
    "bg":"#bc6c25",
    "compound":"left",
    "disabledforeground":"#a3a3a3",
    "font":"-family {Times New Roman} -size 20 -weight bold",
    "fg":"#602e01",
    "highlightbackground":"#d9d9d9",
    "highlightcolor":"black",
    "pady":0,
}

class ScraperMenu:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("410x205+660+205")
        top.minsize(400, 170)
        top.maxsize(440, 215)
        top.title("Scraper-Tool")
        top.configure(background="#1d2d44")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.btn_email = tk.Button(self.top)
        self.btn_email.place(relx=0.049, rely=0.102, height=34, width=107)
        self.btn_email.configure(BTN_PARAMS)
        self.btn_email.configure(command=main_email)
        self.btn_email.configure(text='''email''')
        
        self.btn_href = tk.Button(self.top)
        self.btn_href.place(relx=0.366, rely=0.102, height=34, width=107)
        self.btn_href.configure(BTN_PARAMS)
        self.btn_href.configure(command=main_href)
        self.btn_href.configure(text='''href''')
        
        self.btn_text = tk.Button(self.top)
        self.btn_text.place(relx=0.683, rely=0.102, height=34, width=107)
        self.btn_text.configure(BTN_PARAMS)
        self.btn_text.configure(command=main_text)
        self.btn_text.configure(text='''text''')
        
        self.btn_image = tk.Button(self.top)
        self.btn_image.place(relx=0.049, rely=0.355, height=34, width=107)
        self.btn_image.configure(BTN_PARAMS)
        self.btn_image.configure(command=main_image)
        self.btn_image.configure(text='''image''')
        
        self.btn_list = tk.Button(self.top)
        self.btn_list.place(relx=0.366, rely=0.355, height=34, width=107)
        self.btn_list.configure(BTN_PARAMS)
        self.btn_list.configure(command=main_list)
        self.btn_list.configure(text='''list''')
        
        self.btn_number = tk.Button(self.top)
        self.btn_number.place(relx=0.683, rely=0.355, height=34, width=107)
        self.btn_number.configure(BTN_PARAMS)
        self.btn_number.configure(command=main_number)
        self.btn_number.configure(text='''number''')
        
        self.btn_all = tk.Button(self.top)
        self.btn_all.place(relx=0.366, rely=0.60, height=34, width=107)
        self.btn_all.configure(BTN_PARAMS)
        self.btn_all.configure(command=main_all)
        self.btn_all.configure(text='''ALL''')
        
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

def scraper_main():
    global root
    if root is not None:
        root.destroy()  # Close the window if it already exists
    root = tk.Toplevel()
    root.iconbitmap('ressources/scraper_tool/scraper_icon.ico')
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = ScraperMenu(_top1)
    root.mainloop()

def app_theme():
    root.tk_setPalette(background='#444444', foreground='white')
    
""" 
Scraping Functions
""" 
def main_email():
    app_theme()
    email()
    
def main_href():
    app_theme()
    href()
    
def main_text():
    app_theme()
    text()
    
def main_image():
    app_theme()
    image()
    
def main_list():
    app_theme()
    list()
    
def main_number():
    app_theme()
    number()
    
def main_all():
    app_theme()
    all()
    
    
if __name__ == '__main__':
    scraper_main()