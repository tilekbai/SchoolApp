from django.db import models
from . import constants
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    phone = models.CharField(
        max_length=13, 
        unique=True,
        )
    subject = models.CharField(
        max_length=90,
        null=True, 
        blank=True, 
        verbose_name="Название предмета",
        )
    

    class Meta:
        db_table = "teacher"
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"



class Student(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Full Name'
    )
    email = models.EmailField(
        max_length=254,
    )
    birth_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
    )
    school_class = models.ForeignKey(
        verbose_name='Class',
        to='SchoolClass',
        on_delete=models.DO_NOTHING,
        related_name='students',
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Address',
    )
    gender = models.CharField(
        verbose_name='Gender',
        max_length=6,
        choices=constants.GenderVariants.CHOICES,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "student"
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.name

class SchoolClass(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Name'
    )
    teacher = models.ForeignKey(
        verbose_name='Teacher',
        to='Teacher',
        on_delete=models.DO_NOTHING,
        related_name='classes',
        blank=True,
        null=True,
    )
    school = models.ForeignKey(
        verbose_name='School',
        to='School',
        on_delete=models.DO_NOTHING,
        related_name='classes',
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "class"
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(
        verbose_name='School name',
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "school"
        verbose_name = "Школа"
        verbose_name_plural = "Школы"

    def __str__(self):
        return self.name