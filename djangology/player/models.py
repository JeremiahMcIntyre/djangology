from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    userDisplayName = models.CharField(max_length=25)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
