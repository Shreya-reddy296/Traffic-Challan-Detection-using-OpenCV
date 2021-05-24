import smtplib, ssl
import receiver


def send_emails(reg_no):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "testing.majorproj@gmail.com"  # Enter your address
    #receiver_email = "receiver@gmail.com"  # Enter receiver address
    password ="Testing#123" #input("Type your password and press enter: ")

    message1 = """\
Subject: Challan for your vehicle
    
We have detected your vehicle for wrong parking. You need to pay xxxx amount
."""

    receiver_email=receiver.generate_receiver_email(reg_no)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, message1)
#send_emails()
            
    #print("Emails are sent successfully")