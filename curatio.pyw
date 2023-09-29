import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os
import os.path
import subprocess
import platform
import csv
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from tkinter import filedialog, messagebox, simpledialog
import requests
import re
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

from ressources.graphic_tool.graphic_tool import graphic_main


_script = sys.argv[0]
_location = os.path.dirname(_script)

LABEL_PARAMS = {
    "activebackground":"#f9f9f9",
    "anchor":"w",
    "bg":"#444444",
    "disabledforeground":"#a3a3a3",
    "font":"-family {Impact} -size 22 -underline 1",
    "fg":"#ffffff",
    "highlightbackground":"#d9d9d9",
    "highlightcolor":"black",
}

BTN_PARAMS = {
    "activebackground":"#c0c0c0",
    "activeforeground":"#161616",
    "bg":"#818181",
    "compound":"left",
    "disabledforeground":"#a3a3a3",
    "font":"-family {Inter} -size 12 -weight bold",
    "fg":"#f3f3f3",
    "highlightbackground":"#d9d9d9",
    "highlightcolor":"black",
}

class Curatio:
    def __init__(self, top=None):
        top.geometry("974x465+451+105")
        top.minsize(880, 500)
        top.maxsize(1200, 620)
        top.title("Curatio App")
        top.configure(background="#444444")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#cdcdcd',fg="#000000")
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(self.menubar, activebackground='#999999'
                ,activeborderwidth=1, activeforeground='#f7f7f7'
                ,background='#5f5f5f', borderwidth=1, disabledforeground='#a3a3a3'
                ,font="-family {Constantia} -size 10 -weight bold"
                ,foreground='#eeeeee', tearoff=0)
        self.menubar.add_cascade(compound='left', label='Fichier'
                ,menu=self.sub_menu, )
        self.sub_menu.add_command(command=menu_open_csv
                ,compound='left', label='Ouvrir CSV')
        self.sub_menu0 = tk.Menu(self.menubar, activebackground='#999999'
                ,activeborderwidth=1, activeforeground='#f7f7f7'
                ,background='#5f5f5f', borderwidth=1, disabledforeground='#a3a3a3'
                ,font="-family {Constantia} -size 10 -weight bold"
                ,foreground='#eeeeee', tearoff=0)
        self.sub_menu1 = tk.Menu(self.menubar, activebackground='#999999'
                ,activeborderwidth=1, activeforeground='#f7f7f7'
                ,background='#5f5f5f', borderwidth=1, disabledforeground='#a3a3a3'
                ,font="-family {Constantia} -size 10 -weight bold"
                ,foreground='#eeeeee', tearoff=0)
        self.sub_menu2 = tk.Menu(self.menubar, activebackground='#999999'
                ,activeborderwidth=1, activeforeground='#f7f7f7'
                ,background='#5f5f5f', borderwidth=1, disabledforeground='#a3a3a3'
                ,font="-family {Constantia} -size 10 -weight bold"
                ,foreground='#eeeeee', tearoff=0)
        self.menubar.add_command(label='Graphique', command=graphic_tool)
        self.menubar.add_cascade(compound='left', label='Convertisseur'
                ,menu=self.sub_menu1, )
        self.sub_menu1.add_command(command=sql_csv
                ,compound='left', label='SQL --> CSV')
        self.sub_menu1.add_command(command=xlsx_csv
                ,compound='left', label='XLSX --> CSV')
        self.sub_menu1.add_command(command=csv_sql
                ,compound='left', label='CSV --> SQL')
        self.sub_menu1.add_command(command=csv_xlsx
                ,compound='left', label='CSV --> XLSX')
        self.menubar.add_cascade(compound='left', label='Types'
                ,menu=self.sub_menu2, )
        self.sub_menu2.add_command(command=type_converter
                ,compound='left', label='Convertir Type')
        self.menubar.add_command(command=open_scrapper
                ,compound='left', label='Scrapper')
        # IMG logo integration
        image = tk.PhotoImage(file="./ressources/tableur_logo.png")
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.01, rely=0.019, height=34, width=250)
        self.Label1.configure(**LABEL_PARAMS)
        self.Label1.configure(compound='left')
        self.Label1.configure(text='''Ligne & Colonne''')
        self.Label1.configure(image=image)
        self.Label1.image = image
        # IMG logo integration
        image_del = tk.PhotoImage(file="./ressources/del_logo.png")
        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.021, rely=0.114, height=34, width=116)
        self.Button1.configure(**BTN_PARAMS)
        self.Button1.configure(command=del_colonne)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Colonne''')
        self.Button1.configure(image=image_del)
        self.Button1.image = image_del
        self.Button1_1 = tk.Button(self.top)
        self.Button1_1.place(relx=0.021, rely=0.189, height=34, width=116)
        self.Button1_1.configure(**BTN_PARAMS)
        self.Button1_1.configure(command=del_ligne)
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Ligne''')
        self.Button1_1.configure(image=image_del)
        self.Button1_1.image = image_del
        # IMG logo integration
        image_add = tk.PhotoImage(file="./ressources/add_logo.png")
        self.Button1_2 = tk.Button(self.top)
        self.Button1_2.place(relx=0.164, rely=0.114, height=34, width=116)
        self.Button1_2.configure(**BTN_PARAMS)
        self.Button1_2.configure(command=add_colonne)
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Colonne''')
        self.Button1_2.configure(image=image_add)
        self.Button1_2.image = image_add
        self.Button1_2_1 = tk.Button(self.top)
        self.Button1_2_1.place(relx=0.164, rely=0.189, height=34, width=116)
        self.Button1_2_1.configure(**BTN_PARAMS)
        self.Button1_2_1.configure(command=add_ligne)
        self.Button1_2_1.configure(pady="0")
        self.Button1_2_1.configure(text='''Ligne''')
        self.Button1_2_1.configure(image=image_add)
        self.Button1_2_1.image = image_add
        # IMG logo integration
        image_modify = tk.PhotoImage(file="./ressources/modify_logo.png")
        self.Button1_2_2 = tk.Button(self.top)
        self.Button1_2_2.place(relx=0.308, rely=0.114, height=34, width=136)
        self.Button1_2_2.configure(**BTN_PARAMS)
        self.Button1_2_2.configure(command=modify_colonne)
        self.Button1_2_2.configure(pady="0")
        self.Button1_2_2.configure(text='''Colonne''')
        self.Button1_2_2.configure(image=image_modify)
        self.Button1_2_2.image = image_modify
        self.Button1_2_2_1 = tk.Button(self.top)
        self.Button1_2_2_1.place(relx=0.308, rely=0.189, height=34, width=136)
        self.Button1_2_2_1.configure(**BTN_PARAMS)
        self.Button1_2_2_1.configure(command=modify_ligne)
        self.Button1_2_2_1.configure(pady="0")
        self.Button1_2_2_1.configure(text='''Ligne''')
        self.Button1_2_2_1.configure(image=image_modify)
        self.Button1_2_2_1.image = image_modify
        # IMG logo integration
        image_order = tk.PhotoImage(file="./ressources/order_logo.png")
        self.Button1_2_2_1_1 = tk.Button(self.top)
        self.Button1_2_2_1_1.place(relx=0.021, rely=0.323, height=34, width=116)
        self.Button1_2_2_1_1.configure(**BTN_PARAMS)
        self.Button1_2_2_1_1.configure(command=order_by)
        self.Button1_2_2_1_1.configure(pady="0")
        self.Button1_2_2_1_1.configure(text='''Order By''')
        self.Button1_2_2_1_1.configure(image=image_order)
        self.Button1_2_2_1_1.image = image_order
        # IMG logo integration
        image_reverse_order = tk.PhotoImage(file="./ressources/reverse_order_logo.png")
        self.Button1_2_2_1_1_1 = tk.Button(self.top)
        self.Button1_2_2_1_1_1.place(relx=0.164, rely=0.325, height=34
                , width=160)
        self.Button1_2_2_1_1_1.configure(**BTN_PARAMS)
        self.Button1_2_2_1_1_1.configure(command=reverse_order)
        self.Button1_2_2_1_1_1.configure(pady="0")
        self.Button1_2_2_1_1_1.configure(text='''Reverse Order''')
        self.Button1_2_2_1_1_1.configure(image=image_reverse_order)
        self.Button1_2_2_1_1_1.image = image_reverse_order
        self.btn = tk.Button(self.top)
        self.btn.place(relx=0.350, rely=0.325, height=34
                , width=120)
        self.btn.configure(**BTN_PARAMS)
        self.btn.configure(command=interval_value)
        self.btn.configure(pady="0")
        self.btn.configure(text='''Intervalle''')
        # IMG logo integration
        image1 = tk.PhotoImage(file="./ressources/valeur_manquante.png")
        self.Label1_1 = tk.Label(self.top)
        self.Label1_1.place(relx=0.01, rely=0.419, height=34, width=260)
        self.Label1_1.configure(**LABEL_PARAMS)
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(text='''Valeur Manquante''')
        self.Label1_1.configure(image=image1)
        self.Label1_1.image = image1
        self.Button1_3 = tk.Button(self.top)
        self.Button1_3.place(relx=0.021, rely=0.514, height=34, width=116)
        self.Button1_3.configure(**BTN_PARAMS)
        self.Button1_3.configure(command=moyenne)
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Moyenne''')
        self.Button1_3_1 = tk.Button(self.top)
        self.Button1_3_1.place(relx=0.164, rely=0.514, height=34, width=116)
        self.Button1_3_1.configure(**BTN_PARAMS)
        self.Button1_3_1.configure(command=supprimer)
        self.Button1_3_1.configure(pady="0")
        self.Button1_3_1.configure(text='''Supprimer''')
        self.Button1_3_1_1 = tk.Button(self.top)
        self.Button1_3_1_1.place(relx=0.021, rely=0.589, height=34, width=116)
        self.Button1_3_1_1.configure(**BTN_PARAMS)
        self.Button1_3_1_1.configure(command=ecart_type)
        self.Button1_3_1_1.configure(pady="0")
        self.Button1_3_1_1.configure(text='''Écart-Type''')
        self.Button1_3_1_2 = tk.Button(self.top)
        self.Button1_3_1_2.place(relx=0.164, rely=0.589, height=34, width=116)
        self.Button1_3_1_2.configure(**BTN_PARAMS)
        self.Button1_3_1_2.configure(command=valeur_def)
        self.Button1_3_1_2.configure(pady="0")
        self.Button1_3_1_2.configure(text='''Valeur Definir''')
        # IMG logo integration
        image2 = tk.PhotoImage(file="./ressources/transfo_var.png")
        self.Label1_1_1 = tk.Label(self.top)
        self.Label1_1_1.place(relx=0.01, rely=0.686, height=34, width=340)
        self.Label1_1_1.configure(**LABEL_PARAMS)
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(text='''Transformation Variables''')
        self.Label1_1_1.configure(image=image2)
        self.Label1_1_1.image = image2
        self.Button1_2_2_1_1_2 = tk.Button(self.top)
        self.Button1_2_2_1_1_2.place(relx=0.021, rely=0.781, height=34
                , width=146)
        self.Button1_2_2_1_1_2.configure(**BTN_PARAMS)
        self.Button1_2_2_1_1_2.configure(command=dtypes_object)
        self.Button1_2_2_1_1_2.configure(pady="0")
        self.Button1_2_2_1_1_2.configure(text='''dtypes Object''')
        self.Button1_2_2_1_1_2_1 = tk.Button(self.top)
        self.Button1_2_2_1_1_2_1.place(relx=0.195, rely=0.781, height=34
                , width=126)
        self.Button1_2_2_1_1_2_1.configure(**BTN_PARAMS)
        self.Button1_2_2_1_1_2_1.configure(command=one_hot)
        self.Button1_2_2_1_1_2_1.configure(pady="0")
        self.Button1_2_2_1_1_2_1.configure(text='''One Hot''')
        self.Button1_2_2_1_1_2_1_1 = tk.Button(self.top)
        self.Button1_2_2_1_1_2_1_1.place(relx=0.021, rely=0.858, height=34
                , width=146)
        self.Button1_2_2_1_1_2_1_1.configure(**BTN_PARAMS)
        self.Button1_2_2_1_1_2_1_1.configure(command=dummies)
        self.Button1_2_2_1_1_2_1_1.configure(pady="0")
        self.Button1_2_2_1_1_2_1_1.configure(text='''dummies''')
        self.Button1_2_2_1_1_2_1_2 = tk.Button(self.top)
        self.Button1_2_2_1_1_2_1_2.place(relx=0.195, rely=0.858, height=34
                , width=126)
        self.Button1_2_2_1_1_2_1_2.configure(**BTN_PARAMS)
        self.Button1_2_2_1_1_2_1_2.configure(command=replace)
        self.Button1_2_2_1_1_2_1_2.configure(pady="0")
        self.Button1_2_2_1_1_2_1_2.configure(text='''Fusion''')
        self.Button1_2_2_1_1_2_1_3 = tk.Button(self.top)
        self.Button1_2_2_1_1_2_1_3.place(relx=0.708, rely=0.858, height=34, width=126)
        self.Button1_2_2_1_1_2_1_3.configure(**BTN_PARAMS)
        self.Button1_2_2_1_1_2_1_3.configure(command=lambda: open_csv(self))
        self.Button1_2_2_1_1_2_1_3.configure(pady="0")
        self.Button1_2_2_1_1_2_1_3.configure(text='''Ouvrir Fichier''')
        self.Text1 = tk.Text(self.top)
        self.Text1.place(relx=0.554, rely=0.019, relheight=0.806, relwidth=0.433)
        self.Text1.configure(background="#2b2b2b")
        self.Text1.configure(borderwidth="2")
        self.Text1.configure(highlightbackground="#4a4a4a")
        self.Text1.configure(highlightcolor="#d8d8d8")
        self.Text1.configure(insertbackground="#d8d8d8")
        self.Text1.configure(relief="flat")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(font="Helvetica", foreground="#EFEFEF")
        
        scrollbar = tk.Scrollbar(self.top, command=self.Text1.yview)
        scrollbar.place(relx=0.980, rely=0.019, relheight=0.806)
        self.Text1.configure(yscrollcommand=scrollbar.set)
        
        # Bind CTRL-F to search for text
        self.Text1.bind("<Control-f>", self.search_text)

    def search_text(self, event):
        search_window = tk.Toplevel(self.top)
        search_window.title("CTRL-F Advanced Search")
        search_window.configure(background="#333333")
        search_window.geometry("300x80")
    
        search_label = ttk.Label(search_window, text="Search Text:", background="#333333", foreground="#ffffff")
        search_label.pack()
    
        search_entry = ttk.Entry(search_window, width=30)
        search_entry.pack()
        search_entry.focus_set()
    
        def find_text():
            search_term = search_entry.get()
            if search_term:
                # Clear previous search tags
                self.Text1.tag_remove("search", "1.0", "end")
    
                text = self.Text1.get("1.0", "end")
                start_index = "1.0"
                while True:
                    index = self.Text1.search(search_term, start_index, stopindex="end", nocase=1)
                    if index:
                        end_index = f"{index}+{len(search_term)}c"
                        self.Text1.tag_add("search", index, end_index)
                        self.Text1.tag_configure("search", background="blue")
                        start_index = end_index
                    else:
                        break

        search_button = ttk.Button(search_window, text="Find", command=find_text)
        search_button.pack()

        search_window.bind("<Return>", lambda event: find_text())




