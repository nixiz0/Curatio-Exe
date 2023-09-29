import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import filedialog, messagebox, simpledialog
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os.path


_script = sys.argv[0]
_location = os.path.dirname(_script)

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
        self.btn_hist.configure(command=histogram)
        self.btn_hist.configure(pady="0")
        self.btn_hist.configure(text='''Histogram''')
        self.btn_hist.configure(image=hist_png)
        self.btn_hist.image = hist_png
        
        scatter_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/scatter.png")
        self.btn_scatter = tk.Button(self.top)
        self.btn_scatter.place(relx=0.381, rely=0.084, height=44, width=147)
        self.btn_scatter.configure(**BTN_PARAMS)
        self.btn_scatter.configure(command=scatter_plot)
        self.btn_scatter.configure(pady="0")
        self.btn_scatter.configure(text='''Scatter''')
        self.btn_scatter.configure(image=scatter_png)
        self.btn_scatter.image = scatter_png
        
        box_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/box.png")
        self.btn_box = tk.Button(self.top)
        self.btn_box.place(relx=0.679, rely=0.084, height=44, width=147)
        self.btn_box.configure(**BTN_PARAMS)
        self.btn_box.configure(command=box_plot)
        self.btn_box.configure(pady="0")
        self.btn_box.configure(text=''' Box''')
        self.btn_box.configure(image=box_png)
        self.btn_box.image = box_png
        
        pie_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/pie.png")
        self.btn_pie = tk.Button(self.top)
        self.btn_pie.place(relx=0.083, rely=0.231, height=44, width=147)
        self.btn_pie.configure(**BTN_PARAMS)
        self.btn_pie.configure(command=pie_charts)
        self.btn_pie.configure(pady="0")
        self.btn_pie.configure(text='''Pie''')
        self.btn_pie.configure(image=pie_png)
        self.btn_pie.image = pie_png
        
        bar_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/bar.png")
        self.btn_bar = tk.Button(self.top)
        self.btn_bar.place(relx=0.381, rely=0.231, height=44, width=147)
        self.btn_bar.configure(**BTN_PARAMS)
        self.btn_bar.configure(command=bar_plot)
        self.btn_bar.configure(pady="0")
        self.btn_bar.configure(text=''' Bar''')
        self.btn_bar.configure(image=bar_png)
        self.btn_bar.image = bar_png
        
        surface_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/surface.png")
        self.btn_surface = tk.Button(self.top)
        self.btn_surface.place(relx=0.679, rely=0.231, height=44, width=147)
        self.btn_surface.configure(**BTN_PARAMS)
        self.btn_surface.configure(command=surface_plot)
        self.btn_surface.configure(pady="0")
        self.btn_surface.configure(text='''Surface''')
        self.btn_surface.configure(image=surface_png)
        self.btn_surface.image = surface_png
        
        heatmap_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/heatmap.png")
        self.btn_heatmap = tk.Button(self.top)
        self.btn_heatmap.place(relx=0.083, rely=0.378, height=44, width=147)
        self.btn_heatmap.configure(**BTN_PARAMS)
        self.btn_heatmap.configure(command=heatmap)
        self.btn_heatmap.configure(pady="0")
        self.btn_heatmap.configure(text='''HeatMap''')
        self.btn_heatmap.configure(image=heatmap_png)
        self.btn_heatmap.image = heatmap_png
        
        violin_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/violin.png")
        self.btn_violin = tk.Button(self.top)
        self.btn_violin.place(relx=0.381, rely=0.378, height=44, width=147)
        self.btn_violin.configure(**BTN_PARAMS)
        self.btn_violin.configure(command=violin_plot)
        self.btn_violin.configure(pady="0")
        self.btn_violin.configure(text=''' Violin''')
        self.btn_violin.configure(image=violin_png)
        self.btn_violin.image = violin_png
        
        butterfly_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/butterfly.png")
        self.btn_butterfly = tk.Button(self.top)
        self.btn_butterfly.place(relx=0.679, rely=0.378, height=44, width=147)
        self.btn_butterfly.configure(**BTN_PARAMS)
        self.btn_butterfly.configure(command=butterfly)
        self.btn_butterfly.configure(pady="0")
        self.btn_butterfly.configure(text='''Butterfly''')
        self.btn_butterfly.configure(image=butterfly_png)
        self.btn_butterfly.image = butterfly_png
        
        correlation_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/correlation.png")
        self.btn_corr = tk.Button(self.top)
        self.btn_corr.place(relx=0.083, rely=0.525, height=44, width=147)
        self.btn_corr.configure(**BTN_PARAMS)
        self.btn_corr.configure(command=correlation)
        self.btn_corr.configure(pady="0")
        self.btn_corr.configure(text='''Correlation''')
        self.btn_corr.configure(image=correlation_png)
        self.btn_corr.image = correlation_png
        
        stem_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/stem.png")
        self.btn_stem = tk.Button(self.top)
        self.btn_stem.place(relx=0.381, rely=0.525, height=44, width=147)
        self.btn_stem.configure(**BTN_PARAMS)
        self.btn_stem.configure(command=stem_plot)
        self.btn_stem.configure(pady="0")
        self.btn_stem.configure(text=''' Stem''')
        self.btn_stem.configure(image=stem_png)
        self.btn_stem.image = stem_png
        
        density_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/density.png")
        self.btn_density = tk.Button(self.top)
        self.btn_density.place(relx=0.679, rely=0.525, height=44, width=147)
        self.btn_density.configure(**BTN_PARAMS)
        self.btn_density.configure(command=density_plot)
        self.btn_density.configure(pady="0")
        self.btn_density.configure(text='''Density''')
        self.btn_density.configure(image=density_png)
        self.btn_density.image = density_png
        
        distribution_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/distribution.png")
        self.btn_distrib = tk.Button(self.top)
        self.btn_distrib.place(relx=0.083, rely=0.672, height=44, width=147)
        self.btn_distrib.configure(**BTN_PARAMS)
        self.btn_distrib.configure(font="-family {Arial} -size 14 -weight bold")
        self.btn_distrib.configure(command=distribution)
        self.btn_distrib.configure(pady="0")
        self.btn_distrib.configure(text='''Distribution''')
        self.btn_distrib.configure(image=distribution_png)
        self.btn_distrib.image = distribution_png
        
        categorical_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/categorical.png")
        self.btn_categorical = tk.Button(self.top)
        self.btn_categorical.place(relx=0.381, rely=0.672, height=44, width=147)
        self.btn_categorical.configure(**BTN_PARAMS)
        self.btn_categorical.configure(font="-family {Arial} -size 14 -weight bold")
        self.btn_categorical.configure(command=categorical)
        self.btn_categorical.configure(pady="0")
        self.btn_categorical.configure(text='''Categorical''')
        self.btn_categorical.configure(image=categorical_png)
        self.btn_categorical.image = categorical_png
        
        cluster_png = tk.PhotoImage(file="ressources/graphic_tool/graphic_ressources/cluster.png")
        self.btn_cluster = tk.Button(self.top)
        self.btn_cluster.place(relx=0.679, rely=0.672, height=44, width=147)
        self.btn_cluster.configure(**BTN_PARAMS)
        self.btn_cluster.configure(command=clusters)
        self.btn_cluster.configure(pady="0")
        self.btn_cluster.configure(text='''Cluster''')
        self.btn_cluster.configure(image=cluster_png)
        self.btn_cluster.image = cluster_png



