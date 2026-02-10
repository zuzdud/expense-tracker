from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    last_used = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Products"
        db_table = "products"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    last_used = models.DateTimeField()

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Expense(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    class Meta:
        db_table = "expenses"
        verbose_name_plural = "Expenses"

        indexes = [
            models.Index(fields=['category']),
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.category.last_used = self.created_at
        self.category.save(update_fields=['last_updated'])

    def __str__(self):
        return f"{self.product.name}"
