from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class ExpenseItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class ExpenseDetail(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200)
    exitem = models.ForeignKey(ExpenseItem, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.description

class Contribution(models.Model):
    date = models.DateField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.member} - {self.amount}"

