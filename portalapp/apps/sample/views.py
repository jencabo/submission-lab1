# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

#Load CORE views to inherit from
from core import views as CORE_VIEWS


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    context = CORE_VIEWS.context_maker(request, context)

    html_template = loader.get_template('sample/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    context = CORE_VIEWS.context_maker(request, context)


    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        elif load_template == "":
            return HttpResponseRedirect(reverse('home'))

        context['segment'] = load_template

        html_template = loader.get_template('sample/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('sample/page-404.html')
        return HttpResponse(html_template.render(context, request))

#    except:
#        html_template = loader.get_template('sample/page-500.html')
#        return HttpResponse(html_template.render(context, request))
