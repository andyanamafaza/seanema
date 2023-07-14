from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def withdraw_balance(self, amount):
        self.balance -= amount
        self.save()

    def deposit_balance(self, amount):
        self.balance += amount
        self.save()


class TicketTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_title = models.TextField()
    seat_numbers = models.TextField()
    total_cost = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
