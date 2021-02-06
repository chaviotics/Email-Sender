import smtplib # allows us to create an SMT server
from email.message import EmailMessage # built-in

email = EmailMessage()
email['from'] = 'Chav Sumalinog'
email['to'] = 'chaviotics@gmail.com'
email['subject'] = 'First email from python.'

email.set_content('Hello Chav!') # can send stuff

# smtp sends to email

with smtplib.SMTP(host='smpt.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # encryption mechanism
    smtp.login('icearchts@gmail.com', 'emiliepp2')
    smtp.send_message(email)
    print('All good!')


