from django.shortcuts import render, redirect


from .models import feedback
from .forms import feedbackForm


# Create your views here.

def index(request):
    return render(request, 'cvapp/index.html')


def home(request):
    
    form = feedbackForm()
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            msg=form.save(commit=False)
            msg.save()
            return redirect('thnx')
        
    msg = feedback.objects.all()

    context ={'form':form,'data':msg}
    return render(request, 'cvapp/Home.html', context)

def thanks(request):

    context = {}
    return render(request, 'cvapp/tnx.html', context)