"""
########################################################
################ FUNCTIONS TOOLS & Main ################
########################################################
"""
def on_exit(icon, item):
    icon.stop()

def main(*args):
    global root
    root = tk.Tk()
    # Icon in bar Windows
    root.iconbitmap('./ressources/bitmap_curatio.ico')
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = Curatio(_top1)
    root.mainloop()
    
def app_theme():
    root.tk_setPalette(background='#444444', foreground='white')
    
def menu_open_csv():
    open_csv()
    
def graphic_tool():
    graphic_main()

def sql_csv(*args):
    root = tk.Tk()
    root.withdraw()

    sql_file = filedialog.askopenfilename(filetypes=[("SQL Files", "*.sql")])
    if not sql_file:
        return

    try:
        # Establish a connection to the database (using SQLite)
        con = sqlite3.connect(":memory:")  # You may want to change the database connection string as needed
        df = pd.read_sql_query(open(sql_file, 'r', encoding='utf-8').read(), con)
        con.close()
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de lecture du fichier SQL : {e}")
        return

    csv_file_converted = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not csv_file_converted:
        return

    # Convert the DataFrame to a CSV file with the 'utf-8-sig' encoding to handle special characters
    try:
        df.to_csv(csv_file_converted, index=False, encoding="utf-8-sig")
        messagebox.showinfo("Succès", "Conversion effectuée avec succès !")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de conversion en CSV : {e}")
        return
        
