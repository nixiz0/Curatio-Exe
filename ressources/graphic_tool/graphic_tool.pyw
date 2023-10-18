import tkinter as tk
from tkinter.constants import *

from ressources.graphic_tool.graphics_functions import *


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'

BTN_PARAMS = {
    "activebackground":"#880000",
    "activeforeground":"#2d2d2d",
    "bg":"#b10d10",
    "compound":"left",
    "disabledforeground":"#a3a3a3",
    "font":"-family {Arial} -size 16 -weight bold",
    "fg":"#f4c095",
    "highlightbackground":"#d9d9d9",
    "highlightcolor":"black",
}

class GraphicMenu:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("580x350+652+143")
        top.minsize(580, 350)
        top.maxsize(650, 450)
        top.title("Graphic-Tool")
        top.configure(background="#071e22")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        hist_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/histogram.png")
        self.btn_hist = tk.Button(self.top)
        self.btn_hist.place(relx=0.083, rely=0.084, height=44, width=147)
        self.btn_hist.configure(**BTN_PARAMS)
        self.btn_hist.configure(command=main_histogram)
        self.btn_hist.configure(pady="0")
        self.btn_hist.configure(text='''Histogram''')
        self.btn_hist.configure(image=hist_png)
        self.btn_hist.image = hist_png
        
        scatter_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/scatter.png")
        self.btn_scatter = tk.Button(self.top)
        self.btn_scatter.place(relx=0.381, rely=0.084, height=44, width=147)
        self.btn_scatter.configure(**BTN_PARAMS)
        self.btn_scatter.configure(command=main_scatter_plot)
        self.btn_scatter.configure(pady="0")
        self.btn_scatter.configure(text='''Scatter''')
        self.btn_scatter.configure(image=scatter_png)
        self.btn_scatter.image = scatter_png
        
        box_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/box.png")
        self.btn_box = tk.Button(self.top)
        self.btn_box.place(relx=0.679, rely=0.084, height=44, width=147)
        self.btn_box.configure(**BTN_PARAMS)
        self.btn_box.configure(command=main_box_plot)
        self.btn_box.configure(pady="0")
        self.btn_box.configure(text=''' Box''')
        self.btn_box.configure(image=box_png)
        self.btn_box.image = box_png
        
        pie_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/pie.png")
        self.btn_pie = tk.Button(self.top)
        self.btn_pie.place(relx=0.083, rely=0.231, height=44, width=147)
        self.btn_pie.configure(**BTN_PARAMS)
        self.btn_pie.configure(command=main_pie_charts)
        self.btn_pie.configure(pady="0")
        self.btn_pie.configure(text='''Pie''')
        self.btn_pie.configure(image=pie_png)
        self.btn_pie.image = pie_png
        
        bar_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/bar.png")
        self.btn_bar = tk.Button(self.top)
        self.btn_bar.place(relx=0.381, rely=0.231, height=44, width=147)
        self.btn_bar.configure(**BTN_PARAMS)
        self.btn_bar.configure(command=main_bar_plot)
        self.btn_bar.configure(pady="0")
        self.btn_bar.configure(text=''' Bar''')
        self.btn_bar.configure(image=bar_png)
        self.btn_bar.image = bar_png
        
        surface_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/surface.png")
        self.btn_surface = tk.Button(self.top)
        self.btn_surface.place(relx=0.679, rely=0.231, height=44, width=147)
        self.btn_surface.configure(**BTN_PARAMS)
        self.btn_surface.configure(command=main_surface_plot)
        self.btn_surface.configure(pady="0")
        self.btn_surface.configure(text='''Surface''')
        self.btn_surface.configure(image=surface_png)
        self.btn_surface.image = surface_png
        
        heatmap_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/heatmap.png")
        self.btn_heatmap = tk.Button(self.top)
        self.btn_heatmap.place(relx=0.083, rely=0.378, height=44, width=147)
        self.btn_heatmap.configure(**BTN_PARAMS)
        self.btn_heatmap.configure(command=main_heatmap)
        self.btn_heatmap.configure(pady="0")
        self.btn_heatmap.configure(text='''HeatMap''')
        self.btn_heatmap.configure(image=heatmap_png)
        self.btn_heatmap.image = heatmap_png
        
        violin_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/violin.png")
        self.btn_violin = tk.Button(self.top)
        self.btn_violin.place(relx=0.381, rely=0.378, height=44, width=147)
        self.btn_violin.configure(**BTN_PARAMS)
        self.btn_violin.configure(command=main_violin_plot)
        self.btn_violin.configure(pady="0")
        self.btn_violin.configure(text=''' Violin''')
        self.btn_violin.configure(image=violin_png)
        self.btn_violin.image = violin_png
        
        butterfly_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/butterfly.png")
        self.btn_butterfly = tk.Button(self.top)
        self.btn_butterfly.place(relx=0.679, rely=0.378, height=44, width=147)
        self.btn_butterfly.configure(**BTN_PARAMS)
        self.btn_butterfly.configure(command=main_butterfly)
        self.btn_butterfly.configure(pady="0")
        self.btn_butterfly.configure(text='''Butterfly''')
        self.btn_butterfly.configure(image=butterfly_png)
        self.btn_butterfly.image = butterfly_png
        
        correlation_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/correlation.png")
        self.btn_corr = tk.Button(self.top)
        self.btn_corr.place(relx=0.083, rely=0.525, height=44, width=147)
        self.btn_corr.configure(**BTN_PARAMS)
        self.btn_corr.configure(command=main_correlation)
        self.btn_corr.configure(pady="0")
        self.btn_corr.configure(text='''Correlation''')
        self.btn_corr.configure(image=correlation_png)
        self.btn_corr.image = correlation_png
        
        stem_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/stem.png")
        self.btn_stem = tk.Button(self.top)
        self.btn_stem.place(relx=0.381, rely=0.525, height=44, width=147)
        self.btn_stem.configure(**BTN_PARAMS)
        self.btn_stem.configure(command=main_stem_plot)
        self.btn_stem.configure(pady="0")
        self.btn_stem.configure(text=''' Stem''')
        self.btn_stem.configure(image=stem_png)
        self.btn_stem.image = stem_png
        
        density_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/density.png")
        self.btn_density = tk.Button(self.top)
        self.btn_density.place(relx=0.679, rely=0.525, height=44, width=147)
        self.btn_density.configure(**BTN_PARAMS)
        self.btn_density.configure(command=main_density_plot)
        self.btn_density.configure(pady="0")
        self.btn_density.configure(text='''Density''')
        self.btn_density.configure(image=density_png)
        self.btn_density.image = density_png
    
        corr_heatmap_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/corr_heatmap.png")
        self.btn_corr_heatmap = tk.Button(self.top)
        self.btn_corr_heatmap.place(relx=0.083, rely=0.672, height=44, width=147)
        self.btn_corr_heatmap.configure(**BTN_PARAMS)
        self.btn_corr_heatmap.configure(font="-family {Arial} -size 13 -weight bold")
        self.btn_corr_heatmap.configure(command=main_corr_heatmap)
        self.btn_corr_heatmap.configure(pady="0")
        self.btn_corr_heatmap.configure(text=''' Corr HeatMap''')
        self.btn_corr_heatmap.configure(image=corr_heatmap_png)
        self.btn_corr_heatmap.image = corr_heatmap_png
        
        distribution_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/distribution.png")
        self.btn_distrib = tk.Button(self.top)
        self.btn_distrib.place(relx=0.381, rely=0.672, height=44, width=147)
        self.btn_distrib.configure(**BTN_PARAMS)
        self.btn_distrib.configure(font="-family {Arial} -size 14 -weight bold")
        self.btn_distrib.configure(command=main_distribution)
        self.btn_distrib.configure(pady="0")
        self.btn_distrib.configure(text='''Distribution''')
        self.btn_distrib.configure(image=distribution_png)
        self.btn_distrib.image = distribution_png
        
        categorical_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/categorical.png")
        self.btn_categorical = tk.Button(self.top)
        self.btn_categorical.place(relx=0.679, rely=0.672, height=44, width=147)
        self.btn_categorical.configure(**BTN_PARAMS)
        self.btn_categorical.configure(font="-family {Arial} -size 14 -weight bold")
        self.btn_categorical.configure(command=main_categorical)
        self.btn_categorical.configure(pady="0")
        self.btn_categorical.configure(text='''Categorical''')
        self.btn_categorical.configure(image=categorical_png)
        self.btn_categorical.image = categorical_png


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

