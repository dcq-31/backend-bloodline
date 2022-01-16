from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# User Model
class User(AbstractUser):
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.get_full_name()
  

  """
  Add Fields
  image
  """
# Dog Model
class Dog(models.Model):
  # Choises of breed (for example)
  AFGHAN_HOUND = 'AF'
  PEKINGESE = 'PE'
  BASSADOR = 'BA'
  DOGS_BREED = (
    (AFGHAN_HOUND, 'Afghan Hound'),
    (PEKINGESE, 'Pekingese'),
    (BASSADOR, 'Bassador'),
  )
  name = models.CharField(max_length=100)
  code = models.CharField('identification code', max_length=10)
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='related user')
  date_birth = models.DateTimeField('date of birthday')
  breed = models.CharField('animal species', choices=DOGS_BREED, max_length=100)
  partners = models.ManyToManyField('self', blank=True, verbose_name='related partners')
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name + " | " + self.code