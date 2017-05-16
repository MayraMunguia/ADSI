from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction

def home(request):
    return render(request, 'hope/home.html', {})


def msg_new(request):
    form = MensajeForm()
    return render(request, 'blog/home.html', {'form': form})

    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
        	post = form.save()
       		post.save()
       		return HttpResponse("Gracias!")       		
    else:
        form = MensajeForm()