def graphic_main():
    global root
    if root is not None:
        root.destroy()  # Close the window if it already exists
    root = tk.Toplevel()
    root.iconbitmap('ressources/graphic_tool/graphic_ressources/bitmap_graphic.ico')
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = GraphicMenu(_top1)
    root.mainloop()

def app_theme():
    root.tk_setPalette(background='#444444', foreground='white')
    
""" 
Graphic Functions
""" 
def main_histogram():
    app_theme()
    histogram()
    
def main_scatter_plot():
    app_theme()
    scatter_plot()
    
def main_box_plot():
    app_theme()
    box_plot()
    
def main_pie_charts():
    app_theme()
    pie_charts()
    
def main_bar_plot():
    app_theme()
    bar_plot()
    
def main_surface_plot():
    app_theme()
    surface_plot()
    
def main_heatmap():
    app_theme()
    heatmap()
    
def main_violin_plot():
    app_theme()
    violin_plot()
    
def main_butterfly():
    app_theme()
    butterfly()
    
def main_correlation():
    app_theme()
    correlation()
    
def main_stem_plot():
    app_theme()
    stem_plot()
    
def main_density_plot():
    app_theme()
    density_plot()
    
def main_corr_heatmap():
    app_theme()
    corr_heatmap()
    
def main_distribution():
    app_theme()
    distribution()
    
def main_categorical():
    app_theme()
    categorical()
    

if __name__ == '__main__':
    graphic_main()