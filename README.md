# VirtualPortal

VirtualPortal is a Python-based utility designed to scan and report on the health of disk drives on Windows systems. It offers preemptive alerts before potential failures, helping to prevent data loss and downtime.

## Features

- Monitors disk health using Windows Management Instrumentation Command-line (WMIC).
- Sends email alerts if any disk reports a status other than `OK`.
- Easy configuration for email notifications.

## Requirements

- Python 3.x
- Windows operating system
- An email account for sending alerts

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/VirtualPortal.git
   ```
2. Navigate to the project directory:
   ```bash
   cd VirtualPortal
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Open `virtual_portal.py` in a text editor.
2. Update the following variables with your email configuration:
   ```python
   email_sender = "your_email@example.com"
   email_password = "your_password"
   email_receiver = "alert_receiver@example.com"
   smtp_server = "smtp.example.com"
   smtp_port = 587
   ```
3. Save the changes.

## Usage

Run the script using Python:
```bash
python virtual_portal.py
```

The program will check the disk health and send an email alert if any issues are detected.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Please ensure that you securely handle your email credentials. It is highly recommended to use environment variables or a secure vault for managing sensitive information in production environments.