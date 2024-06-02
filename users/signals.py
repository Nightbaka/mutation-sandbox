from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(user_signed_up)
def populate_user(sender, request, user, **kwargs):
    sociallogin = kwargs.get('sociallogin')
    if sociallogin:
        if sociallogin.account.provider == 'google':
            extra_data = sociallogin.account.extra_data
            user.first_name = extra_data.get('given_name', '')
            user.last_name = extra_data.get('family_name', '')
            user.email = extra_data.get('email', '')
            user.save()
