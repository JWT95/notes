from django.http import HttpResponse, HttpResponseRedirect
from .models import Note
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


def index(request):
    posts = Note.objects.order_by('-pub_date__date', '-likes')
    context = {
        'notes': posts,
    }
    return HttpResponse(render(request, 'notes/index.html', context))


def like(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.likes += 1
    note.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('notes:index'))


def post(request):

    try:
        note = request.POST['note']
        note = Note(note=note)
        note.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('notes:index'))
    except (KeyError, Note.DoesNotExist):
        return HttpResponse("You shouldn't be here")
