import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "testing.majorproj@gmail.com"  # Enter your address
receiver_email = "ragireddys@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Your vehicle is subjected to challan. You need to pay xxxx amount"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)