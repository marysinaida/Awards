from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    #create message subject and sender
    subject = 'Welcome to the moringa Awwards'
    sender = 'marydorcassinaida54@gmail.com'

    #passing in the context variables
    text_content = render_to_string('email/projectsemail.txt',{"name:name"})

    html_content = render_to_string('email/projectemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
    