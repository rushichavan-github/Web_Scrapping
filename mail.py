from email import message
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_mail(filename):
    mail_from = 'chavanrishi17@gmail.com'
    mail_to = 'chavan.rushi@yahoo.com'
    subject = 'Finance Stock Report.'

    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = subject

    body = "<b> Today's Finance Report Attached.</b>"
    msg.attach(MIMEText(body,'html'))

    my_file = open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment;filename='+ filename)
    msg.attach(part)
    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(mail_from ,'yhbnglwpwawxvmwd')

    server.sendmail(mail_from,mail_to,message)
    server.quit()