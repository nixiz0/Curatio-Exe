import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os
import os.path
from tkinter import filedialog, messagebox, simpledialog
import dask.dataframe as dd
from prettytable import PrettyTable

from ressources.main_functions.line_col import *
from ressources.main_functions.order import *
from ressources.main_functions.missing_val import *
from ressources.main_functions.transfo_var import *
from ressources.graphic_tool.graphic_tool import graphic_main
from ressources.statistic_tool.statistic_tool import statistic_main
from ressources.scraper_tool.scrap_tool import scraper_main
from ressources.type_converter_tool.type_converter_tool import type_converter_main
from ressources.automate_exploratory.auto_report import *
from ressources.converter.converter import *


LABEL_PARAMS = {
    "activebackground":"#f9f9f9",
    "anchor":"w",
    "bg":"#444444",
    "disabledforeground":"#a3a3a3",
    "font":"-family {Impact} -size 26 -underline 1",
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
    "font":"-family {Inter} -size 15 -weight bold",
    "fg":"#f3f3f3",
    "highlightbackground":"#d9d9d9",
    "highlightcolor":"black",
}

class Curatio(tk.Tk):
    def __init__(self):
        super().__init__()
        # Icon in bar Windows
        self.iconbitmap('./ressources/bitmap_curatio.ico')
        self.protocol('WM_DELETE_WINDOW' , self.destroy)
        self.minsize(980, 650)
        
        self.title("Curatio App")
        self.configure(background="#444444")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

        self.menubar = tk.Menu(self,font="TkMenuFont",bg='#cdcdcd',fg="#000000")
        self.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(self.menubar, activebackground='#999999'
                ,activeborderwidth=1, activeforeground='#f7f7f7'
                ,background='#5f5f5f', borderwidth=1, disabledforeground='#a3a3a3'
                ,font="-family {Constantia} -size 10 -weight bold"
                ,foreground='#eeeeee', tearoff=0)
        self.menubar.add_cascade(compound='left', label='File'
                ,menu=self.sub_menu, )
        self.sub_menu.add_command(command=lambda: open_csv(self)
                ,compound='left', label='Open CSV')
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
        self.menubar.add_command(label='Graphic', command=graphic_tool)
        self.menubar.add_cascade(compound='left', label='Converter'
                ,menu=self.sub_menu1, )
        self.sub_menu1.add_command(command=self.main_sql_csv
                ,compound='left', label='SQL --> CSV')
        self.sub_menu1.add_command(command=self.main_xlsx_csv
                ,compound='left', label='XLSX --> CSV')
        self.sub_menu1.add_command(command=self.main_csv_sql
                ,compound='left', label='CSV --> SQL')
        self.sub_menu1.add_command(command=self.main_csv_xlsx
                ,compound='left', label='CSV --> XLSX')
        self.menubar.add_command(command=type_converter_tool
                ,compound='left', label='Type-Converter')
        self.menubar.add_command(command=scraper_tool
                ,compound='left', label='Scrapper')
        
        # IMG Label Line & Col
        image = tk.PhotoImage(file="./ressources/tableur_logo.png")
        self.label_line_col = tk.Label(self, image=image, **LABEL_PARAMS, compound='left', text='''Lines & Columns''')
        self.label_line_col.image = image
        self.label_line_col.grid(row=0, column=0, padx=(10, 0), pady=10, sticky='nsew', columnspan=3)

        # IMG Btn del
        image_del = tk.PhotoImage(file="./ressources/del_logo.png")
        self.btn_del_col = tk.Button(self, image=image_del, command=self.main_del_column, text='''Column''', **BTN_PARAMS)
        self.btn_del_col.image = image_del
        self.btn_del_col.grid(row=1, column=0, padx=(10, 5), pady=(0, 10), sticky='nsew')
        self.btn_del_line = tk.Button(self, image=image_del, command=self.main_del_line, text='''Line''', **BTN_PARAMS)
        self.btn_del_line.image = image_del
        self.btn_del_line.grid(row=2, column=0, padx=(10, 5), pady=(0, 10), sticky='nsew')

        # IMG Btn add
        image_add = tk.PhotoImage(file="./ressources/add_logo.png")
        self.btn_add_col = tk.Button(self, image=image_add, command=self.main_add_column, text='''Column''', **BTN_PARAMS)
        self.btn_add_col.image = image_add
        self.btn_add_col.grid(row=1, column=1, padx=(5, 10), pady=(0, 10), sticky='nsew')
        self.btn_add_line = tk.Button(self, image=image_add, command=self.main_add_line, text='''Line''', **BTN_PARAMS)
        self.btn_add_line.image = image_add
        self.btn_add_line.grid(row=2, column=1, padx=(5, 10), pady=(0, 10), sticky='nsew')

        # IMG Btn modify
        image_modify = tk.PhotoImage(file="./ressources/modify_logo.png")
        self.btn_modif_col = tk.Button(self, image=image_modify, command=self.main_modify_column, text='''Column ''', **BTN_PARAMS)
        self.btn_modif_col.image = image_modify
        self.btn_modif_col.grid(row=1, column=2, padx=(5, 10), pady=(0, 10), sticky='nsew')
        self.btn_modif_line = tk.Button(self, image=image_modify, command=self.main_modify_line, text='''Line''', **BTN_PARAMS)
        self.btn_modif_line.image = image_modify
        self.btn_modif_line.grid(row=2, column=2, padx=(5, 10), pady=(0, 10), sticky='nsew')
        
        # IMG Btn order
        image_order = tk.PhotoImage(file="./ressources/order_logo.png")
        self.btn_order = tk.Button(self, image=image_order, command=self.main_order_by, text='''Order By''', **BTN_PARAMS)
        self.btn_order.image = image_order
        self.btn_order.grid(row=3, column=0, padx=(10, 0), pady=(15, 0), sticky='nsew')
        # IMG Btn reverse order
        image_reverse_order = tk.PhotoImage(file="./ressources/reverse_order_logo.png")
        self.btn_reverse_order = tk.Button(self, image=image_reverse_order, command=self.main_reverse_order, text='''Reverse Order''', **BTN_PARAMS)
        self.btn_reverse_order.image = image_reverse_order
        self.btn_reverse_order.grid(row=3, column=1, padx=(10, 0), pady=(15, 0), sticky='nsew')
        
        self.btn_interval = tk.Button(self, text='''Interval''', command=self.main_interval_value, **BTN_PARAMS)
        self.btn_interval.grid(row=3, column=2, padx=(10, 0), pady=(15, 0), sticky='nsew')
        
        # IMG Label missing value
        image_missing_val = tk.PhotoImage(file="./ressources/missing_values.png")
        self.label_missing_val = tk.Label(self, image=image_missing_val, **LABEL_PARAMS, compound='left', text='''Missing Values''')
        self.label_missing_val.image = image_missing_val
        self.label_missing_val.grid(row=4, column=0, padx=(10, 0), pady=(25, 0), sticky='nsew', columnspan=3)

        self.btn_mean = tk.Button(self, text="Mean", command=self.main_mean, **BTN_PARAMS)
        self.btn_mean.grid(row=5, column=0, padx=(10, 0), pady=(9, 0), sticky='nsew')
        self.btn_std = tk.Button(self, text="Std", command=self.main_std_function, **BTN_PARAMS)
        self.btn_std.grid(row=6, column=0, padx=(10, 0), pady=(9, 0), sticky='nsew')
        
        self.btn_mode = tk.Button(self, text="Mode", command=self.main_mode, **BTN_PARAMS)
        self.btn_mode.grid(row=5, column=1, padx=(10, 0), pady=(9, 0), sticky='nsew')
        self.btn_median = tk.Button(self, text="Median", command=self.main_median, **BTN_PARAMS)
        self.btn_median.grid(row=6, column=1, padx=(10, 0), pady=(9, 0), sticky='nsew')
        
        self.btn_del = tk.Button(self, text="Delete", command=self.main_delete_function, **BTN_PARAMS)
        self.btn_del.grid(row=5, column=2, padx=(10, 0), pady=(9, 0), sticky='nsew')
        self.btn_val_def = tk.Button(self, text="Define Value", command=self.main_def_value, **BTN_PARAMS)
        self.btn_val_def.grid(row=6, column=2, padx=(10, 0), pady=(9, 0), sticky='nsew')

                
        # IMG Label transformation var
        image_transfo_var = tk.PhotoImage(file="./ressources/transfo_var.png")
        self.label_transfo_var = tk.Label(self, image=image_transfo_var, **LABEL_PARAMS, compound='left', text='''Variable Transformation''')
        self.label_transfo_var.image = image_transfo_var
        self.label_transfo_var.grid(row=7, column=0, padx=(10, 0), pady=(28, 0), sticky='nsew', columnspan=3)

        self.btn_dtypes_object = tk.Button(self, text='''dtypes Object''', command=self.main_dtypes_object, **BTN_PARAMS)
        self.btn_dtypes_object.grid(row=8, column=0, padx=(25, 0), pady=(15, 0), sticky='nsew')
        self.btn_one_hot = tk.Button(self, text='''One Hot''', command=self.main_one_hot, **BTN_PARAMS)
        self.btn_one_hot.grid(row=8, column=1, padx=(25, 0), pady=(15, 0), sticky='nsew')
        self.btn_dummies = tk.Button(self, text='''Dummies''', command=self.main_dummies, **BTN_PARAMS)
        self.btn_dummies.grid(row=9, column=0, padx=(25, 0), pady=(15, 0), sticky='nsew')
        self.btn_fusion = tk.Button(self, text='''Fusion''', command=self.main_fusion, **BTN_PARAMS)
        self.btn_fusion.grid(row=9, column=1, padx=(25, 0), pady=(15, 0), sticky='nsew')
        
        
        # IMG Label (Automate Exploratory)
        image_auto_explo = tk.PhotoImage(file="./ressources/automate_explo.png")
        self.label_auto_explo = tk.Label(self, image=image_auto_explo, **LABEL_PARAMS, compound='left', text='''Automate Exploratory''')
        self.label_auto_explo.image = image_auto_explo
        self.label_auto_explo.grid(row=0, column=3, padx=(70, 0), pady=(10, 0), sticky='nsew', columnspan=3)

        self.btn_profiling_report = tk.Button(self, text='''Profiling Report''', command=self.main_profiling_report, **BTN_PARAMS)
        self.btn_profiling_report.grid(row=1, column=3, padx=(155, 0), pady=(5, 0), sticky='nsew')
        
        self.btn_analysis_report = tk.Button(self, text='''Analysis Report''', command=self.main_analysis_report, **BTN_PARAMS)
        self.btn_analysis_report.grid(row=2, column=3, padx=(155, 0), pady=(5, 0), sticky='nsew')

        # IMG Label (Statistics)
        image_statistic = tk.PhotoImage(file="./ressources/statistic.png")
        self.label_statistic = tk.Label(self, image=image_statistic, **LABEL_PARAMS, compound='left', text='''Statistics''')
        self.label_statistic.image = image_statistic
        self.label_statistic.grid(row=4, column=3, padx=(160, 0), pady=(10, 0), sticky='nsew', columnspan=3)

        self.btn_statistic_tool = tk.Button(self, text='''Statistic-Tool''', command=statistic_tool, **BTN_PARAMS)
        self.btn_statistic_tool.grid(row=5, column=3, padx=(165, 0), pady=(5, 0), sticky='nsew')
        
    """ 
    Lines & Col Functions
    """ 
    def main_del_column(self):
        self.app_theme()
        del_column()
        
    def main_del_line(self):
        self.app_theme()
        del_line()
        
    def main_add_column(self):
        self.app_theme()
        add_column()
        
    def main_add_line(self):
        self.app_theme()
        add_line()
        
    def main_modify_column(self):
        self.app_theme()
        modify_column()
        
    def main_modify_line(self):
        self.app_theme()
        modify_line()
        
    def main_interval_value(self):
        self.app_theme()
        interval_value()
        
    """ 
    Order Functions
    """ 
    def main_order_by(self):
        self.app_theme()
        order_by()
        
    def main_reverse_order(self):
        self.app_theme()
        reverse_order()
        
    """ 
    Missing Value Functions
    """ 
    def main_mean(self):
        self.app_theme()
        mean()
        
    def main_std_function(self):
        self.app_theme()
        std_function()
        
    def main_delete_function(self):
        self.app_theme()
        delete_function()
        
    def main_def_value(self):
        self.app_theme()
        def_value()
        
    def main_mode(self):
        self.app_theme()
        mode()
        
    def main_median(self):
        self.app_theme()
        median()
        
    """ 
    Transformation Var Functions
    """ 
    def main_dtypes_object(self):
        self.app_theme()
        dtypes_object()
        
    def main_dummies(self):
        self.app_theme()
        dummies()
        
    def main_one_hot(self):
        self.app_theme()
        one_hot()
        
    def main_fusion(self):
        self.app_theme()
        fusion()
        
    """ 
    Converter Functions
    """ 
    def main_sql_csv(self):
        self.app_theme()
        sql_csv()
        
    def main_xlsx_csv(self):
        self.app_theme()
        xlsx_csv()
        
    def main_csv_sql(self):
        self.app_theme()
        csv_sql()
        
    def main_csv_xlsx(self):
        self.app_theme()
        csv_xlsx()
                
    """ 
    Auto Exploratory Function
    """ 
    def main_profiling_report(self):
        self.app_theme()
        profiling_report()
        
    def main_analysis_report(self):
        self.app_theme()
        analysis_report()
        
        
    def app_theme(self:tk.Tk|tk.Frame):
        self.tk_setPalette(background='#444444', foreground='white')
        
    def maximize_window(self):
        self.state('zoomed')
        
    def run(self):
        self.maximize_window()
        self.mainloop()
        

