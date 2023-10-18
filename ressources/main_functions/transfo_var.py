import tkinter as tk
from tkinter.constants import *
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import csv


def dtypes_object():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    if file_path:
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                content = "\n".join(", ".join(row) for row in csv_reader)

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
                info_window.title("dtypes Objects in your CSV file")
                
                # Set the position of the window on the left side of the screen
                info_window_width = 350  # Set your desired width
                info_window_height = 200  # Set your desired height
                screen_width = info_window.winfo_screenwidth()
                screen_height = info_window.winfo_screenheight()
                x = (screen_width - info_window_width) // 2
                y = (screen_height - info_window_height) // 2
                info_window.geometry(f"{info_window_width}x{info_window_height}+{x}+{y}")

                info_text_widget = tk.Text(info_window, wrap="word", bg="#2b2b2b", fg="white")

                # Create a vertical scrollbar for the info_text_widget
                info_scrollbar = tk.Scrollbar(info_window, command=info_text_widget.yview)
                info_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                info_text_widget.configure(yscrollcommand=info_scrollbar.set)
                info_text_widget.pack(expand=True, fill="both")

                info_text_widget.insert(tk.END, "Columns with dtype 'object' :\n\n")
                info_text_widget.insert(tk.END, str(object_dtypes))
        except ValueError:
            messagebox.showerror("Error", "Error executing the function.")


# The dummies function takes the specified column and replaces it with its dummies variables
def dummies():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    # Load the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read CSV file : {str(e)}")
        return

    # Ask the user for the name of the column to process
    column_name = simpledialog.askstring("Entry", "Enter the name of the column to process :")
    if not column_name:
        messagebox.showerror("Error", "You must provide the name of the column to process.")
        return  # If no column name was entered, exit the function
    
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        messagebox.showerror("Error", f"Column '{column_name}' not found in CSV file.")
        return

    # Check the type of the column
    column_type = df[column_name].dtype
    if column_type not in [object, str]:
        messagebox.showerror("Error", "Only string or object columns are supported for creating dummies.")
        return

    # Convert the column into dummy variables
    try:
        dummies_df = pd.get_dummies(df[column_name], dtype=int) # Specify dtype=int
        # Drop the original column from the DataFrame
        df.drop(column_name, axis=1, inplace=True)
        # Concatenate the original DataFrame with the dummies DataFrame
        df = pd.concat([df, dummies_df], axis=1)
        
        # Ask the user to choose a new location for the modified file
        new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])
        try:
            df.to_csv(new_file_path, index=False)
            messagebox.showinfo("Success", f"The values of column '{column_name}' have been one hot encoded and the changes have been saved in : {new_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save changes : {str(e)}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Unable to create dummies : {str(e)}")
        
        
# one_hot applies One Hot encoding to the entire DataFrame using the specified column name as the prefix for new generated columns.
def one_hot():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    try:
        # Load CSV file using pandas
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        messagebox.showerror("Error", "The selected file is empty.")
        return
    except pd.errors.ParserError:
        messagebox.showerror("Error", "Unable to read CSV file. Make sure it is formatted correctly.")
        return

    # Request the name of the column to be processed
    column_name = simpledialog.askstring("Entry", "Enter the name of the column to process :")
    if not column_name:
        messagebox.showerror("Error", "You must provide the name of the column to process.")
        return

    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        messagebox.showerror("Error", f"Column '{column_name}' doesn't exist in the CSV file.")
        return

    # Check the column type
    col_type = df[column_name].dtype
    if col_type not in [str, object]:
        messagebox.showerror("Error", "The column must be of type 'string' or 'object' to be processed in one hot encoding.")
        return

    # Apply One Hot Encoding to the column
    try:
        df_encoded = pd.get_dummies(df, columns=[column_name], prefix=[column_name], dtype=int) # Specify dtype=int
        
        # Ask the user to choose a new location for the modified file
        new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])
        try:
            df_encoded.to_csv(new_file_path, index=False)
            messagebox.showinfo("Success", f"The values of column '{column_name}' have been one hot encoded and the changes have been saved in : {new_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save changes : {str(e)}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encoding : {str(e)}")
        
        
def fusion():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    col1_name = simpledialog.askstring("Column names", "Enter the name of the first column to merge :")
    col2_name = simpledialog.askstring("Column names", "Enter the name of the second column to merge :")

    merge_col_name = simpledialog.askstring("Merge Column Name", "Enter the merge column name :")

    if col1_name not in df.columns or col2_name not in df.columns:
        messagebox.showerror("Non-existent columns", "The specified column names don't exist in the file.")
        return

    # Merge the specified columns and place them in the merge column
    df[merge_col_name] = df[col1_name].astype(str) + df[col2_name].astype(str)

    # Ask the user to choose a new location for the merged file
    new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])
    if not new_file_path:
        messagebox.showwarning("Warning", "No output file selected.")
        return

    # Save changes to the new CSV file
    try:
        df.to_csv(new_file_path, index=False)
        messagebox.showinfo("Successful merger", f"The columns have been merged and the changes have been saved to the file : {new_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Merge Failed: {str(e)}")
        return