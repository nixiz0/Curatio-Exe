from tkinter.constants import *
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd


def mean():
    file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
    else:
        df = pd.read_csv(file_path)

        # Ask name of the column
        column_name = simpledialog.askstring("Average of missing values", "Enter the column name to calculate the average:")

        if column_name is None:
            pass
        elif column_name not in df.columns:
            messagebox.showerror("Error", f"Column '{column_name}' doesn't exist in the file.")
        else:
            # Verify if column is numeric
            try:
                df[column_name] = pd.to_numeric(df[column_name])
                # Calcul the mean
                mean_value = df[column_name].mean()

                # Replace missing values by the mean
                df[column_name].fillna(mean_value, inplace=True)

                # Save in a new path the modify file
                new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])

                if new_file_path:
                    # Save the modify file
                    df.to_csv(new_file_path, index=False)
                    messagebox.showinfo("Success", f"The file was edited and saved with the average of the missing values in the '{column_name}' column.\nThe file has been saved in : {new_file_path}")
            except ValueError:
                messagebox.showerror("Error", f"Column '{column_name}' is not numeric (float or int).")


def std_function():
    file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
    else:
        df = pd.read_csv(file_path)
        
        # Ask name of the column
        column_name = simpledialog.askstring("Standard Deviation of missing values", "Enter the column name to calculate the standard deviation:")
        
        if column_name is None:
            return
        elif column_name not in df.columns:
            messagebox.showerror("Error", f"Column '{column_name}' doesn't exist in the file.")
        else: 
            # Verify if column is numeric
            try: 
                df[column_name] = pd.to_numeric(df[column_name])
                # Calcul the standard deviation (std)
                std_dev_value = df[column_name].std()
                
                # Replace missing values by std
                df[column_name].fillna(std_dev_value, inplace=True)
                
                # Save in a new path the modify file
                new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])
                
                if new_file_path:
                    # Save the modify file
                    df.to_csv(new_file_path, index=False)
                    messagebox.showinfo("Success", f"The file was edited and saved with the standard deviation of the missing values in the '{column_name}' column.\nThe file has been saved in : {new_file_path}")
            except ValueError:
                messagebox.showerror("Error", f"Column '{column_name}' is not numeric (float or int).")
        
        
def delete_function():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to read CSV file : {e}")
        return

    column = simpledialog.askstring("Choose a column", "Enter the name of the column to process :")

    # Check if the column exists in the DataFrame
    if column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{column}' doesn't exist in the CSV file.")
        return

    # Perform the drop of fillna() to remove rows with missing values in the chosen column
    df.dropna(subset=[column], inplace=True)

    # Save the modified DataFrame to a new CSV file
    new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    # Check if a file path has been provided for saving
    if not new_file_path:
        messagebox.showwarning("Warning", "No file saving path provided.")
        return

    try:
        df.to_csv(new_file_path, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to save CSV file : {e}")
        return
    messagebox.showinfo("Success", f"The file was edited and saved with the suppression of the missing values in the '{column}' column.\nThe file has been saved in : {new_file_path}")


def def_value():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    col_name = simpledialog.askstring("Select column", "Enter the name of the column to modify :")
    if not col_name:
        messagebox.showinfo("Info", "Invalid or empty column name.")
        return

    # Check if the column exists in the DataFrame
    if col_name not in df.columns:
        messagebox.showinfo("Info", f"Column '{col_name}' does not exist in the file.")
        return

    # Ask the user for the value to replace missing values with
    value_to_replace = simpledialog.askstring("Replacement value", "Enter value to replace missing values :")
    if value_to_replace is None:
        messagebox.showinfo("Info", "Invalid or empty replacement value.")
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
            messagebox.showinfo("Info", f"Unsupported column type : {col_type}.")
            return
    except ValueError:
        messagebox.showinfo("Info", f"Invalid replacement value type for column '{col_name}'.")
        return

    # Replace missing values in the selected column
    df[col_name].fillna(value_to_replace, inplace=True)

    new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not new_file_path:
        messagebox.showinfo("Info", "Operation canceled.")
        return

    df.to_csv(new_file_path, index=False)
    messagebox.showinfo("Success", f"The missing values were replaced and the new file was saved.\nThe file has been saved in : {new_file_path}")


def mode():
    file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    column_name = simpledialog.askstring("Mode Replacement of missing values", "Enter the column name to replace missing values with the mode :")
    if column_name is None:
        return

    if column_name not in df.columns:
        messagebox.showerror("Error", f"Column '{column_name}' doesn't exist in the file.")
        return

    # Check if the values in the column are categorical
    if df[column_name].dtype == 'object':
        try:
            mode_value = df[column_name].mode().iloc[0]
            df[column_name].fillna(mode_value, inplace=True)
            new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])
            if not new_file_path:
                return

            df.to_csv(new_file_path, index=False)
            messagebox.showinfo("Success", f"The file was edited and saved with mode replacement in the '{column_name}' column.\nThe file has been saved in : {new_file_path}")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e))
    else:
        messagebox.showerror("Error", "Column values must be categorical (strings).")


def median():
    file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
    else: 
        df = pd.read_csv(file_path)
        
        # Ask name of the column
        column_name = simpledialog.askstring("Median of missing values", "Enter the column name to calculate the median:")
        
        if column_name is None:
            pass 
        elif column_name not in df.columns:
            messagebox.showerror("Error", f"Column '{column_name}' doesn't exist in the file.")
        else: 
            # Verify if column is numeric
            try:
                df[column_name] = pd.to_numeric(df[column_name])
                # Calcul the median
                median_value = df[column_name].median()
                
                # Replace missing values by the median
                df[column_name].fillna(median_value, inplace=True)
                
                # Save in a new path the modify file
                new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[('CSV files', '*.csv')])
                
                if new_file_path:
                    # Save the modify file
                    df.to_csv(new_file_path, index=False)
                    messagebox.showinfo("Success", f"The file was edited and saved with the median of the missing values in the '{column_name}' column.\nThe file has been saved in : {new_file_path}")
            except ValueError:
                messagebox.showerror("Error", f"Column '{column_name}' is not numeric (float or int).")