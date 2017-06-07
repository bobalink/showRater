# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Show(models.Model):
    show_name = models.CharField(max_length=200)
    show_date = models.DateTimeField('show date')

    def __str__(self):
        return self.show_name

