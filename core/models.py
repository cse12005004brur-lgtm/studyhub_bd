from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
  CLASS_CHOICES = [
      ('Class 6', 'Class 6'),
      ('Class 7', 'Class 7'),
      ('Class 8', 'Class 8'),
      ('Class 9', 'Class 9'),
      ('Class 10', 'Class 10'),
      ('Class 11', 'Class 11'),
      ('Class 12', 'Class 12'),
  ]

  title = models.CharField(max_length=200, verbose_name='নোটের নাম')
  student_class = models.CharField(
      max_length=20, choices=CLASS_CHOICES, verbose_name='ক্লাস'
  )
  subject = models.CharField(max_length=100, verbose_name='বিষয়')
  description = models.TextField(verbose_name='বিবরণ')
  pdf_file = models.FileField(
      upload_to='notes_pdf/', verbose_name='পিডিএফ ফাইল'
  )
  upload_date = models.DateTimeField(
      auto_now_add=True, verbose_name='আপলোড তারিখ'
  )
  favorites = models.ManyToManyField(
      User, related_name='favorite_notes', blank=True
  )

  def __str__(self):
    return f'{self.title} ({self.student_class} - {self.subject})'