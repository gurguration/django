from django.shortcuts import render,redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.

def home(request):
    entries =  Entry.objects.all()
    context = {
        'entries': entries
    }
    return render(request, 'diary/index.html', context)

def add(request):
    #print(my_form.fields['text'].attrs)
    if request.method == "POST":
        my_form = EntryForm(request.POST)
        print('request received')
        print(my_form)
        if my_form.is_valid():
            my_form.save()
            return redirect('diary:home')
    else:
        my_form = EntryForm()

    context = {
        'my_form': my_form
    }
    print('skipped if')
    return render(request, 'diary/raw.html', context)