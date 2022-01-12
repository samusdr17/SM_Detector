from django.db import models
from django_matplotlib.fields import MatplotlibFigureField

# Create your models here.


class MriDdbb(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='mriddbbs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'mriddbb'
        verbose_name_plural= 'mriddbbs'

    def __str__(self):
        return self.title



class MyModelWithFigure(models.Model):
    # ... other fields
    # figures.py should be in the same directory where models.py is placed.
    # see  ./django_matplotlib/figures.py for example.
    fig = MatplotlibFigureField(figure='test_figure', verbose_name='figure',
                                silent=True)
    # ... other fields