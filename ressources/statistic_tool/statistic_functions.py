import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.constants import *
import pandas as pd
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os


def min_max():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not filepath:
        messagebox.showwarning("Warning", "No file selected.")
        return

    df = pd.read_csv(filepath)

    column = simpledialog.askstring("Entry", "Enter the name of column :")

    if column not in df.columns:
        messagebox.showerror("Error", "The specified column names are invalid.")
        return
    
    # Check that the columns are numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        messagebox.showerror("Error", "The selected columns don't contain numeric data.")
        return

    try:
        # Do the min & max functions
        min_value = df[column].min()
        max_value = df[column].max()
        
        # Create a window to display information about the MinMax
        info_window = tk.Toplevel()
        info_window.title("Min Max Information")
        
        # Set the position of the window on the left side of the screen
        info_window_width = 200  # Set your desired width
        info_window_height = 110  # Set your desired height
        screen_width = info_window.winfo_screenwidth()
        screen_height = info_window.winfo_screenheight()
        x = (screen_width - info_window_width) // 2
        y = (screen_height - info_window_height) // 2
        info_window.geometry(f"{info_window_width}x{info_window_height}+{x}+{y}")
        
        # Background & Foreground custom
        info_text_widget = tk.Text(info_window, wrap="word", bg="#023047", fg="#ec7d1a")
        info_text_widget.pack(expand=True, fill="both")

        info_text_widget.insert(tk.END, f"Minimum of {column} :\n")
        info_text_widget.insert(tk.END, str(min_value))
        info_text_widget.insert(tk.END, f"\n\nMaximum of {column} :\n")
        info_text_widget.insert(tk.END, str(max_value))
    except Exception as e:
        messagebox.showerror("Error", f"Error : '{e}'")

    
def describe():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not filepath:
        messagebox.showwarning("Warning", "No file selected.")
        return

    df = pd.read_csv(filepath)

    try:
        # Do the describe function
        df_describe = df.describe()
        
        table_window = tk.Toplevel()
        table_window.title("Describe on : " + str(os.path.basename(filepath)))

        # Set the position of the window on the right side of the screen
        window_width = 750  # Set your desired width
        window_height = 410  # Set your desired height
        screen_width = table_window.winfo_screenwidth()
        screen_height = table_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2 
        table_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        text_frame = ttk.Frame(table_window)
        text_frame.pack(expand=True, fill="both")

        text_widget = tk.Text(text_frame, wrap="none", bg="#2b2b2b", fg="white")
        text_widget.pack(expand=True, fill="both")

        # Convert the Pandas DataFrame to PrettyTable with left alignment
        table = PrettyTable()
        table.field_names = ["<-Statistic->"] + df_describe.columns.tolist()

        for row_name in df_describe.index:
            row_data = [row_name] + df_describe.loc[row_name].tolist()
            table.add_row(row_data)
            
        table_str = table.get_string()
        text_widget.insert(tk.END, table_str)

        x_scrollbar = ttk.Scrollbar(table_window, orient="horizontal", command=text_widget.xview)
        x_scrollbar.pack(side="bottom", fill="x")
        text_widget.config(xscrollcommand=x_scrollbar.set)
    except Exception as e:
        messagebox.showerror("Error", f"Error : '{e}'")
    
    
def std():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not filepath:
        messagebox.showwarning("Warning", "No file selected.")
        return

    df = pd.read_csv(filepath)

    column = simpledialog.askstring("Entry", "Enter the name of column :")

    if column not in df.columns:
        messagebox.showerror("Error", "The specified column names are invalid.")
        return
    
    # Check that the columns are numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        messagebox.showerror("Error", "The selected columns don't contain numeric data.")
        return

    try:
        # Do the std function
        df_std = df[column].std()
        
        # Create a window to display information about the MinMax
        info_window = tk.Toplevel()
        info_window.title("Standard Deviation Information")
        
        # Set the position of the window on the left side of the screen
        info_window_width = 280  # Set your desired width
        info_window_height = 120  # Set your desired height
        screen_width = info_window.winfo_screenwidth()
        screen_height = info_window.winfo_screenheight()
        x = (screen_width - info_window_width) // 2
        y = (screen_height - info_window_height) // 2
        info_window.geometry(f"{info_window_width}x{info_window_height}+{x}+{y}")
        
        # Background & Foreground custom
        info_text_widget = tk.Text(info_window, wrap="word", bg="#023047", fg="#ec7d1a")
        info_text_widget.pack(expand=True, fill="both")

        info_text_widget.insert(tk.END, f"Standard Deviation of {column} :\n")
        info_text_widget.insert(tk.END, str(df_std))
    except Exception as e:
        messagebox.showerror("Error", f"Error : '{e}'")
    
    
