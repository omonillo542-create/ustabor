from django.db import models

# User Model
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

# ServiceRequest Model
class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Location Model
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

# Job Model
class Job(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Payment Model
class Payment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

# Rating Model
class Rating(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)