from django.shortcuts import render

# Create your views here.
from .forms import postForm
from .models import PostModel

def index(request):
    post_form = postForm()

    if request.method == 'POST':
        PostModel.objects.create(
            Name    = request.POST['Name'],
            Email   = request.POST['Email'],
            Mail    = request.POST['Mail']
        )
    
    context = {
        'forms' : post_form
    }
    return render (request, 'blog/index.html', context)

# def list(request):
#     return