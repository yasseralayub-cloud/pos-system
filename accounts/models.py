from django.db import models
from django.contrib.auth.models import User

# خيارات الأدوار
ROLE_CHOICES = (
    ('admin', 'مدير النظام'),
    ('cashier', 'كاشير'),
    ('manager', 'مشرف'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cashier')

    def __str__(self):
        return f"{self.user.username} ({self.role})"
