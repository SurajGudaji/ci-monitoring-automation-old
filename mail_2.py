import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
# Run the monitor.py script and capture its output
from monitor_2 import main
process = main()
print("Mail procss = ",process)

sender_email = 'yarasanisrinivas@gmail.com'
receiver_email = ['yarasani.srinivasa.rao@ibm.com','suraj.gudaji1@ibm.com','shilpa.gokul@ibm.com']
receiver_email_string = ', '.join(receiver_email)
smtp_server = 'smtp.gmail.com' #'smtp.outlook.com'
smtp_port = 587
smtp_username = 'yarasanisrinivas@gmail.com'
smtp_password = ''
subject = 'Monitor.py Script Output'
body = process # Convert the byte output to a string
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email_string
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    # Use receiver_email without conversion here, as sendmail expects a list or string
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")
