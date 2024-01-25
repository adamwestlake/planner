from django.db import models

class Role(models.Model):
    STATUS_MEMBER = 'M'
    STATUS_MANAGER = 'A'

    STATUS_CHOICES = [
        (STATUS_MEMBER, 'Member'),
        (STATUS_MANAGER, 'Manager'),
    ]

    type = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_MEMBER, primary_key=True, blank=True)

    def __str__(self) -> str:
        return f"{self.type}"

class Location(models.Model):
    
    basic = 'shops'
    building = models.CharField(max_length=255, blank=True, default=basic)

    def __str__(self) -> str:
        return f"{self.building}"

class User(models.Model):
    STATUS_MEMBER = 'Member'
    STATUS_MANAGER = 'Manager'

    STATUS_CHOICES = [
        (STATUS_MEMBER, 'Member'),
        (STATUS_MANAGER, 'Manager'),
    ]
   
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=55, choices=STATUS_CHOICES, default=STATUS_MEMBER)
    location = models.ForeignKey('Location', blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ['name']

        