"""
########################################################
################ FUNCTIONS TOOLS & Main ################
########################################################
"""
def graphic_main():
    global root
    root = tk.Toplevel()
    root.iconbitmap('ressources/graphic_tool/graphic_ressources/bitmap_graphic.ico')
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = GraphicMenu(_top1)
    root.mainloop()

def app_theme():
    root.tk_setPalette(background='#444444', foreground='white')
    
def histogram():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user how many values ​​they want to display
    num_values = simpledialog.askinteger("Choisir le nombre de valeurs", "Entrez 1 ou 2.\n\n --> 1 pour afficher un histogramme avec 1 valeur.\n --> 2 pour afficher un histogramme avec 2 valeurs.")
    if num_values not in [1, 2]:
        messagebox.showwarning("Avertissement", "Veuillez entrer 1 ou 2.")
        return

    # Ask the user to enter the name of the column(s)
    column_input = simpledialog.askstring("Choisir la colonne(s)", "Entrez le(s) nom(s) de colonne(s) (séparé par une virgule) :")
    column_names = [col.strip() for col in column_input.split(',')]

    # Check that column names are valid
    if len(column_names) != num_values:
        messagebox.showwarning("Avertissement", f"Vous devez entrer {num_values} nom(s) de colonne(s).")
        return

    # Create Histogram
    for col in column_names:
        plt.hist(df[col], alpha=0.7, label=col)

    if num_values == 1:
        plt.xlabel(column_names[0])
        plt.ylabel("Fréquence")
        plt.title(f"Histogramme de {column_names[0]}")
    else:
        plt.xlabel(column_names[0])
        plt.ylabel(column_names[1])
        plt.title(f"Histogramme de {column_names[0]} et {column_names[1]}")

    plt.legend()
    plt.show()
    
    
