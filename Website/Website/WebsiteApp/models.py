from django.db import models

# Create your models here.
class Feature:
    id: int
    title: str
    description: str
    image: str
    is_true: bool
