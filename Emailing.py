import smtplib
import ssl
def email(message):

    host = ("smtp.gmail.com")
    port = 465

    username = "abdullahbilal938@gmail.com"
    password="xlzf zusq ygeo mamb"

    reciever = "abdullahbilal938@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host , port ,context = context) as server:
        server.login(username , password)
        server.sendmail(username , reciever ,message)
