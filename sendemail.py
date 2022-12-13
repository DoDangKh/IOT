import smtplib
import ssl
from email.message import EmailMessage

email_sender='n19dccn093@student.ptithcm.edu.vn'
email_password='kcxmbelvpalffeaf'
email_receiver='ddangkhoa75@gmail.com'


def sendmail(DUST, SOUND):
    import smtplib

    subject='Thong tin o nhiem'
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content("O Nhiem bui: "+str(DUST)+" O Nhiem Tieng On: "+str(SOUND))
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())