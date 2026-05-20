import os
import re
import shutil

if not os.path.exists("emails.txt"):
    with open("emails.txt", "w") as file:
        file.write("""
        Contact us at support@gmail.com
        Send mail to admin@yahoo.com
        Another email: test123@outlook.com
        """)

with open("emails.txt", "r") as file:
    content = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

output_file = "extracted_emails.txt"

with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")

folder_name = "Output_Folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

shutil.move(output_file, os.path.join(folder_name, output_file))

print(f"{output_file} moved to {folder_name}")
