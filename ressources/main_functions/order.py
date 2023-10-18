from tkinter.constants import *
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd


def order_by():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        messagebox.showerror("Error", "The file is empty or cannot be read.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file :\n{str(e)}")
        return

    # Ask the user which column they want to sort
    column_to_sort = simpledialog.askstring("Column selection", "Enter the name of the column to sort :")

    if column_to_sort is None:
        return

    if column_to_sort not in df.columns:
        messagebox.showerror("Error", "The specified column doesn't exist in the CSV file.")
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
        messagebox.showinfo("Success", "The CSV file has been sorted in ascending order and saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file :\n{str(e)}")


def reverse_order():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        messagebox.showerror("Error", "The file is empty or cannot be read.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file :\n{str(e)}")
        return

    # Ask the user which column they want to sort
    column_to_sort = simpledialog.askstring("Column selection", "Enter the name of the column to sort :")

    if column_to_sort is None:
        return

    if column_to_sort not in df.columns:
        messagebox.showerror("Error", "The specified column doesn't exist in the CSV file.")
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
        messagebox.showinfo("Success", "The CSV file was sorted in descending order and saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file :\n{str(e)}")