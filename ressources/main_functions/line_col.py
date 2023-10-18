from tkinter.constants import *
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd


def del_column():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    df = pd.read_csv(file_path)
    
    columns_to_delete = simpledialog.askstring("Delete columns", "Enter the names of the columns to delete (separated by commas) :")
    
    if columns_to_delete is not None:  # Check if user pressed "Cancel"
        columns_to_delete = [col.strip() for col in columns_to_delete.split(",")]
        
        # Check if all the entered column names exist in the DataFrame
        invalid_columns = [col for col in columns_to_delete if col not in df.columns]
        
        if invalid_columns:
            messagebox.showerror("Error", f"The following columns don't exist in the file : {', '.join(invalid_columns)}")
            return
        
        df.drop(columns_to_delete, axis=1, inplace=True)
        df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
        messagebox.showinfo("Success", "Columns successfully deleted and saved to file.")
    else:
        messagebox.showwarning("Warning", "No columns have been deleted.")
        
        
def del_line():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user for the range of lines to delete
    start_index = simpledialog.askinteger("Blanking range", "Enter starting index :")
    end_index = simpledialog.askinteger("Blanking range", "Enter ending index :")

    # Check if the input values are valid
    if start_index is None or end_index is None or start_index < 1 or end_index < 1 or start_index > end_index:
        messagebox.showwarning("Warning", "Invalid input values.")
        return

    try:
        # Open the file in read mode and read its lines
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check if the provided range is valid
        if start_index > len(lines) or end_index > len(lines):
            messagebox.showwarning("Warning", "The range exceeds the number of lines in the file.")
            return

        # Delete the lines within the specified range
        lines = lines[:start_index - 1] + lines[end_index:]

        # Save the modifications back to the original file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        messagebox.showinfo("Deletion successful", f"Rows {start_index} up to {end_index} were successfully deleted.")
    except Exception as e:
        messagebox.showerror("Error", f"An Error has occurred : {e}")


def add_column():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    df = pd.read_csv(file_path)

    columns_to_add = simpledialog.askstring("Add columns", "Enter the names of the new columns (separated by commas) :")
    
    if columns_to_add is not None:
        columns_to_add = [col.strip() for col in columns_to_add.split(",")]
        for new_col in columns_to_add:
            df[new_col] = None

        df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
        messagebox.showinfo("Success", "Columns successfully added and saved to file.")
    else:
        messagebox.showwarning("Warning", "The user hasn't entered any new columns.")


def add_line():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    columns = df.columns.tolist()
    columns_to_add_values = simpledialog.askstring("Columns to add values", "Enter column names to add values (separated by commas) :")

    if columns_to_add_values is not None:
        # Split the input string into a list of column names, strip whitespace, and filter valid column names
        columns_to_add_values = [col.strip() for col in columns_to_add_values.split(",") if col.strip() in columns]
    else:
        # Handle the case where the user cancels the dialog
        columns_to_add_values = []

    if not columns_to_add_values:
        messagebox.showwarning("Warning", "No valid columns were specified to add values to.")
        return

    index_interval = simpledialog.askstring("Index Interval", "Enter the index interval (separated by a hyphen '-') :")
    start_index, end_index = map(int, index_interval.split('-'))

    if start_index < 0 or end_index >= len(df):
        messagebox.showerror("Error", "Invalid index interval.")
        return

    new_data = {}
    for col in columns_to_add_values:
        new_value_input = simpledialog.askstring("New value", f"Enter the value for the column '{col}':")
        new_value = new_value_input.strip()

        if new_value is None:
            new_value = ""  # Use an empty string for non-numeric values

        new_data[col] = [new_value] * (end_index - start_index + 1)

    new_df = pd.DataFrame(new_data)

    for col in columns_to_add_values:
        df.loc[start_index:end_index, col] = new_df[col].values

    df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
    messagebox.showinfo("Success", "Lines added successfully and saved to file.")
      
        
def modify_column():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    column_to_modify = simpledialog.askstring("Change the name of a column", "Enter the name of the column to modify :")
    if column_to_modify:
        if column_to_modify in df.columns:
            new_column_name = simpledialog.askstring("Change column name", f"Enter the new name for the column '{column_to_modify}':")
            if new_column_name:
                df.rename(columns={column_to_modify: new_column_name}, inplace=True)
                df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
                messagebox.showinfo("Success", "Column name successfully modified and saved to file.")
            else:
                messagebox.showwarning("Warning", "No new column name has been entered.")
        else:
            messagebox.showerror("Error", f"Column '{column_to_modify}' does not exist in the file.")
    else:
        messagebox.showwarning("Warning", "No columns have been selected.")


def modify_line():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    columns = df.columns.tolist()  # Convert columns to a list of column names
    column_to_modify = simpledialog.askstring("Choose column", "Enter the name of the column to modify :")
    
    # Check if column_to_modify is None or an empty string
    if column_to_modify is None or column_to_modify.strip() == "":
        messagebox.showwarning("Warning", "Invalid or unspecified column name.")
        return

    column_to_modify = column_to_modify.strip()

    if column_to_modify not in columns:
        messagebox.showerror("Error", "Invalid column name.")
        return

    index_interval = simpledialog.askstring("Index Interval", "Enter the index interval (separated by a hyphen '-') :")
    start_index, end_index = map(int, index_interval.split('-'))

    if start_index < 0 or end_index >= len(df):
        messagebox.showerror("Error", "Invalid index interval.")
        return

    new_value_input = simpledialog.askstring("New value", f"Enter the new value for column '{column_to_modify}' at index interval [{start_index}:{end_index}] :")
    new_value = new_value_input.strip()

    if not new_value:
        messagebox.showerror("Error", "You must enter a value for the chosen column.")
        return

    df.loc[start_index:end_index, column_to_modify] = new_value

    df.to_csv(file_path, index=False)  # Save the modified DataFrame back to the same file
    messagebox.showinfo("Success", "Values changed successfully and saved to file.")


def interval_value():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")
        return
    except pd.errors.EmptyDataError:
        messagebox.showerror("Error", "The file is empty")
        return
    except pd.errors.ParserError:
        messagebox.showerror("Error", "Unable to parse file")
        return

    column_name = simpledialog.askstring("Entry", "Enter the name of the column to process :")
    if column_name not in df.columns:
        messagebox.showerror("Error", f"Column '{column_name}' doesn't exist in the filer")
        return

    interval_str = simpledialog.askstring("Entry", "Enter the selection interval (ex: 0:1) :")

    if not interval_str:
        messagebox.showerror("Error", "Invalid interval. Use the 'start:end' format")
        return

    interval_parts = interval_str.split(':')
    if len(interval_parts) == 1:
        start = None
        end = int(interval_parts[0])
    elif len(interval_parts) == 2:
        start = int(interval_parts[0]) if interval_parts[0] else None
        end = int(interval_parts[1]) if interval_parts[1] else None
    else:
        messagebox.showerror("Error", "Invalid interval. Use the 'start:end' format")
        return

    if start is None:
        start = 0
    if end is None:
        end = len(df[column_name])

    df[column_name] = df[column_name].apply(lambda x: x[start:end])

    output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not output_file:
        messagebox.showerror("Error", "Invalid output file name")
        return

    try:
        df.to_csv(output_file, index=False)
        messagebox.showinfo("Success", "Changes saved successfully !")
    except PermissionError:
        messagebox.showerror("Error", "Unable to save changes. Make sure the file isn't already open.")
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving : {e}")