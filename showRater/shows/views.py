# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import generic


from .models import Show

class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name= 'show_list'

    def get_queryset(self):
        return Show.objects.order_by('show_date')
