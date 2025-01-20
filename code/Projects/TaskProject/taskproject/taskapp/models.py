from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model) :
    title=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    TASK_CATEGORIES = (
            ('Business', 'Business'),
            ('Personal', 'Personal'),
        )
    category = models.CharField(max_length=100,choices=TASK_CATEGORIES,default="Personal")

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.title