def scatter_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user how many values ​​they want to display
    num_values = simpledialog.askinteger("Choisir le nombre de valeurs", "Entrez 1 ou 2.\n\n --> 1 pour afficher un scatter plot avec 1 valeur.\n --> 2 pour afficher un scatter plot avec 2 valeurs.")
    if num_values not in [1, 2]:
        messagebox.showwarning("Avertissement", "Veuillez entrer 1 ou 2.")
        return

    # Ask the user to enter the name of the column(s)
    column_input = simpledialog.askstring("Choisir la colonne(s)", "Entrez le(s) nom(s) de colonne(s) (séparé par une virgule) :")
    column_names = [col.strip() for col in column_input.split(',')]

    # Check that column names are valid
    if len(column_names) != num_values:
        messagebox.showwarning("Avertissement", f"Vous devez entrer {num_values} nom(s) de colonne(s).")
        return

    # Create the Scatter Plot
    if num_values == 1:
        plt.scatter(df[column_names[0]], df.index)
        plt.xlabel(column_names[0])
        plt.title(f"Scatter Plot de {column_names[0]}")
    else:
        plt.scatter(df[column_names[0]], df[column_names[1]])
        plt.xlabel(column_names[0])
        plt.ylabel(column_names[1])
        plt.title(f"Scatter Plot de {column_names[0]} et {column_names[1]}")

    plt.show()
    
    
def box_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user how many values ​​they want to display
    num_values = simpledialog.askinteger("Choisir le nombre de valeurs", "Entrez 1 ou 2.\n\n --> 1 pour afficher un box plot avec 1 valeur.\n --> 2 pour afficher un box plot avec 2 valeurs.")
    if num_values not in [1, 2]:
        messagebox.showwarning("Avertissement", "Veuillez entrer 1 ou 2.")
        return

    # Ask the user to enter the name of the column(s)
    column_input = simpledialog.askstring("Choisir la colonne(s)", "Entrez le(s) nom(s) de colonne(s) (séparé par une virgule) :")
    column_names = [col.strip() for col in column_input.split(',')]

    # Check that column names are valid
    if len(column_names) != num_values:
        messagebox.showwarning("Avertissement", f"Vous devez entrer {num_values} nom(s) de colonne(s).")
        return

    # Create the Box Plot
    if num_values == 1:
        plt.boxplot(df[column_names[0]])
        plt.xlabel(column_names[0])
        plt.title(f"Box Plot de {column_names[0]}")
    else:
        data = [df[column] for column in column_names]
        plt.boxplot(data, labels=column_names)
        plt.xlabel("Colonnes")
        plt.ylabel("Valeurs")
        plt.title(f"Box Plot de {', '.join(column_names)}")

    plt.show()
    
    