def xlsx_csv(*args):
    file_path_xlsx = filedialog.askopenfilename(filetypes=[("Fichiers Excel", "*.xlsx")])
    if not file_path_xlsx:
        return

    try:
        df = pd.read_excel(file_path_xlsx)

        file_path_csv = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        if not file_path_csv:
            return

        # Convert and save the file to CSV with utf-8-sig encoding
        df.to_csv(file_path_csv, index=False, encoding="utf-8-sig")

        tk.messagebox.showinfo("Conversion réussie", "Le fichier a été converti avec succès en CSV.")
    except Exception as e:
        tk.messagebox.showerror("Erreur", f"Une erreur est survenue lors de la conversion : {str(e)}")
        
def csv_sql(*args):
    root = tk.Tk()
    root.withdraw()

    csv_file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not csv_file:
        return

    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de lecture du fichier CSV : {e}")
        return

    sql_file_converted = filedialog.asksaveasfilename(defaultextension=".sql", filetypes=[("SQL Files", "*.sql")])
    if not sql_file_converted:
        return

    try:
        with open(sql_file_converted, 'w', encoding='utf-8') as sql_file:
            # Assuming the table name is 'my_table', you may change this as needed
            table_name = 'my_table'
            # Generate SQL statements to create the table and insert data
            create_table_statement = df.to_sql(table_name, sqlite3.connect(":memory:"), if_exists='replace', index=False)
            insert_data_statement = f"INSERT INTO {table_name} {df.to_string(index=False, header=False)}"
            # Write the SQL statements into the SQL file
            sql_file.write(f"{create_table_statement};\n{insert_data_statement};")
        messagebox.showinfo("Succès", "Conversion effectuée avec succès !")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de conversion en SQL : {e}")
        return
        
def csv_xlsx(*args):
    file_path_csv = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
    if not file_path_csv:
        return

    try:
        df = pd.read_csv(file_path_csv)

        file_path_xlsx = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Fichiers Excel", "*.xlsx")])
        if not file_path_xlsx:
            return

        df.to_excel(file_path_xlsx, index=False)

        messagebox.showinfo("Conversion réussie", "Le fichier a été converti avec succès en XLSX.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors de la conversion : {str(e)}")
        
