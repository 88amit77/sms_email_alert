#working code which also excepts attachments
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path



def Send_Mail(email, password,send_to_emails, subject, message, file_location):
    # Create the attachment file (only do it once)
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # Connect and login to the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    print("wait....80%..process..Done")
    # Loop over each email to send to
    for send_to_email in send_to_emails:
        # Setup MIMEMultipart for each email address (if we don't do this, the emails will concat on each email sent)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        # Attach the message to the MIMEMultipart object
        msg.attach(MIMEText(message, 'plain'))
        # Attach the attachment file
        msg.attach(part)

        # Send the email to this specific email address
        server.sendmail(email, send_to_email, msg.as_string())
    print("sent")
    # Quit the email server when everything is done
    server.quit()

def Mail_Data():
    email = 'testamit78@gmail.com'
    password = '@8896340048a'
    send_to_emails = ["amit.t@sellerbuymore.com", "88amit77@gmail.com", "7788amittiwari7788@gmail.com"] # List of email addresses
    subject = 'This is the subject'
    message = 'This is my message'
    # file_location = 'C:/photography/pic1.JPEG'
    file_location = '/Users/amittiwari/Downloads/anders-jilden-uwbajDCODj4-unsplash.jpg'

    Send_Mail(email, password,send_to_emails, subject, message, file_location)

print(Mail_Data())