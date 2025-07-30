from django.db import models

class Pizza(models.Model):
    """A pizza model representing a pizza with a name."""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """Return a string representation of the pizza."""
        return self.name

class Topping(models.Model):
    """A topping model representing a topping that can be added to a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """Return a string representation of the topping."""
        return self.name