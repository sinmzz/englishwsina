from django.shortcuts import render
from .models import FlashCard


# Create your views here.
def index(request):
    return render(request, 'index.html', context={})


def lookup(request):
    context = {}
    return render(request, template_name='lookup.html', context=context)


def flashcard(request):
    userInput = request.GET['userInput']
    word = FlashCard.objects.get(word__contains=userInput)
    context = {'word': word}
    return render(request, template_name='flashcard.html', context=context)


def newcard(request):
    if request.method == 'POST':
        card = FlashCard()
        card.word = request.POST['word']
        card.part = request.POST['part']
        card.definition = request.POST['definition']
        card.example = request.POST['example']
        card.collocation = request.POST['collocation']
        card.save()
    return render(request, template_name='newcard.html', context={})