def mean():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not filepath:
        messagebox.showwarning("Warning", "No file selected.")
        return

    df = pd.read_csv(filepath)

    column = simpledialog.askstring("Entry", "Enter the name of column :")

    if column not in df.columns:
        messagebox.showerror("Error", "The specified column names are invalid.")
        return
    
    # Check that the columns are numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        messagebox.showerror("Error", "The selected columns don't contain numeric data.")
        return

    try:
        # Do the mean function
        df_mean = df[column].mean()
        
        # Create a window to display information about the MinMax
        info_window = tk.Toplevel()
        info_window.title("Mean Information")
        
        # Set the position of the window on the left side of the screen
        info_window_width = 180  # Set your desired width
        info_window_height = 80  # Set your desired height
        screen_width = info_window.winfo_screenwidth()
        screen_height = info_window.winfo_screenheight()
        x = (screen_width - info_window_width) // 2
        y = (screen_height - info_window_height) // 2
        info_window.geometry(f"{info_window_width}x{info_window_height}+{x}+{y}")
        
        # Background & Foreground custom
        info_text_widget = tk.Text(info_window, wrap="word", bg="#023047", fg="#ec7d1a")
        info_text_widget.pack(expand=True, fill="both")

        info_text_widget.insert(tk.END, f"Mean of {column} :\n")
        info_text_widget.insert(tk.END, str(df_mean))
    except Exception as e:
        messagebox.showerror("Error", f"Error : '{e}'")
    
    
def variance():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not filepath:
        messagebox.showwarning("Warning", "No file selected.")
        return

    df = pd.read_csv(filepath)

    column = simpledialog.askstring("Entry", "Enter the name of column :")

    if column not in df.columns:
        messagebox.showerror("Error", "The specified column names are invalid.")
        return
    
    # Check that the columns are numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        messagebox.showerror("Error", "The selected columns don't contain numeric data.")
        return

    try:
        # Do the variance function
        df_variance = df[column].var()
        
        # Create a window to display information about the MinMax
        info_window = tk.Toplevel()
        info_window.title("Variance Information")
        
        # Set the position of the window on the left side of the screen
        info_window_width = 180  # Set your desired width
        info_window_height = 80  # Set your desired height
        screen_width = info_window.winfo_screenwidth()
        screen_height = info_window.winfo_screenheight()
        x = (screen_width - info_window_width) // 2
        y = (screen_height - info_window_height) // 2
        info_window.geometry(f"{info_window_width}x{info_window_height}+{x}+{y}")
        
        # Background & Foreground custom
        info_text_widget = tk.Text(info_window, wrap="word", bg="#023047", fg="#ec7d1a")
        info_text_widget.pack(expand=True, fill="both")

        info_text_widget.insert(tk.END, f"Variance of {column} :\n")
        info_text_widget.insert(tk.END, str(df_variance))
    except Exception as e:
        messagebox.showerror("Error", f"Error : '{e}'")
        
    
def frequency():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter the name of the column
    column_name = simpledialog.askstring("Choose column", "Enter the column name :")
    
    if column_name not in df.columns:
        messagebox.showwarning("Warning", "Invalid column name.")
        return

    # Create Histogram for the specified column
    plt.hist(df[column_name], alpha=0.7, label=column_name)
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {column_name}")
    plt.legend()
    plt.show()
    
    
def pca():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
        
    df = pd.read_csv(file_path)
    
    # Check for missing values in numeric columns
    numeric_columns = df.select_dtypes(include=['int64', 'float64'])
    
    if numeric_columns.isnull().values.any():
        messagebox.showerror("Error", "Missing values found in numeric columns. There should be no missing values.")
        return

    # Standardize and scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_columns)
    
    # Create a PCA instance
    pca = PCA()
    
    # Fit the PCA model to the standardized data
    pca.fit(scaled_data)
    
    # Get explained variance
    explained_variance = pca.explained_variance_ratio_
    
    # Calculate cumulative explained variance
    cumulative_explained_variance = explained_variance.cumsum()
    
    # Create a 1x2 grid of subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot the cumulative explained variance curve in the first subplot
    axes[0].scatter(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, marker='o')
    axes[0].plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, linestyle='--')
    axes[0].set_xlabel('Number of principal components')
    axes[0].set_ylabel('Cumulative explained variance')
    axes[0].set_title('Cumulative explained variance by principal component')
    
    # Calculate the loadings (vecteurs propres)
    loadings = pca.components_.T  # Transpose for easy use
    
    # Plot the correlation circle in the second subplot
    num_pc = len(pca.explained_variance_ratio_)
    for i in range(num_pc):
        axes[1].arrow(0, 0, loadings[i, 0], loadings[i, 1], head_width=0.03, head_length=0.05, fc='r', ec='r')
        axes[1].text(loadings[i, 0]*1.2, loadings[i, 1]*1.2, numeric_columns.columns[i], color='b', ha='center', va='center')
    
    # Add a unit circle to the second subplot
    circle = plt.Circle((0, 0), 1, color='b', fill=False)
    axes[1].add_artist(circle)
    
    axes[1].grid()
    axes[1].set_aspect('equal', adjustable='box')
    axes[1].set_xlim(-1, 1)
    axes[1].set_ylim(-1, 1)
    axes[1].set_xlabel('PC1')
    axes[1].set_ylabel('PC2')
    axes[1].set_title('Correlation Circle')
    
    plt.tight_layout()
    plt.show()
        
    
