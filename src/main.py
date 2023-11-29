from django_orm import *
from db.models import User


# Seed a few users in the database
User.objects.create(name="Dan")
User.objects.create(name="Robert")

for u in User.objects.all():
    print(f"ID: {u.id} \tUsername: {u.name}")