"""
########################################################
################ FUNCTIONS & Main ################
########################################################
"""
def on_exit(icon):
    icon.stop()

def main():
    app_run = Curatio()
    app_run.run()
    
def graphic_tool():
    graphic_main()
    
def statistic_tool():
    statistic_main()
    
def scraper_tool():
    scraper_main()
        
def type_converter_tool():
    type_converter_main()

# Function to highlight keywords in a Text widget
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


def toggle_pin(window, pin_button, pinned_var):
    if window.attributes('-topmost'):
        window.attributes('-topmost', 0)
        pinned_var.set("   Pin   ")
    else:
        window.attributes('-topmost', 1)
        pinned_var.set("  Unpin  ")
        
open_windows = []
def open_csv(self:tk.Tk):
    global open_windows
    # Close all previously opened windows
    for window in open_windows:
        window.destroy()
    open_windows = []  # Reset the list of open windows

    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    if file_path:
        self.app_theme()
        # Ask the user to select a separator
        separator_choice = simpledialog.askstring("Select Separator", "Enter 1: \\t (tab) \nEnter 2: , (comma) \nEnter 3: ; (semicolon) \nOr leave empty for no separator")

        if separator_choice == "1":
            separator = "\t"
        elif separator_choice == "2":
            separator = ","
        elif separator_choice == "3":
            separator = ";"
        else:
            separator = None

        # Read the CSV using Dask with the selected separator or no separator
        if separator is not None:
            # Specify dtype for the 'code' column as 'object'
            dask_df = dd.read_csv(file_path, sep=separator, dtype={'code': 'object'})
        else:
            # Specify dtype for the 'code' column as 'object'
            dask_df = dd.read_csv(file_path, dtype={'code': 'object'})

        # Convert the Dask DataFrame to a Pandas DataFrame for displaying in a Text widget
        pd_df = dask_df.compute()

        # Create a window to display the Pandas DataFrame
        table_window = tk.Toplevel()
        table_window.title("Your CSV File: " + str(os.path.basename(file_path)))
        open_windows.append(table_window)

        # Set the position of the window on the right side of the screen
        window_width = 780  # Set your desired width
        window_height = 550  # Set your desired height
        screen_width = table_window.winfo_screenwidth()
        screen_height = table_window.winfo_screenheight()
        x = screen_width - window_width - 70
        y = (screen_height - window_height) // 2 - 200
        table_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        text_frame = ttk.Frame(table_window)
        text_frame.pack(expand=True, fill="both")

        # Add a vertical scrollbar
        text_widget = tk.Text(text_frame, wrap="none", bg="#2b2b2b", fg="white")
        y_scrollbar = ttk.Scrollbar(text_frame, command=text_widget.yview)
        y_scrollbar.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=y_scrollbar.set)

        text_widget.pack(expand=True, fill="both")

        # Convert the Pandas DataFrame to PrettyTable with left alignment
        table = PrettyTable()
        for col in pd_df.columns:
            table.add_column(col, pd_df[col].values, align='l')

        table_str = table.get_string()
        text_widget.insert(tk.END, table_str)

        x_scrollbar = ttk.Scrollbar(table_window, orient="horizontal", command=text_widget.xview)
        x_scrollbar.pack(side="bottom", fill="x")
        text_widget.config(xscrollcommand=x_scrollbar.set)

        def on_find():
            keyword = find_entry.get().strip()
            if keyword:
                find_and_highlight(text_widget, keyword)
                
        style = ttk.Style()
        style.configure("Custom.TLabel", background="#444444", foreground="white", font="-family {Impact} -size 14")
        style.configure("Custom.TButton", background="#444444", foreground="black")

        find_frame = ttk.Frame(table_window, style="Custom.TLabel")
        find_frame.pack(side=tk.TOP, padx=10, pady=5)

        find_label = ttk.Label(find_frame, text="Search-Bar  : ", style="Custom.TLabel")
        find_label.pack(side=tk.LEFT)

        find_entry = ttk.Entry(find_frame)
        find_entry.pack(side=tk.LEFT, padx=5)

        find_button = ttk.Button(find_frame, text="Search", command=on_find, style="Custom.TButton")
        find_button.pack(side=tk.LEFT, padx=5)

        text_widget.tag_configure("highlight", background="cyan", foreground="black")

        # Create a window to display information about the CSV file
        info_window = tk.Toplevel()
        info_window.title("CSV File Information")
        open_windows.append(info_window)
        
        # Set the position of the window on the left side of the screen
        info_window_width = 430  # Set your desired width
        info_window_height = 550  # Set your desired height
        screen_width = info_window.winfo_screenwidth()
        screen_height = info_window.winfo_screenheight()
        x = 50
        y = (screen_height - info_window_height) // 2 - 200
        info_window.geometry(f"{info_window_width}x{info_window_height}+{x}+{y}")

        info_text_widget = tk.Text(info_window, wrap="word", bg="#2b2b2b", fg="white")
        info_text_widget.pack(expand=True, fill="both")

        info_text_widget.insert(tk.END, "Number of Lines:\n")
        info_text_widget.insert(tk.END, str(len(pd_df)))
        info_text_widget.insert(tk.END, "\nNumber of Columns:\n")
        info_text_widget.insert(tk.END, str(len(pd_df.columns)))

        # Calculate missing values using Dask and display
        missing_values = dask_df.isnull().sum().compute()
        info_text_widget.insert(tk.END, "\n\nMissing Values:\n")
        info_text_widget.insert(tk.END, str(missing_values))

        # Calculate columns with 'object' data types using Dask and display
        object_dtypes = dask_df.select_dtypes(include='object').dtypes
        info_text_widget.insert(tk.END, "\n\nColumns with 'object' dtype:\n")
        info_text_widget.insert(tk.END, str(object_dtypes))

        pinned_var = tk.StringVar()
        pinned_var.set("  Unpin  ")

        toggle_pin(table_window, None, pinned_var)  # Pin the windows by default
        pin_button = tk.Button(table_window, textvariable=pinned_var, command=lambda: toggle_pin(table_window, pin_button, pinned_var))
        pin_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        pinned_var_info = tk.StringVar()
        pinned_var_info.set("   Pin   ")

        pin_button = tk.Button(info_window, textvariable=pinned_var_info, command=lambda: toggle_pin(info_window, pin_button, pinned_var_info))
        pin_button.pack(side=tk.BOTTOM, padx=10, pady=10)
        
        
if __name__ == '__main__':
    main()