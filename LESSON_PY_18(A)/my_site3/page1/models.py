from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

from .models import Person
  
people = Person.objects.bulk_create([
    Person(name="Kate", age=24),
    Person(name="Ann", age=21),
])
 
for person in people:
    print(f"{person.id}. {person.name}")