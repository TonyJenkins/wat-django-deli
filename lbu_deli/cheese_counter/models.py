from django.db import models


class Cheese(models.Model):

    MILK_CHOICES = [
        ("cow", "Cow"),
        ("goat", "Goat"),
        ("sheep", "Sheep"),
        ("buffalo", "Buffalo"),
        ("plant", "Plant-based"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=200, unique=True)
    milk_type = models.CharField(max_length=20, choices=MILK_CHOICES, default="cow")
    origin = models.CharField(max_length=200, blank=True)
    age_months = models.PositiveIntegerField(null=True, blank=True)
    is_vegan = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    slug = models.SlugField(max_length=200, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Cheese"
        verbose_name_plural = "Cheeses"

    def __str__(self):
        return self.name