def pie_charts():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to choose the column for the pie chart
    column_name = simpledialog.askstring("Choisir la colonne", "Entrez le nom de la colonne pour le pie chart :")

    # Check that the column name is valid
    if column_name not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{column_name}' n'existe pas dans le fichier CSV.")
        return

    # Get column data
    data = df[column_name].value_counts()

    # Create the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal') # To make the pie chart a circle
    plt.title(f"Diagramme circulaire de la colonne '{column_name}'")
    plt.show()
    
    
def bar_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter the category column name
    category_column = simpledialog.askstring("Choisir la colonne des catégories", "Entrez le nom de la colonne des catégories :")

    # Check that the column name is valid
    if category_column not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{category_column}' n'existe pas dans le fichier CSV.")
        return

    # Ask the user to enter the name of the values ​​column
    value_column = simpledialog.askstring("Choisir la colonne des valeurs", "Entrez le nom de la colonne des valeurs :")

    # Check that the column name is valid
    if value_column not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{value_column}' n'existe pas dans le fichier CSV.")
        return

    # Create the bar plot
    plt.figure(figsize=(12, 6))
    plt.bar(df[category_column], df[value_column])
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.title(f"Diagramme à Barres de {value_column} par {category_column}")
    plt.xticks(rotation=45, ha='right')
    
    plt.show()
    
    
def surface_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter the name of column X & Check that column name X is valid
    x_column = simpledialog.askstring("Choisir la colonne X", "Entrez le nom de la colonne X (valeurs numériques):")
    if x_column not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{x_column}' n'existe pas dans le fichier CSV.")
        return

    # Ask the user to enter the name of column Y & Check that column name Y is valid
    y_column = simpledialog.askstring("Choisir la colonne Y", "Entrez le nom de la colonne Y (valeurs numériques) :")
    if y_column not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{y_column}' n'existe pas dans le fichier CSV.")
        return

    # Ask the user to enter the name of column Z & Check that column name Z is valid
    z_column = simpledialog.askstring("Choisir la colonne Z (valeurs)", "Entrez le nom de la colonne Z (valeurs numériques) :")
    if z_column not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{z_column}' n'existe pas dans le fichier CSV.")
        return

    # Create the surface diagram
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(df[x_column], df[y_column], df[z_column], cmap='viridis')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_zlabel(z_column)
    ax.set_title(f"Diagramme de Surface de {z_column} en fonction de {x_column} et {y_column}")

    plt.show()
    

def heatmap():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)
    
    choice_heatmap = simpledialog.askstring("Veuillez entrer 2 ou 3 \n", "--> 2 pour une heatmap à 2 colonnes simples (crosstab). \n --> 3 pour une heatmap à 3 colonnes, plus avancées (pivot).")
    if (choice_heatmap != '2') and (choice_heatmap != '3'):
        messagebox.showerror("Erreur", "Veuillez entrer 2 ou 3.")
        return
    else: 
        if choice_heatmap == '2':
            col1 = simpledialog.askstring("Entrée", "Entrez le nom de la colonne 1 :")
            if not col1:
                messagebox.showerror("Erreur", "Le nom de la colonne 1 ne peut pas être vide.")
                return

            col2 = simpledialog.askstring("Entrée", "Entrez le nom de la colonne 2 :")
            if not col2:
                messagebox.showerror("Erreur", "Le nom de la colonne 2 ne peut pas être vide.")
                return

            # Check if column names exist in the DataFrame
            if col1 not in df.columns or col2 not in df.columns:
                messagebox.showerror("Erreur", "Les noms de colonnes saisis ne sont pas présents dans le fichier.")
                return

            # Create heat map using seaborn and matplotlib
            crosstab_data = pd.crosstab(df[col1], df[col2])
            plt.figure(figsize=(12, 8))
            sns.heatmap(crosstab_data, annot=True, fmt="d", cmap="YlGnBu")
            plt.title("Carte de chaleur")
            plt.xlabel(col2)
            plt.ylabel(col1)
            plt.show()
        else: 
            # Prompt user to enter column name X & Verify that column name X is valid
            x_column = simpledialog.askstring("Choisir la colonne X", "Entrez le nom de la colonne X :")
            if x_column not in df.columns:
                messagebox.showwarning("Avertissement", f"La colonne '{x_column}' n'existe pas dans le fichier CSV.")
                return

            # Prompt user to enter column name Y & Verify that column name Y is valid
            y_column = simpledialog.askstring("Choisir la colonne Y", "Entrez le nom de la colonne Y :")
            if y_column not in df.columns:
                messagebox.showwarning("Avertissement", f"La colonne '{y_column}' n'existe pas dans le fichier CSV.")
                return

            # Prompt user to enter column name Z & Verify that column name Z is valid
            value_column = simpledialog.askstring("Choisir la colonne des valeurs (Z)", "Entrez le nom de la colonne des valeurs (Z) :")
            if value_column not in df.columns:
                messagebox.showwarning("Avertissement", f"La colonne '{value_column}' n'existe pas dans le fichier CSV.")
                return

            # Create the pivot dataframe for the heatmap
            pivot_df = df.pivot(index=y_column, columns=x_column, values=value_column)

            # Create HeatMap
            plt.figure(figsize=(10, 6))
            sns.heatmap(pivot_df, cmap="YlGnBu", annot=True, fmt=".2f", cbar=True)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f"Heatmap de {value_column} par {x_column} et {y_column}")
            plt.show()
    
    