def open_scrapper():
    app_theme()
    url = simpledialog.askstring("URL", "Entrez l'URL à scrapper:")

    if not url:
        messagebox.showwarning("Avertissement", "Aucune URL saisie")
        return

    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.2;) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/53.0.3631.346 Safari/536"}

    try:
        response = requests.get(url, headers=headers)

        # Parse content HTML of page
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrapes the necessary data
        scraped_data = []
        email_addresses = [] 
        for tag in soup.find_all(["a", "p", "span"]):
            scraped_data.append({
                "tag": tag.name,
                "text": tag.text.strip(),
                "href": tag.get("href", "")
            })

            # Searches for email addresses and adds them to the email list_addresses
            if tag.name not in ["script", "style"]:
                email_matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", tag.text)
                email_addresses.extend(email_matches)

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            messagebox.showerror("Erreur", "Aucun chemin saisie")
            return

        # Writes data to CSV file including email addresses
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["tag", "text", "href", "email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for item in scraped_data:
                item["email"] = ""
                writer.writerow(item)

            # Adds the extracted email addresses to the CSV file
            for email in email_addresses:
                writer.writerow({"tag": "email", "text": email, "href": "", "email": email})

        messagebox.showinfo("Terminé", "Le scrapping est terminé et les données ont été sauvegardées dans un fichier CSV.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors du scrapping: {str(e)}")
        
def type_converter():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return
    
    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))
    
    col_names = simpledialog.askstring("Colonnes", "Entrez le nom de la ou les colonnes (séparées par des virgules):")
    if not col_names:
        messagebox.showwarning("Attention", "Vous devez entrer au moins un nom de colonne.")
        return
    
    col_names = [col.strip() for col in col_names.split(",")]
    
    invalid_cols = [col_name for col_name in col_names if col_name not in df.columns]
    if invalid_cols:
        messagebox.showerror("Erreur", f"Les colonnes suivantes ne sont pas présentes dans le fichier CSV : {', '.join(invalid_cols)}")
        return
    
    for col_name in col_names:
        data_type = simpledialog.askstring("Type de données", f"Entrez le type de données pour la colonne '{col_name}':\n"
                                                              "1: string\n"
                                                              "2: object\n"
                                                              "3: int\n"
                                                              "4: float\n"
                                                              "5: bool\n"
                                                              "6: date")
        if not data_type:
            continue
        
        if data_type == "1":
            df[col_name] = df[col_name].astype(str)
        elif data_type == "2":
            df[col_name] = df[col_name].astype(object)
        elif data_type == "3":
            df[col_name] = pd.to_numeric(df[col_name], errors='coerce', downcast='integer')
        elif data_type == "4":
            df[col_name] = pd.to_numeric(df[col_name], errors='coerce')
        elif data_type == "5":
            df[col_name] = df[col_name].astype(bool)
        elif data_type == "6":
            df[col_name] = pd.to_datetime(df[col_name], errors='coerce')
        else:
            messagebox.showwarning("Attention", f"Type de données invalide pour la colonne '{col_name}'.")
    
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
    if output_file_path:
        df.to_csv(output_file_path, index=False)
        messagebox.showinfo("Succès", "Le fichier CSV a été sauvegardé avec les modifications.")
        
def del_colonne(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return
    
    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))
    
    columns_to_delete = simpledialog.askstring("Supprimer des colonnes", "Entrez les noms des colonnes à supprimer (séparés par des virgules):")
    
    if columns_to_delete is not None:  # Check if user pressed "Cancel"
        columns_to_delete = [col.strip() for col in columns_to_delete.split(",")]
        
        # Check if all the entered column names exist in the DataFrame
        invalid_columns = [col for col in columns_to_delete if col not in df.columns]
        
        if invalid_columns:
            messagebox.showerror("Erreur", f"Les colonnes suivantes n'existent pas dans le fichier : {', '.join(invalid_columns)}")
            return
        
        df.drop(columns_to_delete, axis=1, inplace=True)
        df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
        messagebox.showinfo("Succès", "Colonnes supprimées avec succès et enregistrées dans le fichier.")
    else:
        messagebox.showwarning("Avertissement", "Aucune colonne n'a été supprimée.")
        
def del_ligne(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    # Ask the user for the range of lines to delete
    start_index = simpledialog.askinteger("Plage de suppression", "Entrer l’index de départ:")
    end_index = simpledialog.askinteger("Plage de suppression", "Entrer l’index de fin:")

    # Check if the input values are valid
    if start_index is None or end_index is None or start_index < 1 or end_index < 1 or start_index > end_index:
        messagebox.showwarning("Avertissement", "Valeurs d’entrée non valides.")
        return

    try:
        # Open the file in read mode and read its lines
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check if the provided range is valid
        if start_index > len(lines) or end_index > len(lines):
            messagebox.showwarning("Avertissement", "La plage dépasse le nombre de lignes dans le fichier.")
            return

        # Delete the lines within the specified range
        lines = lines[:start_index - 1] + lines[end_index:]

        # Save the modifications back to the original file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        messagebox.showinfo("Suppression réussie", f"Lignes {start_index} jusqu'à {end_index} a été supprimé avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite: {e}")

def add_colonne(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return
    
    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))

    columns_to_add = simpledialog.askstring("Ajouter des colonnes", "Entrez les noms des nouvelles colonnes (séparés par des virgules):")
    
    if columns_to_add is not None:
        columns_to_add = [col.strip() for col in columns_to_add.split(",")]
        for new_col in columns_to_add:
            df[new_col] = None

        df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
        messagebox.showinfo("Succès", "Colonnes ajoutées avec succès et enregistrées dans le fichier.")
    else:
        messagebox.showwarning("Avertissement", "L'utilisateur n'a pas entré de nouvelles colonnes.")

