import smtplib # allows us to create an SMT server
from email.message import EmailMessage # built-in
from string import Template # using $, we can sbustitute variables
from pathlib import Path # os.path; but better because we can read it

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Chav Sumalinog'
email['to'] = 'chaviotics@gmail.com', 'epsumalinog@up.edu.ph'
email['subject'] = 'First email from python.'

email.set_content(html.substitute({'name': 'Chaviiiu'}), 'html') # can send stuff; # or even {'name': 'Isaac'}

# smtp sends to email

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # encryption mechanism
    smtp.login('icearchts@gmail.com', 'emiliepp2')
    smtp.send_message(email)
    print('All good!')


# learn how to send to multiple people at once with customized name using data bases.

