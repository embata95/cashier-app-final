from django.db.models.signals import post_save
from cashier.profiles.models import UserProfile
from cashier.users.models import cashierUser, ContactDetails
from django.dispatch import receiver

@receiver(post_save, sender=cashierUser)
def super_user_created(instance, created, **kwargs):
    if created:
        if cashierUser.objects.get(id=instance.id).is_superuser:
            profile = UserProfile(first_name='', last_name='', email=instance.id, phone_number='', apartment=None,
                               user=cashierUser.objects.get(id=instance.id))
            profile.save()
        if not ContactDetails.objects.exists():
            contact_profile = ContactDetails(
                email='default@email.com',
                phone = '0123456789',
                first_name = 'Default_First_Name',
                last_name = 'Default_Last_Name'
            )
            contact_profile.save()
