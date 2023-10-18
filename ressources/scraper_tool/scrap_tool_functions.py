from tkinter import simpledialog, filedialog, messagebox
from bs4 import BeautifulSoup
import csv
import requests
import re
from fake_useragent import UserAgent


def email():
    url = simpledialog.askstring("URL", "Enter the URL to scrape:")

    if not url:
        messagebox.showwarning("Warning", "No URL entered")
        return

    try:
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
        }

        response = requests.get(url, headers=headers)

        # Parse content HTML of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrapes email addresses
        email_addresses = set()  # Using a set to avoid duplicates
        for tag in soup.find_all(["a", "p", "span"]):
            if tag.name not in ["script", "style"]:
                email_matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", tag.text)
                email_addresses.update(email_matches)

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        
        if not file_path:
            messagebox.showerror("Error", "No path entered")
            return

        # Writes email addresses to CSV file
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for email in email_addresses:
                writer.writerow({"email": email})

        messagebox.showinfo("Finished", "The scraping is complete, and the email addresses have been saved in a CSV file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scraping: {str(e)}")
    
     
def href():
    url = simpledialog.askstring("URL", "Enter the URL to scrape:")

    if not url:
        messagebox.showwarning("Warning", "No URL entered")
        return

    try:
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
        }

        response = requests.get(url, headers=headers)

        # Parse content HTML of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrapes href attributes
        href_attributes = set()  # Using a set to avoid duplicates
        for tag in soup.find_all(["a"]):
            if 'href' in tag.attrs:
                href_attributes.add(tag['href'])

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        
        if not file_path:
            messagebox.showerror("Error", "No path entered")
            return

        # Writes href attributes to CSV file
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["href"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for href in href_attributes:
                writer.writerow({"href": href})

        messagebox.showinfo("Finished", "The scraping is complete, and the href attributes have been saved in a CSV file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scraping: {str(e)}")
    
      
def text():
    url = simpledialog.askstring("URL", "Enter the URL to scrape:")

    if not url:
        messagebox.showwarning("Warning", "No URL entered")
        return

    try:
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
        }

        response = requests.get(url, headers=headers)

        # Parse content HTML of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrapes text content
        text_content = set()  # Using a set to avoid duplicates
        for tag in soup.find_all(["p", "span", "div", "h1", "h2", "h3", "h4", "h5", "h6", "a"]):
            if tag.get_text(strip=True):  # Check if the tag has non-empty text content
                text_content.add(tag.get_text(strip=True))

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        
        if not file_path:
            messagebox.showerror("Error", "No path entered")
            return

        # Writes text content to CSV file
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["text"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for text in text_content:
                writer.writerow({"text": text})

        messagebox.showinfo("Finished", "The scraping is complete, and the text content has been saved in a CSV file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scraping: {str(e)}")
    
     
def image():
    url = simpledialog.askstring("URL", "Enter the URL to scrape images from:")

    if not url:
        messagebox.showwarning("Warning", "No URL entered")
        return

    try:
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
        }

        response = requests.get(url, headers=headers)

        # Parse content HTML of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrapes image URLs
        image_urls = set()  # Using a set to avoid duplicates
        for img_tag in soup.find_all("img"):
            if 'src' in img_tag.attrs:
                image_urls.add(img_tag['src'])

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        
        if not file_path:
            messagebox.showerror("Error", "No path entered")
            return

        # Writes image URLs to CSV file
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["image_url"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for image_url in image_urls:
                writer.writerow({"image_url": image_url})

        messagebox.showinfo("Finished", "The scraping is complete, and the image URLs have been saved in a CSV file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scraping: {str(e)}")
    
      
def list():
    url = simpledialog.askstring("URL", "Enter the URL to scrape lists from:")

    if not url:
        messagebox.showwarning("Warning", "No URL entered")
        return

    try:
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
        }

        response = requests.get(url, headers=headers)

        # Parse content HTML of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrapes list items
        list_items = set()  # Using a set to avoid duplicates
        for list_tag in soup.find_all(["ul", "ol"]):
            for item in list_tag.find_all("li"):
                list_items.add(item.get_text(strip=True))

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        
        if not file_path:
            messagebox.showerror("Error", "No path entered")
            return

        # Writes list items to CSV file
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["list_item"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for list_item in list_items:
                writer.writerow({"list_item": list_item})

        messagebox.showinfo("Finished", "The scraping is complete, and the list items have been saved in a CSV file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scraping: {str(e)}")
        

def number():
    url = simpledialog.askstring("URL", "Enter the URL to scrape numbers from:")

    if not url:
        messagebox.showwarning("Warning", "No URL entered")
        return

    try:
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
        }

        response = requests.get(url, headers=headers)

        # Parse content HTML of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrape numbers (ints and floats) with accompanying text
        number_pattern = r"([-+]?\d*\.\d+|\d+)(\D+)"
        data = []

        for text in soup.stripped_strings:
            matches = re.findall(number_pattern, text)
            for match in matches:
                number, text = match
                data.append({"number": number, "text": text})

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

        if not file_path:
            messagebox.showerror("Error", "No path entered")
            return

        # Writes numbers and accompanying text to a CSV file
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["number", "text"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for entry in data:
                writer.writerow(entry)

        messagebox.showinfo("Finished", "Scraping is complete, and data has been saved in a CSV file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scraping: {str(e)}")
    
      
def all():
    url = simpledialog.askstring("URL", "Enter the URL to scrape:")

    if not url:
        messagebox.showwarning("Warning", "No URL entered")
        return

    ua = UserAgent()
    headers = {
        "User-Agent": ua.random
    }

    try:
        response = requests.get(url, headers=headers)

        # Parse content HTML of page
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrapes the necessary data
        scraped_data = []
        email_addresses = []
        numbers_with_text = []

        for tag in soup.find_all(["a", "p", "span", "img"]):
            tag_text = tag.text.strip()

            # Searches for numbers with accompanying text
            number_pattern = r"([-+]?\d*\.\d+|\d+)(\D+)"
            number_matches = re.findall(number_pattern, tag_text)
            for match in number_matches:
                number, text = match
                numbers_with_text.append({"number": number, "text": text})

            scraped_data.append({
                "tag": tag.name,
                "text": tag_text,
                "href": tag.get("href", ""),
                "email": ""
            })

            # Searches for email addresses and adds them to the email_addresses list
            if tag.name not in ["script", "style"]:
                email_matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", tag_text)
                email_addresses.extend(email_matches)

        # Find and add image sources to the scraped data
        for img in soup.find_all("img"):
            img_src = img.get("src", "")
            scraped_data.append({
                "tag": "img",
                "text": "",
                "href": img_src,
                "email": ""
            })

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            messagebox.showerror("Error", "No path entered")
            return

        # Writes data to CSV file, including email addresses and numbers with text
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["tag", "text", "href", "email", "number", "number_text"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for entry in scraped_data:
                entry["number"] = ""
                entry["number_text"] = ""
                writer.writerow(entry)

            # Adds the extracted email addresses to the CSV file
            for email in email_addresses:
                writer.writerow({"tag": "email", "text": email, "href": "", "email": email, "number": "", "number_text": ""})

            # Adds the extracted numbers with text to the CSV file
            for num_entry in numbers_with_text:
                writer.writerow({"tag": "number", "text": num_entry["text"], "href": "", "email": "", "number": num_entry["number"], "number_text": num_entry["text"]})

        messagebox.showinfo("Finished", "The scraping is complete, and the data has been saved in a CSV file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scraping: {str(e)}")
