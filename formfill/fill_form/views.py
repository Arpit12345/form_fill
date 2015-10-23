from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import dataForm
from .models import fill


def index(request):
    response = "WELCOME"
    template = loader.get_template('fill_form/home.html')
    context = RequestContext(request, {'response': response})
    return HttpResponse(template.render(context))

def form(request):
    template1 = loader.get_template('fill_form/form.html')
    context = RequestContext(request)

    return HttpResponse(template1.render(context))

def get_data(request):

    # fill.Full_name = request.POST.get('name')
    # fill.Add = request.POST.get('add')
    # fill.ipadd = request.POST.get('ipadd')
    # fill.email = request.POST.get('email')
    # fill.phoneno = request.POST.get('number')
    if request.POST:
        form = request.POST.get("name, address, ip, email, phoneno")
        form = dataForm(request.POST)
        if form.is_valid():
            #instance = f.save(commit=False)
            form.save()
            return HttpResponseRedirect('/home/')
        else:
            f = dataForm()
            args = {}

            args['form'] = form
            return render_to_response('/', args)


    template2 = loader.get_template('fill_form/show.html')
    context = RequestContext(request)
    return HttpResponse(template2.render(context))







