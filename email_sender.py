import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'NAME_OF_SENDER'
email['to'] = 'TO_EMAIL_ADDRESS'
email['subject'] = 'This is a Python email'

email.set_content(html.substitute({'name': 'NAME_OF_RECIPIENT'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    email_address = 'FROM_EMAIL_ADDRESS'
    email_password = 'EMAIL_PASSWORD'
    smtp.login(email_address, email_password)
    smtp.send_message(email)
    print('All good!')
