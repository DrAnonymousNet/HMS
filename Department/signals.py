from django.db.models.signals import post_init, post_save
from .models.inventory import Bed, Room
from django.dispatch import receiver

from django.dispatch import Signal

@receiver(post_save, sender = Room, dispatch_uid = "CreateBeds")
def create_bed_receiver(sender, **kwargs):
    if kwargs["created"]:
        max_bed_num = kwargs["instance"].max_bed_num
        name = kwargs["instance"].name
        beds = Bed.objects.bulk_create(
            [Bed(name = f"{name}-{i}", room = kwargs["instance"]) for i in range(max_bed_num)]
        )
        for bed in beds:
            bed.save()
    print(kwargs["instance"].max_bed_num, kwargs["created"])



#Signal.connect(create_bed_receiver, sender=Room)
