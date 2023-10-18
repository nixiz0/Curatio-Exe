from tkinter import filedialog, messagebox
import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv


def profiling_report():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return

    df = pd.read_csv(file_path)
    profile = ProfileReport(df, title="Profiling Report")
    new_file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[('HTML files', '*html')])
    if new_file_path:
        # Save the modify file
        profile.to_file(new_file_path)
        messagebox.showinfo("Success", f"The file has been saved in : {new_file_path}")
    elif Exception: 
        messagebox.showerror("Error", f"{Exception}")
    else: 
        messagebox.showerror("Error", "Operation Canceled")
    
def analysis_report():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        messagebox.showwarning("Warning", "No files selected.")
        return
    df = pd.read_csv(file_path)
    analyze_report = sv.analyze(df)
    new_file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[('HTML files', '*html')])
    if new_file_path:
        # Save the modify file
        analyze_report.show_html(new_file_path)
        messagebox.showinfo("Success", f"The file has been saved in : {new_file_path}")
    elif Exception: 
        messagebox.showerror("Error", f"{Exception}")
    else: 
        messagebox.showerror("Error", "Operation Canceled")