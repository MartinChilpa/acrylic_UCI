import urllib.parse
from django.conf import settings
from django.core.mail import send_mail


def send_registration_invite(email, language):
    signup_url = f'{settings.FRONTEND_BASE_URL}auth/sign-up'

    email_string = urllib.parse.quote_plus(email)
    
    if language == 'en':
        subject = "🦎You're IN! You got your Acrylic.LA invitation!"
        message = f"""
        Welcome to the Acrylic platform!
        
        REGISTER HERE! {signup_url}?email={email_string}
        
        If you have any questions, just join us on Skool (https://www.skool.com/the-acrylic-kamunity/about), a free community where you can learn about your music rights and ask any questions you have about Acrylic or how it works.​
        
        Let's go!🦎​
        -KAM​
        """
    else:
        subject = "🦎¡Estás DENTRO! ¡Ya tienes tu invitación Acrylic.LA!"
        message = f"""
        ¡Bienvenido a la plataforma Acrylic!
        
        RÉGISTRATE AQUÍ {signup_url}?email={email_string}

        Si tienes alguna pregunta, únete a nosotros en Skool (https://www.skool.com/la-kamunidad-acrylic-8907/about), una comunidad gratuita donde puedes aprender sobre tus derechos musicales y hacer cualquier pregunta que tengas sobre Acrylic o cómo funciona.
    
        ¡Vamos!🦎
        -KAM
        """

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
