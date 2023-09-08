from django.dispatch import receiver
from django.db.models.signals import post_save
from rolepermissions.roles import assign_role

from .models import Users


@receiver(post_save, sender=Users)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == "V":
            assign_role(instance, 'vendedor')
        elif instance.cargo == "G":
            assign_role(instance, 'gerente')
