import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "@gmail.com"# Email que esta enviando
toaddr = "@gmail.com"# Email que vai receber a cotacao do Dolar

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Cotacao do Dolar via API"

body = "Arquivo cotação dolar"

msg.attach(MIMEText(body, 'plain'))

filename = "meu_arquivo.json"
attachment = open("meu_arquivo.json", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "password") #Senha do email que esta enviando a cotacao Dolar
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()

