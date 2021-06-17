# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

"""
Different models used by system tests in django-spanner code.
"""
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=40)
    user_id = models.IntegerField(primary_key=True)
    
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    rating = models.DecimalField()
    class Meta:
        interleave = Person

class Number(models.Model):
    num = models.DecimalField()

    def __str__(self):
        return str(self.num)
