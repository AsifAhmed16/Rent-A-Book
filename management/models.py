from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

    class Meta:
        db_table = 'management_book'


class Rent(models.Model):
    user_id = models.IntegerField()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.FloatField(default=50.00)
    created_date = models.DateTimeField(auto_now_add=True)
    expired_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.book_id

    class Meta:
        db_table = 'management_rent'
