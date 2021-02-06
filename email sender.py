import smtplib # allows us to create an SMT server
from email.message import EmailMessage # built-in

email = EmailMessage()
email['from'] = 'Chav Sumalinog'
email['to'] = 'chaviotics@gmail.com'
email['subject'] = 'First email from python.'

