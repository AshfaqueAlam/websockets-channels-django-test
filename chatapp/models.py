from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Logs(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('successful', 'Successful'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='u_logs')
    status = models.CharField(choices=STATUS_CHOICE, max_length=250, blank=True, null=True, default='pending')
    percent_completed = models.FloatField(default=0.0, blank=True, null=True)
    error_msg = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'logs'
