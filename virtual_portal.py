import os
import subprocess
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
email_sender = "your_email@example.com"
email_password = "your_password"
email_receiver = "alert_receiver@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587

def get_disk_health():
    command = "wmic diskdrive get status, model, size"
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if result.stderr:
        raise Exception(f"Error running disk health check: {result.stderr}")
    return result.stdout.strip()

def parse_disk_health(output):
    lines = output.splitlines()
    keys = lines[0].split()
    disks = []
    for line in lines[1:]:
        line_data = line.split()
        disk_info = dict(zip(keys, line_data))
        disks.append(disk_info)
    return disks

def check_disk_status(disks):
    warnings = []
    for disk in disks:
        if disk['Status'] != 'OK':
            warnings.append(f"Disk {disk['Model']} with size {disk['Size']} is reporting a status of {disk['Status']}.")
    return warnings

def send_email_alert(warnings):
    subject = "Disk Health Alert"
    body = "\n".join(warnings)

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, msg.as_string())
    server.quit()

def main():
    try:
        disk_health_output = get_disk_health()
        disks = parse_disk_health(disk_health_output)
        warnings = check_disk_status(disks)
        if warnings:
            send_email_alert(warnings)
            print("Alert email sent.")
        else:
            print("All disks are healthy.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()