def add_ligne(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))

    columns = df.columns.tolist()
    columns_to_add_values = simpledialog.askstring("Colonnes pour ajouter des valeurs", "Entrez les noms des colonnes pour ajouter des valeurs (séparés par des virgules):")

    if columns_to_add_values is not None:
        # Split the input string into a list of column names, strip whitespace, and filter valid column names
        columns_to_add_values = [col.strip() for col in columns_to_add_values.split(",") if col.strip() in columns]
    else:
        # Handle the case where the user cancels the dialog
        columns_to_add_values = []

    if not columns_to_add_values:
        messagebox.showwarning("Avertissement", "Aucune colonne valide n'a été spécifiée pour ajouter des valeurs.")
        return

    index_interval = simpledialog.askstring("Intervalle d'index", "Entrez l'intervalle d'index (séparé par un tiret '-'):")
    start_index, end_index = map(int, index_interval.split('-'))

    if start_index < 0 or end_index >= len(df):
        messagebox.showerror("Erreur", "Intervalle d'index invalide.")
        return

    new_data = {}
    for col in columns_to_add_values:
        new_value_input = simpledialog.askstring("Nouvelle valeur", f"Entrez la valeur pour la colonne '{col}':")
        new_value = new_value_input.strip()

        if new_value is None:
            new_value = ""  # Use an empty string for non-numeric values

        new_data[col] = [new_value] * (end_index - start_index + 1)

    new_df = pd.DataFrame(new_data)

    for col in columns_to_add_values:
        df.loc[start_index:end_index, col] = new_df[col].values

    df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
    messagebox.showinfo("Succès", "Lignes ajoutées avec succès et enregistrées dans le fichier.")
        
def modify_colonne(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))

    column_to_modify = simpledialog.askstring("Modifier le nom d'une colonne", "Entrez le nom de la colonne à modifier :")
    if column_to_modify:
        if column_to_modify in df.columns:
            new_column_name = simpledialog.askstring("Modifier le nom de la colonne", f"Entrez le nouveau nom pour la colonne '{column_to_modify}':")
            if new_column_name:
                df.rename(columns={column_to_modify: new_column_name}, inplace=True)
                df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
                messagebox.showinfo("Succès", "Nom de colonne modifié avec succès et enregistré dans le fichier.")
            else:
                messagebox.showwarning("Avertissement", "Aucun nouveau nom de colonne n'a été saisi.")
        else:
            messagebox.showerror("Erreur", f"La colonne '{column_to_modify}' n'existe pas dans le fichier.")
    else:
        messagebox.showwarning("Avertissement", "Aucune colonne n'a été sélectionnée.")

def modify_ligne(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))

    columns = df.columns.tolist()  # Convert columns to a list of column names
    column_to_modify = simpledialog.askstring("Choisir la colonne", "Entrez le nom de la colonne à modifier:")
    
    # Check if column_to_modify is None or an empty string
    if column_to_modify is None or column_to_modify.strip() == "":
        messagebox.showwarning("Avertissement", "Nom de colonne invalide ou non spécifié.")
        return

    column_to_modify = column_to_modify.strip()

    if column_to_modify not in columns:
        messagebox.showerror("Erreur", "Nom de colonne invalide.")
        return

    index_interval = simpledialog.askstring("Intervalle d'index", "Entrez l'intervalle d'index (séparé par un tiret '-'):")
    start_index, end_index = map(int, index_interval.split('-'))

    if start_index < 0 or end_index >= len(df):
        messagebox.showerror("Erreur", "Intervalle d'index invalide.")
        return

    new_value_input = simpledialog.askstring("Nouvelle valeur", f"Entrez la nouvelle valeur pour la colonne '{column_to_modify}' à l'intervalle d'index [{start_index}:{end_index}]:")
    new_value = new_value_input.strip()

    if not new_value:
        messagebox.showerror("Erreur", "Vous devez entrer une valeur pour la colonne choisie.")
        return

    df.loc[start_index:end_index, column_to_modify] = new_value

    df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
    messagebox.showinfo("Succès", "Valeurs modifiées avec succès et enregistrées dans le fichier.")
        
def order_by(*args):
    app_theme()

    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    try:
        df = pd.read_csv(file_path)
        _w1.Text1.delete(1.0, tk.END)  # Clear the Text
        _w1.Text1.insert(tk.END, df.to_csv(index=False))
    except pd.errors.EmptyDataError:
        messagebox.showerror('Erreur', "Le fichier est vide ou ne peut pas être lu.")
        return
    except Exception as e:
        messagebox.showerror('Erreur', f"Une erreur s’est produite lors de la lecture du fichier :\n{str(e)}")
        return

    # Ask the user which column they want to sort
    column_to_sort = simpledialog.askstring('Sélection de colonne', 'Saisir le nom de la colonne à trier :', parent=root)

    if column_to_sort is None:
        return

    if column_to_sort not in df.columns:
        messagebox.showerror('Erreur', 'La colonne spécifiée n’existe pas dans le fichier CSV.')
        return

    # Determine the data type of the column and sort accordingly
    column_data = df[column_to_sort]
    if pd.api.types.is_numeric_dtype(column_data):
        df[column_to_sort] = pd.to_numeric(column_data, errors='coerce')
    else:
        df[column_to_sort] = df[column_to_sort].str.lower()

    # Sort the DataFrame by the specified column in ascending order (default for text and numeric data)
    df.sort_values(by=column_to_sort, inplace=True)

    try:
        df.to_csv(file_path, index=False)
        messagebox.showinfo('Succès', 'Le fichier CSV a été trié par ordre croissant et enregistré avec succès.')
    except Exception as e:
        messagebox.showerror('Erreur', f"Une erreur s’est produite lors de l’enregistrement du fichier :\n{str(e)}")

def reverse_order(*args):
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    try:
        df = pd.read_csv(file_path)
        _w1.Text1.delete(1.0, tk.END)  # Clear the Text
        _w1.Text1.insert(tk.END, df.to_csv(index=False))
    except pd.errors.EmptyDataError:
        messagebox.showerror('Erreur', "Le fichier est vide ou ne peut pas être lu.")
        return
    except Exception as e:
        messagebox.showerror('Erreur', f"Une erreur s’est produite lors de la lecture du fichier :\n{str(e)}")
        return

    # Ask the user which column they want to sort
    column_to_sort = simpledialog.askstring('Sélection de colonne', 'Saisir le nom de la colonne à trier :', parent=root)

    if column_to_sort is None:
        return

    if column_to_sort not in df.columns:
        messagebox.showerror('Erreur', 'La colonne spécifiée n’existe pas dans le fichier CSV.')
        return

    # Determine the data type of the column and sort accordingly
    column_data = df[column_to_sort]
    if pd.api.types.is_numeric_dtype(column_data):
        df[column_to_sort] = pd.to_numeric(column_data, errors='coerce')
        # Sort the DataFrame by the specified column in descending order (reverse order for numeric data)
        df.sort_values(by=column_to_sort, ascending=False, inplace=True)
    else:
        df[column_to_sort] = df[column_to_sort].str.lower()
            
    # Sort the DataFrame by the specified column in descending order (reverse order for text data)
    df.sort_values(by=column_to_sort, ascending=False, inplace=True)

    try:
        df.to_csv(file_path, index=False)
        messagebox.showinfo('Succès', 'Le fichier CSV a été trié par ordre décroissant et enregistré avec succès.')
    except Exception as e:
        messagebox.showerror('Erreur', f"Une erreur s’est produite lors de l’enregistrement du fichier :\n{str(e)}")
        
