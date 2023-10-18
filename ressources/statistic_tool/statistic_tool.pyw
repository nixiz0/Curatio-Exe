import tkinter as tk
from tkinter.constants import *

from ressources.statistic_tool.statistic_functions import *


BTN_PARAMS = {
    "activebackground":"#01879e",
    "activeforeground":"black",
    "bg":"#219ebc",
    "compound":"left",
    "disabledforeground":"#a3a3a3",
    "font":"-family {Arial} -size 18 -weight bold",
    "fg":"#ec7d1a",
    "highlightbackground":"#d9d9d9",
    "highlightcolor":"black",
    "pady": 0,
}

BTN_STAT = {
    "activebackground":"#01879e",
    "activeforeground":"black",
    "bg":"#219ebc",
    "compound":"left",
    "disabledforeground":"#a3a3a3",
    "font":"-family {Arial} -size 18 -weight bold",
    "fg":"#f0c951",
    "highlightbackground":"#d9d9d9",
    "highlightcolor":"black",
    "pady": 0,
}

class StatisticTool:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("612x476+629+120")
        top.minsize(570, 450)
        top.maxsize(650, 500)
        top.title("Statistic-Tool")
        top.configure(background="#023047")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.btn_min_max = tk.Button(self.top)
        self.btn_min_max.place(relx=0.098, rely=0.063, height=44, width=147)
        self.btn_min_max.configure(**BTN_PARAMS)
        self.btn_min_max.configure(command=main_min_max)
        self.btn_min_max.configure(text='''Min & Max''')
        
        self.btn_describe = tk.Button(self.top)
        self.btn_describe.place(relx=0.376, rely=0.063, height=44, width=147)
        self.btn_describe.configure(**BTN_PARAMS)
        self.btn_describe.configure(command=main_describe)
        self.btn_describe.configure(text='''Describe''')
        
        self.btn_std = tk.Button(self.top)
        self.btn_std.place(relx=0.654, rely=0.063, height=44, width=147)
        self.btn_std.configure(**BTN_PARAMS)
        self.btn_std.configure(command=main_std)
        self.btn_std.configure(text='''Std''')
        
        self.btn_mean = tk.Button(self.top)
        self.btn_mean.place(relx=0.098, rely=0.189, height=44, width=147)
        self.btn_mean.configure(**BTN_PARAMS)
        self.btn_mean.configure(command=main_mean)
        self.btn_mean.configure(text='''Mean''')
        
        self.btn_variance = tk.Button(self.top)
        self.btn_variance.place(relx=0.376, rely=0.189, height=44, width=147)
        self.btn_variance.configure(**BTN_PARAMS)
        self.btn_variance.configure(command=main_variance)
        self.btn_variance.configure(text='''Variance''')
        
        self.btn_freq = tk.Button(self.top)
        self.btn_freq.place(relx=0.654, rely=0.189, height=44, width=147)
        self.btn_freq.configure(**BTN_PARAMS)
        self.btn_freq.configure(command=main_frequency)
        self.btn_freq.configure(text='''Freq %''')
        
        self.btn_pca = tk.Button(self.top)
        self.btn_pca.place(relx=0.098, rely=0.315, height=44, width=147)
        self.btn_pca.configure(**BTN_PARAMS)
        self.btn_pca.configure(command=main_pca)
        self.btn_pca.configure(text='''PCA''')
        
        self.btn_boxplot = tk.Button(self.top)
        self.btn_boxplot.place(relx=0.376, rely=0.315, height=44, width=147)
        self.btn_boxplot.configure(**BTN_PARAMS)
        self.btn_boxplot.configure(command=main_boxplot)
        self.btn_boxplot.configure(text='''Boxplot''')
        
        self.btn_quartiles = tk.Button(self.top)
        self.btn_quartiles.place(relx=0.654, rely=0.315, height=44, width=147)
        self.btn_quartiles.configure(**BTN_PARAMS)
        self.btn_quartiles.configure(command=main_quartiles)
        self.btn_quartiles.configure(text='''Quartiles''')
        
        
        self.label_statistic_test = tk.Label(self.top)
        self.label_statistic_test.place(relx=0.327, rely=0.567, height=41, width=224)
        self.label_statistic_test.configure(activebackground="#f9f9f9")
        self.label_statistic_test.configure(anchor='w')
        self.label_statistic_test.configure(background="#023047")
        self.label_statistic_test.configure(compound='left')
        self.label_statistic_test.configure(disabledforeground="#a3a3a3")
        self.label_statistic_test.configure(font="-family {Arial} -size 24 -weight bold")
        self.label_statistic_test.configure(foreground="#ffb703")
        self.label_statistic_test.configure(highlightbackground="#d9d9d9")
        self.label_statistic_test.configure(highlightcolor="black")
        self.label_statistic_test.configure(text='''Statistic Test''')
        
        self.btn_chi_square = tk.Button(self.top)
        self.btn_chi_square.place(relx=0.049, rely=0.687, height=44, width=177)
        self.btn_chi_square.configure(**BTN_STAT)
        self.btn_chi_square.configure(command=main_chi_square)
        self.btn_chi_square.configure(text='''Chi-Square''')
        
        self.btn_anova = tk.Button(self.top)
        self.btn_anova.place(relx=0.359, rely=0.687, height=44, width=177)
        self.btn_anova.configure(**BTN_STAT)
        self.btn_anova.configure(command=main_anova)
        self.btn_anova.configure(text='''ANOVA''')
        
        self.btn_shapiro = tk.Button(self.top)
        self.btn_shapiro.place(relx=0.67, rely=0.687, height=44, width=177)
        self.btn_shapiro.configure(**BTN_STAT)
        self.btn_shapiro.configure(command=main_shapiro_wilk)
        self.btn_shapiro.configure(text='''Shapiro-Wilk''')
        
        self.btn_t_test = tk.Button(self.top)
        self.btn_t_test.place(relx=0.359, rely=0.811, height=44, width=177)
        self.btn_t_test.configure(**BTN_STAT)
        self.btn_t_test.configure(command=main_t_test_student)
        self.btn_t_test.configure(text='''T Test Student''')
        
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
        self.pin_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

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

def statistic_main():
    global root
    if root is not None:
        root.destroy()  # Close the window if it already exists
    root = tk.Toplevel()
    root.iconbitmap('ressources/statistic_tool/statistic_ressources/bitmap_statistic.ico')
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = StatisticTool(_top1)
    root.mainloop()

def app_theme():
    root.tk_setPalette(background='#444444', foreground='white')
    
def main_min_max():
    app_theme()
    min_max()
    
def main_describe():
    app_theme()
    describe()
    
def main_std():
    app_theme()
    std()
    
def main_mean():
    app_theme()
    mean()
    
def main_variance():
    app_theme()
    variance()
    
def main_frequency():
    app_theme()
    frequency()
    
def main_pca():
    app_theme()
    pca()
    
def main_boxplot():
    app_theme()
    boxplot()
    
def main_quartiles():
    app_theme()
    quartiles()

def main_chi_square():
    app_theme()
    chi_square()

def main_anova():
    app_theme()
    anova()

def main_shapiro_wilk():
    app_theme()
    shapiro_wilk()

def main_t_test_student():
    app_theme()
    t_test_student()


if __name__ == '__main__':
    statistic_main()