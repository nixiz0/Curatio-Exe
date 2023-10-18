from tkinter import simpledialog, filedialog, messagebox
import pandas as pd


def string_converter():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    df = pd.read_csv(file_path)
    
    col_names = simpledialog.askstring("Columns", "Enter the name of the column(s) (separated by commas) :")
    if not col_names:
        messagebox.showwarning("Attention", "You must enter at least one column name.")
        return
    
    col_names = [col.strip() for col in col_names.split(",")]
    invalid_cols = [col_name for col_name in col_names if col_name not in df.columns]
    if invalid_cols:
        messagebox.showerror("Error", f"The following columns aren't present in the CSV file : {', '.join(invalid_cols)}")
        return
    
    for col_name in col_names:
        df[col_name] = df[col_name].astype(str)
        
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
    if output_file_path:
        df.to_csv(output_file_path, index=False)
        messagebox.showinfo("Success", "The CSV file has been saved with the changes, conversion in String succeded.")
    else: 
        messagebox.showerror("Error", "The CSV file encountered an error")

    
def object_converter():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    df = pd.read_csv(file_path)
    
    col_names = simpledialog.askstring("Columns", "Enter the name of the column(s) (separated by commas) :")
    if not col_names:
        messagebox.showwarning("Attention", "You must enter at least one column name.")
        return
    
    col_names = [col.strip() for col in col_names.split(",")]
    invalid_cols = [col_name for col_name in col_names if col_name not in df.columns]
    if invalid_cols:
        messagebox.showerror("Error", f"The following columns aren't present in the CSV file : {', '.join(invalid_cols)}")
        return
    
    for col_name in col_names:
        df[col_name] = df[col_name].astype(object)
        
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
    if output_file_path:
        df.to_csv(output_file_path, index=False)
        messagebox.showinfo("Success", "The CSV file has been saved with the changes, conversion in Object succeded.")
    else: 
        messagebox.showerror("Error", "The CSV file encountered an error")
    
    
def int_converter():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    df = pd.read_csv(file_path)
    
    col_names = simpledialog.askstring("Columns", "Enter the name of the column(s) (separated by commas) :")
    if not col_names:
        messagebox.showwarning("Attention", "You must enter at least one column name.")
        return
    
    col_names = [col.strip() for col in col_names.split(",")]
    invalid_cols = [col_name for col_name in col_names if col_name not in df.columns]
    if invalid_cols:
        messagebox.showerror("Error", f"The following columns aren't present in the CSV file : {', '.join(invalid_cols)}")
        return
    
    for col_name in col_names:
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce', downcast='integer')
        
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
    if output_file_path:
        df.to_csv(output_file_path, index=False)
        messagebox.showinfo("Success", "The CSV file has been saved with the changes, conversion in Int succeded.")
    else: 
        messagebox.showerror("Error", "The CSV file encountered an error")
    
    
def float_converter():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    df = pd.read_csv(file_path)
    
    col_names = simpledialog.askstring("Columns", "Enter the name of the column(s) (separated by commas) :")
    if not col_names:
        messagebox.showwarning("Attention", "You must enter at least one column name.")
        return
    
    col_names = [col.strip() for col in col_names.split(",")]
    invalid_cols = [col_name for col_name in col_names if col_name not in df.columns]
    if invalid_cols:
        messagebox.showerror("Error", f"The following columns aren't present in the CSV file : {', '.join(invalid_cols)}")
        return
    
    for col_name in col_names:
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce')
        
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
    if output_file_path:
        df.to_csv(output_file_path, index=False)
        messagebox.showinfo("Success", "The CSV file has been saved with the changes, conversion in Float succeded.")
    else: 
        messagebox.showerror("Error", "The CSV file encountered an error")
    
    
def bool_converter():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    df = pd.read_csv(file_path)
    
    col_names = simpledialog.askstring("Columns", "Enter the name of the column(s) (separated by commas) :")
    if not col_names:
        messagebox.showwarning("Attention", "You must enter at least one column name.")
        return
    
    col_names = [col.strip() for col in col_names.split(",")]
    invalid_cols = [col_name for col_name in col_names if col_name not in df.columns]
    if invalid_cols:
        messagebox.showerror("Error", f"The following columns aren't present in the CSV file : {', '.join(invalid_cols)}")
        return
    
    for col_name in col_names:
        df[col_name] = df[col_name].astype(bool)
        
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
    if output_file_path:
        df.to_csv(output_file_path, index=False)
        messagebox.showinfo("Success", "The CSV file has been saved with the changes, conversion in Boolean succeded.")
    else: 
        messagebox.showerror("Error", "The CSV file encountered an error")
    
    
def date_converter():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    df = pd.read_csv(file_path)
    
    col_names = simpledialog.askstring("Columns", "Enter the name of the column(s) (separated by commas) :")
    if not col_names:
        messagebox.showwarning("Attention", "You must enter at least one column name.")
        return
    
    col_names = [col.strip() for col in col_names.split(",")]
    invalid_cols = [col_name for col_name in col_names if col_name not in df.columns]
    if invalid_cols:
        messagebox.showerror("Error", f"The following columns aren't present in the CSV file : {', '.join(invalid_cols)}")
        return
    
    for col_name in col_names:
        df[col_name] = pd.to_datetime(df[col_name], errors='coerce')
        
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
    if output_file_path:
        df.to_csv(output_file_path, index=False)
        messagebox.showinfo("Success", "The CSV file has been saved with the changes, conversion in Date succeded.")
    else: 
        messagebox.showerror("Error", "The CSV file encountered an error")