def interval_value():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()

    try:
        df = pd.read_csv(file_path)
        _w1.Text1.delete(1.0, tk.END)  # Clear the Text
        _w1.Text1.insert(tk.END, df.to_csv(index=False))
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Fichier introuvable")
        return
    except pd.errors.EmptyDataError:
        messagebox.showerror("Erreur", "Le fichier est vide")
        return
    except pd.errors.ParserError:
        messagebox.showerror("Erreur", "Impossible de parser le fichier")
        return

    column_name = simpledialog.askstring("Entrée", "Entrez le nom de la colonne à traiter :")
    if column_name not in df.columns:
        messagebox.showerror("Erreur", f"La colonne '{column_name}' n'existe pas dans le fichier")
        return

    interval_str = simpledialog.askstring("Entrée", "Entrez l'intervalle de sélection (ex: 0:1) :")

    if not interval_str:
        messagebox.showerror("Erreur", "Intervalle invalide. Utilisez le format 'début:fin'")
        return

    interval_parts = interval_str.split(':')
    if len(interval_parts) == 1:
        start = None
        end = int(interval_parts[0])
    elif len(interval_parts) == 2:
        start = int(interval_parts[0]) if interval_parts[0] else None
        end = int(interval_parts[1]) if interval_parts[1] else None
    else:
        messagebox.showerror("Erreur", "Intervalle invalide. Utilisez le format 'début:fin'")
        return

    if start is None:
        start = 0
    if end is None:
        end = len(df[column_name])

    df[column_name] = df[column_name].apply(lambda x: x[start:end])

    output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not output_file:
        messagebox.showerror("Erreur", "Nom de fichier de sortie invalide")
        return

    try:
        df.to_csv(output_file, index=False)
        messagebox.showinfo("Succès", "Modifications sauvegardées avec succès !")
    except PermissionError:
        messagebox.showerror("Erreur", "Impossible de sauvegarder les modifications. Assurez-vous que le fichier n'est pas déjà ouvert.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde : {e}")
        
