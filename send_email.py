import smtplib,ssl

host = 'smtp.gmail.com'
port = 465

username =  'kartikey.goel.285@gmail.com'
password =  'rmhfrwhhusshohjt'
receiver = 'kartikey.goel.285@gmail.com'

message = """\
Subject:Hi!
How are you?
Bye!
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)