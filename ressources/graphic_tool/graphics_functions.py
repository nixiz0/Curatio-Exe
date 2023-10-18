from tkinter.constants import *
from tkinter import filedialog, messagebox, simpledialog
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def histogram():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user how many values ​​they want to display
    num_values = simpledialog.askinteger("Choose the number of values", "Enter 1 or 2.\n\n --> 1 to display a histogram with 1 value.\n --> 2 to display a histogram with 2 values.")
    if num_values not in [1, 2]:
        messagebox.showwarning("Warning", "Please enter 1 or 2.")
        return

    # Ask the user to enter the name of the column(s)
    column_input = simpledialog.askstring("Choose column(s)", "Enter the column name(s) (separated by a comma):")
    column_names = [col.strip() for col in column_input.split(',')]

    # Check that column names are valid
    if len(column_names) != num_values:
        messagebox.showwarning("Warning", f"You must enter {num_values} column name(s).")
        return

    # Create Histogram
    for col in column_names:
        plt.hist(df[col], alpha=0.7, label=col)

    if num_values == 1:
        plt.xlabel(column_names[0])
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {column_names[0]}")
    else:
        plt.xlabel(column_names[0])
        plt.ylabel(column_names[1])
        plt.title(f"Histogram of {column_names[0]} and {column_names[1]}")

    plt.legend()
    plt.show()
    
    
def scatter_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user how many values ​​they want to display
    num_values = simpledialog.askinteger("Choose the number of values", "Enter 1 or 2.\n\n --> 1 to display a scatter plot with 1 value.\n --> 2 to display a scatter plot with 2 values.")
    if num_values not in [1, 2]:
        messagebox.showwarning("Warning", "Please enter 1 or 2.")
        return

    # Ask the user to enter the name of the column(s)
    column_input = simpledialog.askstring("Choose column(s)", "Enter column name(s) (comma separated) :")
    column_names = [col.strip() for col in column_input.split(',')]

    # Check that column names are valid
    if len(column_names) != num_values:
        messagebox.showwarning("Warning", f"You must enter {num_values} column name(s).")
        return

    # Create the Scatter Plot
    if num_values == 1:
        plt.scatter(df[column_names[0]], df.index)
        plt.xlabel(column_names[0])
        plt.title(f"Scatter Plot of {column_names[0]}")
    else:
        plt.scatter(df[column_names[0]], df[column_names[1]])
        plt.xlabel(column_names[0])
        plt.ylabel(column_names[1])
        plt.title(f"Scatter Plot of {column_names[0]} and {column_names[1]}")

    plt.show()
    
    
def box_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user how many values ​​they want to display
    num_values = simpledialog.askinteger("Choose the number of values", "Enter 1 or 2.\n\n --> 1 to display a box plot with 1 value.\n --> 2 to display a box plot with 2 values.")
    if num_values not in [1, 2]:
        messagebox.showwarning("Warning", "Please enter 1 or 2.")
        return

    # Ask the user to enter the name of the column(s)
    column_input = simpledialog.askstring("Choose column(s)", "Enter the column name(s) (separated by a comma) :")
    column_names = [col.strip() for col in column_input.split(',')]

    # Check that column names are valid
    if len(column_names) != num_values:
        messagebox.showwarning("Warning", f"You must enter {num_values} column name(s).")
        return

    # Create the Box Plot
    if num_values == 1:
        plt.boxplot(df[column_names[0]])
        plt.xlabel(column_names[0])
        plt.title(f"Box Plot of {column_names[0]}")
    else:
        data = [df[column] for column in column_names]
        plt.boxplot(data, labels=column_names)
        plt.xlabel("Columns")
        plt.ylabel("Values")
        plt.title(f"Box Plot of {', '.join(column_names)}")

    plt.show()
    
    
def pie_charts():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to choose the column for the pie chart
    column_name = simpledialog.askstring("Choose column", "Enter the column name for the pie chart :")

    # Check that the column name is valid
    if column_name not in df.columns:
        messagebox.showwarning("Warning", f"Column '{column_name}' doesn't exist in the CSV file.")
        return

    # Get column data
    data = df[column_name].value_counts()

    # Create the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal') # To make the pie chart a circle
    plt.title(f"Column pie chart of '{column_name}'")
    plt.show()
    
    
def bar_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter the category column name
    category_column = simpledialog.askstring("Choose the categories column", "Enter the category column name :")

    # Check that the column name is valid
    if category_column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{category_column}' doesn't exist in the CSV file.")
        return

    # Ask the user to enter the name of the values ​​column
    value_column = simpledialog.askstring("Choose the value column", "Enter the name of the value column :")

    # Check that the column name is valid
    if value_column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{value_column}' doesn't exist in the CSV file.")
        return

    # Create the bar plot
    plt.figure(figsize=(12, 6))
    plt.bar(df[category_column], df[value_column])
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.title(f"Bar Chart of {value_column} by {category_column}")
    plt.xticks(rotation=45, ha='right')
    
    plt.show()
    
    