def boxplot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    column_input = simpledialog.askstring("Choose column", "Enter the column name:")
    
    if not column_input:
        messagebox.showwarning("Warning", "No column name entered.")
        return

    if column_input not in df.columns:
        messagebox.showwarning("Warning", "Column not found in the dataset.")
        return

    # Use pd.to_numeric to convert the column to float64 with the errors='coerce' option
    df[column_input] = pd.to_numeric(df[column_input], errors='coerce')

    if pd.api.types.is_numeric_dtype(df[column_input]):
        threshold_input = simpledialog.askstring("Enter Threshold Range", "Enter the Lower and Upper thresholds separated by ' : '\n"
                                                 "(example  10 : 50)\n(If you don't want Threshold just let the input empty) : ")

        if threshold_input:
            lower_threshold, upper_threshold = map(pd.to_numeric, threshold_input.split(':'))

            filtered_data = df[(df[column_input] > lower_threshold) & (df[column_input] < upper_threshold)]
        else:
            filtered_data = df

        plt.boxplot(filtered_data[column_input])
        plt.xlabel(column_input)
        plt.title(f"Box Plot of {column_input}")
        plt.show()
    else:
        messagebox.showerror("Error", "The selected column doesn't contain numeric data.")
    
    
def quartiles():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not filepath:
        messagebox.showwarning("Warning", "No file selected.")
        return

    df = pd.read_csv(filepath)

    column = simpledialog.askstring("Entry", "Enter the name of column :")

    if column not in df.columns:
        messagebox.showerror("Error", "The specified column names are invalid.")
        return
    
    # Check that the columns are numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        messagebox.showerror("Error", "The selected columns don't contain numeric data.")
        return

    try:
        # Do the quantile function
        df_q1 = df[column].quantile(0.25) # First quartile (Q1)
        df_q2 = df[column].quantile(0.5) # Second quartile (Q2)
        df_q3 = df[column].quantile(0.75) # Third quartile (Q3)
        df_q4 = df[column].quantile(0.9) # Fourth quartile (Q4)
        
        # Create a window to display information about the MinMax
        info_window = tk.Toplevel()
        info_window.title("Quantiles Information")
        
        # Set the position of the window on the left side of the screen
        info_window_width = 270  # Set your desired width
        info_window_height = 160  # Set your desired height
        screen_width = info_window.winfo_screenwidth()
        screen_height = info_window.winfo_screenheight()
        x = (screen_width - info_window_width) // 2
        y = (screen_height - info_window_height) // 2
        info_window.geometry(f"{info_window_width}x{info_window_height}+{x}+{y}")
        
        # Background & Foreground custom
        info_text_widget = tk.Text(info_window, wrap="word", bg="#023047", fg="#ec7d1a")
        info_text_widget.pack(expand=True, fill="both")

        info_text_widget.insert(tk.END, f"Quantile 1 of {column} :\n")
        info_text_widget.insert(tk.END, str(df_q1))
        info_text_widget.insert(tk.END, f"\nQuantile 2 (Median) of {column} :\n")
        info_text_widget.insert(tk.END, str(df_q2))
        info_text_widget.insert(tk.END, f"\nQuantile 3 of {column} :\n")
        info_text_widget.insert(tk.END, str(df_q3))
        info_text_widget.insert(tk.END, f"\nQuantile 4 of {column} :\n")
        info_text_widget.insert(tk.END, str(df_q4))
    except Exception as e:
        messagebox.showerror("Error", f"Error : '{e}'")



def chi_square():
    print('chi_square')

def anova():
    print('anova')

def shapiro_wilk():
    print('shapiro_wilk')

def t_test_student():
    print('t_test_student')