from fpdf import FPDF
import pandas as pd
from tkinter import Tk, Label, Button, Entry, filedialog
from tkinter import ttk  # Import ttk for modern widgets
from datetime import datetime
import re

def create_seo_report(csv_file, domain_name, output_file, report_date):
    # Read CSV file
    df = pd.read_csv(csv_file)
    
    # Initialize PDF
    pdf = FPDF()
    pdf.set_margins(left=35, top=20, right=35)  # Set consistent margins
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_y(20)  # Adjust starting position
    pdf.set_font("Arial", size=10)  # Reduce overall font size
    
    # Title
    pdf.set_text_color(240, 111, 5)  # Orange color for title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"SEO Report for {domain_name}", ln=True, align='C')
    pdf.ln(5)
    
    # Subtitle
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)  # Reset to black
    pdf.cell(0, 10, f"Created by YOUR BRAND HERE - {report_date}", ln=True, align='C')
    pdf.ln(10)
    
    # Add SEO Issues
    for index, row in df.iterrows():
        pdf.set_font("Arial", 'B', 12)
        pdf.set_text_color(240, 111, 5)  # Orange for issue name
        pdf.cell(0, 10, f"{index + 1}. {row['Issue Name']}", ln=True)
        
        pdf.set_font("Arial", size=10)  # Smaller font for details
        pdf.set_text_color(0, 0, 0)  # Black for details

        # Highlight HTML tags in the description
        description = row['Description']
        highlighted_desc = re.sub(r'(<[^>]+>)', r'[\\1]', description)  # Wrap tags in brackets
        
        pdf.multi_cell(0, 8, f"Type: {row['Issue Type']}\nPriority: {row['Issue Priority']}\nURLs: {row['URLs']}\n\nDescription: {highlighted_desc}\nHow to Fix: {row['How To Fix']}\n")
        pdf.ln(3)  # Reduce line spacing between sections
    
    # Save PDF
    pdf.output(output_file)

def browse_file():
    filename = filedialog.askopenfilename(title="Select SEO Report CSV", filetypes=[("CSV files", "*.csv")])
    file_entry.delete(0, 'end')
    file_entry.insert(0, filename)

def generate_report():
    csv_file = file_entry.get()
    domain_name = domain_entry.get()
    report_date = date_entry.get()
    output_file = f"SEO_Report_{domain_name}.pdf"
    create_seo_report(csv_file, domain_name, output_file, report_date)
    print(f"Report saved as {output_file}")

root = Tk()
root.title("SEO Report Generator")
root.geometry("500x200")  # Set window size
root.resizable(False, False)  # Disable resizing
root.configure(bg="#ffffff")  # Set background to white for better contrast

style = ttk.Style()
style.theme_use("clam")  # Use a modern theme

# Set widget colors with company orange (#F06F05)
style.configure("TLabel", background="#ffffff", foreground="#F06F05")  # White background, company orange text
style.configure("TButton", background="#F06F05", foreground="#ffffff", padding=5, relief="flat")  # Orange button, white text
style.map("TButton", background=[("active", "#D65A04")])  # Slightly darker orange on hover
style.configure("TEntry", fieldbackground="#ffffff", foreground="#000000")  # White entry, black text

ttk.Label(root, text="CSV File:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
file_entry = ttk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=5)
ttk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=5)

ttk.Label(root, text="Domain Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
domain_entry = ttk.Entry(root, width=40)
domain_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Date (MM/DD/YYYY):").grid(row=2, column=0, padx=10, pady=5, sticky='e')
date_entry = ttk.Entry(root, width=40)
date_entry.insert(0, datetime.now().strftime("%m/%d/%Y"))
date_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Button(root, text="Generate Report", command=generate_report).grid(row=3, column=0, columnspan=3, pady=10)



root.mainloop()