def violin_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter the category column name & Check that the category column name is valid
    category_column = simpledialog.askstring("Choisir la colonne des catégories", "Entrez le nom de la colonne des catégories :")
    if category_column not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{category_column}' n'existe pas dans le fichier CSV.")
        return

    # Ask the user to enter the name of the values ​​column & Verify that the column name of the values ​​is valid
    value_column = simpledialog.askstring("Choisir la colonne des valeurs", "Entrez le nom de la colonne des valeurs :")
    if value_column not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{value_column}' n'existe pas dans le fichier CSV.")
        return

    # Create the violin diagram
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=category_column, y=value_column, data=df, palette="muted")
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.title(f"Diagramme en Violon de {value_column} par {category_column}")

    plt.show()
    

def butterfly():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter column names for the butterfly chart values
    value_columns_input = simpledialog.askstring("Choisir les 2 colonnes des valeurs du papillon", "Entrez les noms des 2 colonnes des valeurs du papillon (séparés par des virgules) :")
    value_columns = [col.strip() for col in value_columns_input.split(',')]

    # Check that column names are valid
    if len(value_columns) != 2:
        messagebox.showwarning("Avertissement", "Veuillez entrer exactement deux noms de colonnes pour les valeurs du papillon.")
        return

    # Check that the columns exist in the DataFrame
    columns_exist = all(col in df.columns for col in value_columns)
    if not columns_exist:
        messagebox.showwarning("Avertissement", "Certaines colonnes spécifiées n'existent pas dans le fichier CSV.")
        return

    # Create the butterfly shape graphic
    plt.figure(figsize=(8, 6))
    plt.plot(df[value_columns[0]], label=value_columns[0])
    plt.plot(df[value_columns[1]], label=value_columns[1])
    plt.xlabel("Index")
    plt.ylabel("Valeurs")
    plt.title("Graphique en Forme de Papillon")
    plt.legend()

    plt.show()
    
    
def correlation():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    app_theme()

    if not filepath:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(filepath)

    column1 = simpledialog.askstring("Entrée", "Entrez le nom de la colonne 1 :")
    column2 = simpledialog.askstring("Entrée", "Entrez le nom de la colonne 2 :")

    if column1 not in df.columns or column2 not in df.columns:
        messagebox.showerror("Erreur", "Les noms de colonnes spécifiés ne sont pas valides.")
        return
    
    # Check that the columns are numeric
    if not pd.api.types.is_numeric_dtype(df[column1]) or not pd.api.types.is_numeric_dtype(df[column2]):
        messagebox.showerror("Erreur", "Les colonnes sélectionnées ne contiennent pas de données numériques.")
        return

    # Calculate the correlation between columns
    correlation_value = df[column1].corr(df[column2])

    # Display Correlation
    messagebox.showinfo("Corrélation", f"La corrélation entre '{column1}' et '{column2}' est : {correlation_value:.2f}")

    # Plot the correlation graph
    plt.scatter(df[column1], df[column2])
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f"Corrélation entre {column1} et {column2}")
    
    plt.show()
    