def surface_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter the name of column X & Check that column name X is valid
    x_column = simpledialog.askstring("Choose column X", "Enter the name of column X (numeric values) :")
    if x_column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{x_column}' doesn't exist in the CSV file.")
        return

    # Ask the user to enter the name of column Y & Check that column name Y is valid
    y_column = simpledialog.askstring("Choose column Y", "Enter the name of column Y (numeric values):")
    if y_column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{y_column}' doesn't exist in the CSV file.")
        return

    # Ask the user to enter the name of column Z & Check that column name Z is valid
    z_column = simpledialog.askstring("Choose column Z (values)", "Enter column name Z (numeric values) :")
    if z_column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{z_column}' does not exist in the CSV file.")
        return

    # Create the surface diagram
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(df[x_column], df[y_column], df[z_column], cmap='viridis')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_zlabel(z_column)
    ax.set_title(f"Surface Diagram of {z_column} in function of {x_column} and {y_column}")

    plt.show()
    

def heatmap():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)
    
    choice_heatmap = simpledialog.askstring("Please enter 2 or 3 \n", "--> 2 for a heatmap with 2 simple columns (crosstab). \n --> 3 for a more advanced 3-column heatmap (pivot).")
    if (choice_heatmap != '2') and (choice_heatmap != '3'):
        messagebox.showerror("Error", "Please enter 2 or 3.")
        return
    else: 
        if choice_heatmap == '2':
            col1 = simpledialog.askstring("Entry", "Enter the name of column 1 :")
            if not col1:
                messagebox.showerror("Error", "Column 1 name cannot be empty.")
                return

            col2 = simpledialog.askstring("Entry", "Enter the name of column 2 :")
            if not col2:
                messagebox.showerror("Error", "Column 2 name cannot be empty.")
                return

            # Check if column names exist in the DataFrame
            if col1 not in df.columns or col2 not in df.columns:
                messagebox.showerror("Error", "The column names entered aren't present in the file.")
                return

            # Create heat map using seaborn and matplotlib
            crosstab_data = pd.crosstab(df[col1], df[col2])
            plt.figure(figsize=(12, 8))
            sns.heatmap(crosstab_data, annot=True, fmt="d", cmap="YlGnBu")
            plt.title("HeatMap")
            plt.xlabel(col2)
            plt.ylabel(col1)
            plt.show()
        else: 
            # Prompt user to enter column name X & Verify that column name X is valid
            x_column = simpledialog.askstring("Choose column X", "Enter the name of column X :")
            if x_column not in df.columns:
                messagebox.showwarning("Warning", f"Column '{x_column}' doesn't exist in the CSV file.")
                return

            # Prompt user to enter column name Y & Verify that column name Y is valid
            y_column = simpledialog.askstring("Choose column Y", "Enter the name of column Y :")
            if y_column not in df.columns:
                messagebox.showwarning("Warning", f"Column '{y_column}' does not exist in the CSV file.")
                return

            # Prompt user to enter column name Z & Verify that column name Z is valid
            value_column = simpledialog.askstring("Choose the value column (Z)", "Enter the name of the value column (Z) :")
            if value_column not in df.columns:
                messagebox.showwarning("Warning", f"Column '{value_column}' doesn't exist in the CSV file.")
                return

            # Create the pivot dataframe for the heatmap
            pivot_df = df.pivot(index=y_column, columns=x_column, values=value_column)

            # Create HeatMap
            plt.figure(figsize=(10, 6))
            sns.heatmap(pivot_df, cmap="YlGnBu", annot=True, fmt=".2f", cbar=True)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f"HeatMap of {value_column} by {x_column} and {y_column}")
            plt.show()
    
    
def violin_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter the category column name & Check that the category column name is valid
    category_column = simpledialog.askstring("Choose the categories column", "Enter the category column name :")
    if category_column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{category_column}' doesn't exist in the CSV file.")
        return

    # Ask the user to enter the name of the values ​​column & Verify that the column name of the values ​​is valid
    value_column = simpledialog.askstring("Choose the value column", "Enter the name of the value column :")
    if value_column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{value_column}' doesn't exist in the CSV file.")
        return

    # Create the violin diagram
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=category_column, y=value_column, data=df, palette="muted")
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.title(f"Violin Diagram of {value_column} by {category_column}")

    plt.show()
    

