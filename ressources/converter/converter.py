import sqlite3
import tkinter as tk
from tkinter.constants import *
from tkinter import filedialog, messagebox
import pandas as pd


def sql_csv():
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
        messagebox.showerror("Error", f"Error reading SQL file : {e}")
        return

    csv_file_converted = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not csv_file_converted:
        return

    # Convert the DataFrame to a CSV file with the 'utf-8-sig' encoding to handle special characters
    try:
        df.to_csv(csv_file_converted, index=False, encoding="utf-8-sig")
        messagebox.showinfo("Success", "Conversion completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"CSV conversion error : {e}")
        return
        
        
def xlsx_csv():
    file_path_xlsx = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if not file_path_xlsx:
        return

    try:
        df = pd.read_excel(file_path_xlsx)

        file_path_csv = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path_csv:
            return

        # Convert and save the file to CSV with utf-8-sig encoding
        df.to_csv(file_path_csv, index=False, encoding="utf-8-sig")

        tk.messagebox.showinfo("Successful conversion", "The file was successfully converted to CSV.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred during conversion : {str(e)}")
        
        
def csv_sql():
    root = tk.Tk()
    root.withdraw()

    csv_file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not csv_file:
        return

    try:
        df = pd.read_csv(csv_file, encoding='utf-8')
    except Exception as e:
        messagebox.showerror("Error", f"Error reading CSV file : {e}")
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
        messagebox.showinfo("Success", "Conversion completed successfully !")
    except Exception as e:
        messagebox.showerror("Error", f"SQL conversion error : {e}")
        return
        
        
def csv_xlsx():
    file_path_csv = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path_csv:
        return

    try:
        df = pd.read_csv(file_path_csv)

        file_path_xlsx = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if not file_path_xlsx:
            return

        df.to_excel(file_path_xlsx, index=False)

        messagebox.showinfo("Successful conversion", "The file was successfully converted to XLSX.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during conversion : {str(e)}")