def stem_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to select the column of values ​​to display in the stem chart
    value_column = df.columns[0] # By default, selects the first column

    if len(df.columns) > 1:
        value_column = simpledialog.askstring("Choisir la colonne des valeurs", "Choisissez la colonne des valeurs à afficher :")

        if value_column not in df.columns:
            messagebox.showwarning("Avertissement", f"La colonne '{value_column}' n'existe pas dans le fichier CSV.")
            return

    # Create the stem diagram
    plt.stem(df.index, df[value_column], markerfmt='bo', basefmt=" ", linefmt='b-')
    plt.xlabel("Index")
    plt.ylabel(value_column)
    plt.title(f"Diagramme en Tige de {value_column}")

    plt.show()
    
    
def density_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to select the column of values ​​to display in the density graph
    value_column = df.columns[0]  # By default, selects the first column

    if len(df.columns) > 1:
        value_column = simpledialog.askstring("Choisir la colonne des valeurs", "Choisissez la colonne des valeurs à afficher :")

        if value_column not in df.columns:
            messagebox.showwarning("Avertissement", f"La colonne '{value_column}' n'existe pas dans le fichier CSV.")
            return

    # Create the density graph
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df[value_column], shade=True, color="b")
    plt.xlabel(value_column)
    plt.ylabel("Densité")
    plt.title(f"Graphique de Densité de {value_column}")

    plt.show()
    
    
def distribution():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to select the column of values ​​to display in the distribution graph
    value_column = df.columns[0] # By default, selects the first column

    if len(df.columns) > 1:
        value_column = simpledialog.askstring("Choisir la colonne des valeurs", "Choisissez la colonne des valeurs à afficher :")

        if value_column not in df.columns:
            messagebox.showwarning("Avertissement", f"La colonne '{value_column}' n'existe pas dans le fichier CSV.")
            return

    # Create the distribution graph
    plt.figure(figsize=(10, 6))
    sns.histplot(df[value_column], kde=True, color="b")
    plt.xlabel(value_column)
    plt.ylabel("Fréquence")
    plt.title(f"Graphique de Distribution de {value_column}")

    plt.show()
    

def categorical():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Ask user to select categorical column
    category_column = simpledialog.askstring("Choisir la colonne catégorielle", "Choisissez la colonne catégorielle à afficher :")

    if category_column not in df.columns:
        messagebox.showwarning("Avertissement", f"La colonne '{category_column}' n'existe pas dans le fichier CSV.")
        return

    # Create the categorical variable graph
    plt.figure(figsize=(10, 6))
    sns.countplot(x=category_column, data=df, palette="Set3")
    plt.xlabel(category_column)
    plt.ylabel("Comptage")
    plt.title(f"Graphique de Variables Catégorielles pour {category_column}")
    plt.xticks(rotation=45)
    
    plt.show()
    
    
def clusters():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)

    # Create a data matrix for clustering
    data = df.to_numpy()

    # Calculate linkage matrix for clustering
    linkage_matrix = hierarchy.linkage(data, method='ward')

    # Create the dendrogram
    plt.figure(figsize=(10, 6))
    dendrogram = hierarchy.dendrogram(linkage_matrix, labels=df.index, orientation='top')
    plt.xlabel("Échantillons")
    plt.ylabel("Distance de Ward")
    plt.title("Dendrogramme de Clustering")
    plt.xticks(rotation=90)
    
    plt.show()


if __name__ == '__main__':
    graphic_main()