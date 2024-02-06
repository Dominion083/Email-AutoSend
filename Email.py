import tkinter as tk
from tkinter import filedialog
import csv
import smtplib
from email.mime.text import MIMEText

def send_emails(csv_file, subject, body):
    # Your email and SMTP server configuration
    sender_email = "dummy@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present
        for row in reader:
            recipient_email = row[0]  # Assuming email addresses are in the first column
            message = MIMEText(body)
            message["Subject"] = subject
            message["From"] = sender_email
            message["To"] = recipient_email

            try :
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    # Log in to the server
                    server.starttls()
                    server.login(sender_email,"dummy_password")  # Use a secure method for storing the password(this has to be your gmail key)
                    # Send the email
                    server.sendmail(sender_email, [recipient_email], message.as_string())
            
            except smtplib.SMTPServerDisconnected as e:
               print(f"SMTP Server Disconnected: {e}")
               print("Attempted server:", smtp_server)
               print("Attempted port:", smtp_port)
               print("Attempted sender email:", sender_email)
               print("Attempted recipient email:", recipient_email)
  
def browse_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    csv_path_var.set(file_path)

def send_emails_gui():
    csv_file = csv_path_var.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)
    
    send_emails(csv_file, subject, body)

# GUI setup
root = tk.Tk()
root.title("Email Sender")

csv_path_var = tk.StringVar()

csv_label = tk.Label(root, text="Select CSV File:")
csv_label.pack()

csv_entry = tk.Entry(root, textvariable=csv_path_var, state="readonly")
csv_entry.pack(side=tk.LEFT)

browse_button = tk.Button(root, text="Browse", command=browse_csv)
browse_button.pack(side=tk.LEFT)

subject_label = tk.Label(root, text="Email Subject:")
subject_label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

body_label = tk.Label(root, text="Email Body:")
body_label.pack()

body_text = tk.Text(root, height=5, width=30)
body_text.pack()

send_button = tk.Button(root, text="Send Emails", command=send_emails_gui)
send_button.pack()

root.mainloop()
