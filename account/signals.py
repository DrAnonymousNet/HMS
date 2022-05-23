from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, User)
def send_welcome_email(sender, **kwargs):
    if kwargs["created"]:
        subject = "Welcome Message"
        message = f"Hello {kwargs['instance'].username} !" \
                  f"You are welcome to our great website"
        recipient = [kwargs["instance"].email]
        send_mail(subject=subject,
                  message=message,
                  recipient_list=recipient, fail_silently=True)
        print("Message Sent")

