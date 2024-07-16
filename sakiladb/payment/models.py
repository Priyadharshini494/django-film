from django.db import models
from django.contrib.auth.models import User
from sakiladb.models import BaseModel
from film.models import Film


class Country(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=255)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(BaseModel):

    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=100)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address}, {self.district}"


class Store(BaseModel):
    manager_staff = models.ForeignKey(
        "StaffProfile", on_delete=models.CASCADE, related_name="store_manager"
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Customer(BaseModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Inventory(BaseModel):
    Film = models.ForeignKey(Film, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inventory ID: {self.id}"


class StaffProfile(BaseModel):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    picture = models.BinaryField(blank=True, null=True)  # BLOB field for picture
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Rental(BaseModel):
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    return_date = models.DateTimeField(null=True, blank=True)
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rental {self.id}"


class Payment(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment ID: {self.id}"