def butterfly():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to enter column names for the butterfly chart values
    value_columns_input = simpledialog.askstring("Choose the 2 columns of butterfly values", "Enter the names of the 2 columns of the butterfly values (separated by commas) :")
    value_columns = [col.strip() for col in value_columns_input.split(',')]

    # Check that column names are valid
    if len(value_columns) != 2:
        messagebox.showwarning("Warning", "Please enter exactly 2 column names for the butterfly values.")
        return

    # Check that the columns exist in the DataFrame
    columns_exist = all(col in df.columns for col in value_columns)
    if not columns_exist:
        messagebox.showwarning("Warning", "Some specified columns don't exist in the CSV file.")
        return

    # Create the butterfly shape graphic
    plt.figure(figsize=(8, 6))
    plt.plot(df[value_columns[0]], label=value_columns[0])
    plt.plot(df[value_columns[1]], label=value_columns[1])
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.title("Butterfly Shaped Graphic")
    plt.legend()

    plt.show()
    
    
def correlation():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not filepath:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(filepath)

    column1 = simpledialog.askstring("Entry", "Enter the name of column 1 :")
    column2 = simpledialog.askstring("Entry", "Enter the name of column 2 :")

    if column1 not in df.columns or column2 not in df.columns:
        messagebox.showerror("Error", "The specified column names are invalid.")
        return
    
    # Check that the columns are numeric
    if not pd.api.types.is_numeric_dtype(df[column1]) or not pd.api.types.is_numeric_dtype(df[column2]):
        messagebox.showerror("Error", "The selected columns don't contain numeric data.")
        return

    # Calculate the correlation between columns
    correlation_value = df[column1].corr(df[column2])

    # Display Correlation
    messagebox.showinfo("Correlation", f"The correlation between '{column1}' and '{column2}' is: {correlation_value:.2f}")

    # Plot the correlation graph
    plt.scatter(df[column1], df[column2])
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f"Correlation between {column1} and {column2}")
    
    plt.show()
    

def stem_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to select the column of values ​​to display in the stem chart
    value_column = df.columns[0] # By default, selects the first column

    if len(df.columns) > 1:
        value_column = simpledialog.askstring("Choose the column of values", "Choose the column of values to display :")

        if value_column not in df.columns:
            messagebox.showwarning("Warning", f"Column '{value_column}' doesn't exist in the CSV file.")
            return

    # Create the stem diagram
    plt.stem(df.index, df[value_column], markerfmt='bo', basefmt=" ", linefmt='b-')
    plt.xlabel("Index")
    plt.ylabel(value_column)
    plt.title(f"Stem Diagram of {value_column}")

    plt.show()
    
    
def density_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to select the column of values ​​to display in the density graph
    value_column = df.columns[0]  # By default, selects the first column

    if len(df.columns) > 1:
        value_column = simpledialog.askstring("Choose the value column", "Choose the column of values to display :")

        if value_column not in df.columns:
            messagebox.showwarning("Warning", f"Column '{value_column}' doesn't exist in the CSV file.")
            return

    # Create the density graph
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df[value_column], shade=True, color="b")
    plt.xlabel(value_column)
    plt.ylabel("Density")
    plt.title(f"Density Graph of {value_column}")

    plt.show()
    
    
def corr_heatmap():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)
    numeric_columns = df.select_dtypes(include=['int64', 'float64'])
    if numeric_columns.any().any():
        correlation_matrix = numeric_columns.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title("Correlation Matrix in the Dataframe")
        plt.show()
    else: 
        messagebox.showerror("Error", "You don't have numeric columns in your dataframe.")
    
    
def distribution():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask the user to select the column of values ​​to display in the distribution graph
    value_column = df.columns[0] # By default, selects the first column

    if len(df.columns) > 1:
        value_column = simpledialog.askstring("Choose the value column", "Choose the column of values to display :")

        if value_column not in df.columns:
            messagebox.showwarning("Warning", f"Column '{value_column}' doesn't exist in the CSV file.")
            return

    # Create the distribution graph
    plt.figure(figsize=(10, 6))
    sns.histplot(df[value_column], kde=True, color="b")
    plt.xlabel(value_column)
    plt.ylabel("Frequency")
    plt.title(f"Distribution Chart of {value_column}")

    plt.show()
    

def categorical():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)

    # Ask user to select categorical column
    category_column = simpledialog.askstring("Choose the categorical column", "Choose the categorical column to display :")

    if category_column not in df.columns:
        messagebox.showwarning("Warning", f"Column '{category_column}' doesn't exist in the CSV file.")
        return

    # Create the categorical variable graph
    plt.figure(figsize=(10, 6))
    sns.countplot(x=category_column, data=df, palette="Set3")
    plt.xlabel(category_column)
    plt.ylabel("Counting")
    plt.title(f"Categorical Variables Chart for {category_column}")
    plt.xticks(rotation=45)
    
    plt.show()