def moyenne(*args):
    file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return
    
    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))
    
    column_name = simpledialog.askstring("Moyenne des valeurs manquantes", "Entrez le nom de la colonne pour calculer la moyenne :")

    if column_name is None:
        return

    # Read the CSV file and store the data in a dictionary
    data = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key, value in row.items():
                if key in data:
                    data[key].append(value)
                else:
                    data[key] = [value]

    # Check if the column specified by the user exists
    if column_name not in data:
        messagebox.showerror("Erreur", f"Colonne '{column_name}' n’existe pas dans le fichier.")
        return

    # Check if the values in the column are numeric (integers or floating-point numbers)
    column_values = data[column_name]
    is_number_column = all(
        value is None or value.strip() == '' or value.replace(".", "").isdigit()
        for value in column_values
    )

    if not is_number_column:
        messagebox.showerror("Erreur", "Les valeurs de la colonne doivent être numériques (nombres entiers ou nombres à virgule flottante).")
        return

    # Convert the values to the appropriate type and calculate the mean
    column_values = [float(value) if value and value.strip() != '' else None for value in column_values]

    numeric_values = [value for value in column_values if value is not None]
    if numeric_values:
        mean_value = sum(numeric_values) / len(numeric_values)
    else:
        messagebox.showinfo("Information", "La colonne sélectionnée ne contient aucune valeur numérique.")
        return

    # Replace missing values with the mean
    for i in range(len(data[column_name])):
        if data[column_name][i] is None or data[column_name][i].strip() == '':
            data[column_name][i] = str(mean_value)

    new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])
    if not new_file_path:
        return

    with open(new_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        for i in range(len(data[column_name])):
            row_data = {key: data[key][i] for key in data.keys()}
            writer.writerow(row_data)

    messagebox.showinfo("Succès", f"Le fichier a été modifié et enregistré avec la moyenne des valeurs manquantes dans la '{column_name}' colonne.")

def ecart_type(*args):
    file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return
    
    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))
    
    column_name = simpledialog.askstring("Écart type des valeurs manquantes", "Entrez le nom de la colonne pour calculer l'écart type :")

    if column_name is None:
        return

    # Read the CSV file and store the data in a dictionary
    data = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key, value in row.items():
                if key in data:
                    data[key].append(value)
                else:
                    data[key] = [value]

    # Check if the column specified by the user exists
    if column_name not in data:
        messagebox.showerror("Erreur", f"Colonne '{column_name}' n’existe pas dans le fichier.")
        return

    # Check if the values in the column are numeric (integers or floating-point numbers)
    column_values = data[column_name]
    is_number_column = all(
        value is None or value.strip() == '' or value.replace(".", "").isdigit()
        for value in column_values
    )

    if not is_number_column:
        messagebox.showerror("Erreur", "Les valeurs de la colonne doivent être numériques (nombres entiers ou nombres à virgule flottante).")
        return

    # Convert the values to the appropriate type and calculate the standard deviation
    column_values = [float(value) if value and value.strip() != '' else None for value in column_values]

    numeric_values = [value for value in column_values if value is not None]
    if len(numeric_values) > 1:  # Require at least two numeric values to calculate the standard deviation
        mean_value = sum(numeric_values) / len(numeric_values)
        variance = sum((val - mean_value) ** 2 for val in numeric_values) / (len(numeric_values) - 1)
        std_deviation = math.sqrt(variance)
    else:
        messagebox.showinfo("Information", "La colonne sélectionnée ne contient pas suffisamment de valeurs numériques pour calculer l'écart type.")
        return

    # Replace missing values with the standard deviation
    for i in range(len(data[column_name])):
        if data[column_name][i] is None or data[column_name][i].strip() == '':
            data[column_name][i] = str(std_deviation)

    new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])
    if not new_file_path:
        return

    with open(new_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        for i in range(len(data[column_name])):
            row_data = {key: data[key][i] for key in data.keys()}
            writer.writerow(row_data)

    messagebox.showinfo("Succès", f"Le fichier a été modifié et enregistré avec l'écart type des valeurs manquantes dans la '{column_name}' colonne.")
        
def supprimer(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    app_theme()

    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return
    
    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de lire le fichier CSV : {e}")
        return

    column = simpledialog.askstring("Choisissez une colonne", "Saisir le nom de la colonne à traiter :")

    # Check if the column exists in the DataFrame
    if column not in df.columns:
        messagebox.showwarning("Avertissement", f"Colonne '{column}' n’existe pas dans le fichier CSV.")
        return

    # Perform the drop of fillna() to remove rows with missing values in the chosen column
    df.dropna(subset=[column], inplace=True)

    # Save the modified DataFrame to a new CSV file
    new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    # Check if a file path has been provided for saving
    if not new_file_path:
        messagebox.showwarning("Avertissement", "Aucun chemin d’enregistrement du fichier fourni.")
        return

    try:
        df.to_csv(new_file_path, index=False)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d’enregistrer le fichier CSV : {e}")
        return

    messagebox.showinfo("Opération Réussie", f"Le fichier DataFrame modifié a été enregistré dans : {new_file_path}")

def valeur_def(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showwarning("Avertissement", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))

    df = pd.read_csv(file_path)

    col_name = simpledialog.askstring("Sélectionner la colonne", "Saisir le nom de la colonne à modifier :")
    if not col_name:
        messagebox.showinfo("Info", "Nom de colonne invalide ou vide.")
        return

    # Check if the column exists in the DataFrame
    if col_name not in df.columns:
        messagebox.showinfo("Info", f"Colonne '{col_name}' n’existe pas dans le fichier.")
        return

    # Ask the user for the value to replace missing values with
    value_to_replace = simpledialog.askstring("Valeur de remplacement", "Saisir la valeur pour remplacer les valeurs manquantes :")
    if value_to_replace is None:
        messagebox.showinfo("Info", "Valeur de remplacement non valide ou vide.")
        return

    # Check the type of the column
    col_type = df[col_name].dtype
    try:
        if col_type == 'int64':
            value_to_replace = int(value_to_replace)
        elif col_type == 'float64':
            value_to_replace = float(value_to_replace)
        elif col_type == 'object':
            pass
        else:
            messagebox.showinfo("Info", f"Type de colonne non pris en charge : {col_type}.")
            return
    except ValueError:
        messagebox.showinfo("Info", f"Type de valeur de remplacement non valide pour la colonne '{col_name}'.")
        return

    # Replace missing values in the selected column
    df[col_name].fillna(value_to_replace, inplace=True)

    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not save_path:
        messagebox.showinfo("Info", "Opération annulée.")
        return

    df.to_csv(save_path, index=False)
    messagebox.showinfo("Info", "Les valeurs manquantes ont été remplacées et le nouveau fichier a été enregistré.")

def dtypes_object(*args):
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    if file_path:
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                content = "\n".join(", ".join(row) for row in csv_reader)
                _w1.Text1.delete(1.0, tk.END)  # Clear the Text
                _w1.Text1.insert(tk.END, content)

            df = pd.read_csv(file_path)  # Read CSV using pandas

            with open(file_path, newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                rows = list(csv_reader)

                # Get the maximum length of elements in each column
                col_widths = [max(len(str(rows[row_idx][col_idx])) for row_idx in range(len(rows))) for col_idx in
                            range(len(rows[0]))]

                # Format data as a table with lines and columns
                content = ""
                for row in rows:
                    content += " | ".join(f"{str(row[col_idx]):<{col_widths[col_idx]}}" for col_idx in range(len(row))) + "\n"

                # Calculate missing values and object dtypes
                object_dtypes = df.select_dtypes(include='object').dtypes

                # Create a new window to display missing values and object dtypes
                info_window = tk.Toplevel()
                info_window.title("dtypes Objects dans votre fichier CSV")

                info_text_widget = tk.Text(info_window, wrap="word", bg="#2b2b2b", fg="white")

                # Create a vertical scrollbar for the info_text_widget
                info_scrollbar = tk.Scrollbar(info_window, command=info_text_widget.yview)
                info_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                info_text_widget.configure(yscrollcommand=info_scrollbar.set)
                info_text_widget.pack(expand=True, fill="both")

                info_text_widget.insert(tk.END, "Colonnes avec dtype 'object' :\n")
                info_text_widget.insert(tk.END, str(object_dtypes))
        except ValueError:
            messagebox.showerror("Erreur", "Erreur dans l'exécution de la fonction.")

# The dummies function takes the specified column and replaces it with its dummies variables
def dummies(*args):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    app_theme()
    
    if not file_path:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")
        return
    
    # Load the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(file_path)
        _w1.Text1.delete(1.0, tk.END)  # Clear the Text
        _w1.Text1.insert(tk.END, df.to_csv(index=False))
    except Exception as e:
        messagebox.showerror("Erreur", f"Echec de lecture du fichier CSV : {str(e)}")
        return

    # Ask the user for the name of the column to process
    column_name = simpledialog.askstring("Entrée", "Entrez le nom de la colonne à traiter :")
    if not column_name:
        messagebox.showerror("Erreur", "Vous devez fournir le nom de la colonne à traiter.")
        return  # If no column name was entered, exit the function
    
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        messagebox.showerror("Erreur", f"Colonne '{column_name}' non trouvé dans le fichier CSV.")
        return

    # Check the type of the column
    column_type = df[column_name].dtype
    if column_type not in [object, str]:
        messagebox.showerror("Erreur", "Seules les colonnes de chaîne ou d'objet sont prises en charge pour la création de dummies.")
        return

    # Convert the column into dummy variables
    try:
        dummies_df = pd.get_dummies(df[column_name])
        # Drop the original column from the DataFrame
        df.drop(column_name, axis=1, inplace=True)
        # Concatenate the original DataFrame with the dummies DataFrame
        df = pd.concat([df, dummies_df], axis=1)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de créer des dummies : {str(e)}")
        return
    
    # Save the modified DataFrame back to the CSV file
    try:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Succès", f"Les valeurs de la colonne '{column_name}' ont été encodées en one hot et les modifications ont été enregistrées dans le fichier.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Échec de l'enregistrement des modifications : {str(e)}")
        return
        
# one_hot applies One Hot encoding to the entire DataFrame using the specified column name as the prefix for new generated columns.
def one_hot(*args):
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    app_theme()

    if not file_path:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")
        return

    try:
        # Load CSV file using pandas
        df = pd.read_csv(file_path)
        _w1.Text1.delete(1.0, tk.END)  # Clear the Text
        _w1.Text1.insert(tk.END, df.to_csv(index=False))
    except pd.errors.EmptyDataError:
        messagebox.showerror("Erreur", "Le fichier sélectionné est vide.")
        return
    except pd.errors.ParserError:
        messagebox.showerror("Erreur", "Impossible de lire le fichier CSV. Assurez-vous qu'il est bien formaté.")
        return

    # Request the name of the column to be processed
    column_name = simpledialog.askstring("Entrée", "Entrez le nom de la colonne à traiter :")
    if not column_name:
        messagebox.showerror("Erreur", "Vous devez fournir le nom de la colonne à traiter.")
        return

    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        messagebox.showerror("Erreur", f"La colonne '{column_name}' n'existe pas dans le fichier CSV.")
        return

    # Check the column type
    col_type = df[column_name].dtype
    if col_type not in [str, object]:
        messagebox.showerror("Erreur", "La colonne doit être de type 'string' ou 'object' pour être traitée en one hot encoding.")
        return

    # Apply One Hot Encoding to the column
    try:
        df_encoded = pd.get_dummies(df, columns=[column_name], prefix=[column_name])
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'encodage : {str(e)}")
        return

    # Save changes to CSV file
    try:
        df_encoded.to_csv(file_path, index=False)
        messagebox.showinfo("Succès", f"Les valeurs de la colonne '{column_name}' ont été encodées en one hot et les modifications ont été enregistrées dans le fichier.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'enregistrement des modifications : {str(e)}")
        
def replace(*args):
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    app_theme()
    
    if not file_path:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")
        return

    df = pd.read_csv(file_path)
    _w1.Text1.delete(1.0, tk.END)  # Clear the Text
    _w1.Text1.insert(tk.END, df.to_csv(index=False))

    col1_name = simpledialog.askstring("Noms des colonnes", "Entrez le nom de la première colonne à fusionner:")
    col2_name = simpledialog.askstring("Noms des colonnes", "Entrez le nom de la deuxième colonne à fusionner:")

    merge_col_name = simpledialog.askstring("Nom de la colonne de fusion", "Entrez le nom de la colonne de fusion:")

    if col1_name not in df.columns or col2_name not in df.columns:
        messagebox.showerror("Colonnes inexistantes", "Les noms de colonnes spécifiées n'existent pas dans le fichier.")
        return

    # Merge the specified columns and place them in the merge column
    df[merge_col_name] = df[col1_name].astype(str) + df[col2_name].astype(str)

    # Save changes to CSV file
    try:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Fusion réussie", "Les colonnes ont été fusionnées et les modifications ont été enregistrées dans le fichier.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Échec de la fusion")
        return

def open_csv(*args):
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    def find_and_highlight(text_widget, keyword):
        # Remove any existing 'highlight' tags
        text_widget.tag_remove("highlight", "1.0", tk.END)

        start_pos = "1.0"
        while True:
            start_pos = text_widget.search(keyword, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(keyword)}c"
            text_widget.tag_add("highlight", start_pos, end_pos)
            start_pos = end_pos

    if file_path:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            content = "\n".join(", ".join(row) for row in csv_reader)
            _w1.Text1.delete(1.0, tk.END)  # Clear the Text
            _w1.Text1.insert(tk.END, content)

        df = pd.read_csv(file_path)  # Read CSV using pandas

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = list(csv_reader)

            # Get the maximum length of elements in each column
            col_widths = [max(len(str(rows[row_idx][col_idx])) for row_idx in range(len(rows))) for col_idx in
                          range(len(rows[0]))]

            # Format data as a table with lines and columns
            content = ""
            for row in rows:
                content += " | ".join(f"{str(row[col_idx]):<{col_widths[col_idx]}}" for col_idx in range(len(row))) + "\n"

            table_window = tk.Toplevel()
            table_window.title("Votre fichier CSV : " + str(os.path.basename(file_path)))

            text_widget = tk.Text(table_window, wrap="none", bg="#2b2b2b", fg="white")

            # Create scrollbars for both vertical and horizontal scrolling
            y_scrollbar = tk.Scrollbar(table_window, command=text_widget.yview)
            y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            x_scrollbar = tk.Scrollbar(table_window, command=text_widget.xview, orient=tk.HORIZONTAL)
            x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            text_widget.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
            text_widget.insert(tk.END, content)

            # Calculate the total width of the horizontal bar
            total_width = sum(col_widths) + 3 * (len(rows[0]) - 1)  # Add space for separators

            text_widget.pack(expand=True, fill="both")

            def on_find():
                keyword = find_entry.get().strip()  # Remove leading and trailing spaces
                if keyword:
                    find_and_highlight(text_widget, keyword)

            find_frame = ttk.Frame(table_window)
            find_frame.pack(side=tk.TOP, padx=10, pady=5)

            find_label = ttk.Label(find_frame, text="Rechercher :")
            find_label.pack(side=tk.LEFT)

            find_entry = ttk.Entry(find_frame)
            find_entry.pack(side=tk.LEFT, padx=5)

            find_button = ttk.Button(find_frame, text="Chercher", command=on_find)
            find_button.pack(side=tk.LEFT, padx=5)

            # Add tag configuration for 'highlight' tag
            text_widget.tag_configure("highlight", background="cyan", foreground="black")

            # Calculate missing values and object dtypes
            missing_values = df.isnull().sum()
            object_dtypes = df.select_dtypes(include='object').dtypes

            # Create a new window to display missing values and object dtypes
            info_window = tk.Toplevel()
            info_window.title("Informations sur le fichier CSV")

            info_text_widget = tk.Text(info_window, wrap="word", bg="#2b2b2b", fg="white")

            # Create a vertical scrollbar for the info_text_widget
            info_scrollbar = tk.Scrollbar(info_window, command=info_text_widget.yview)
            info_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            info_text_widget.configure(yscrollcommand=info_scrollbar.set)
            info_text_widget.pack(expand=True, fill="both")

            info_text_widget.insert(tk.END, "Valeurs manquantes :\n")
            info_text_widget.insert(tk.END, str(missing_values))

            info_text_widget.insert(tk.END, "\n\nColonnes avec dtype 'object' :\n")
            info_text_widget.insert(tk.END, str(object_dtypes))
            
            
if __name__ == '__main__':
    main()