# program to send email
from email.message import EmailMessage
import ssl
import smtplib

if __name__ == '__main__':
    sender = input("Enter your email:  ")
    passwd = input("Enter app password:  ")
    reciever = input("Enter reciever email adress:  ")
    subject = input("Enter subject:  ")
    body = input("Enter the body of the mail:  ")

    em = EmailMessage()
    em['From'] = sender
    em['To'] = reciever
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, passwd)
        smtp.sendmail(sender, reciever, em.as_string())
