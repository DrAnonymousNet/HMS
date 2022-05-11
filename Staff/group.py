from django.contrib.auth.models import Group



Doctor_Permission = [
        "can admit", "can prescribe", "can fill entry", 'can edit entry'
        "can discharge",
        "can book surgery", "can diagnose", "can have intern", 'can read prescription', 'can create testresult',
        "can read test result",
    ]


# Nurse_Groups = ["Unit Header"]
def create_group(group_list):
    for name in group_list:
        new_group = Group.objects.create(name=name)
        new_group.save()
