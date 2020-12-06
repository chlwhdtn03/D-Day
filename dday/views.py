from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta, timezone
from .models import Event, Comment

# Create your views here.
def index(request):
    list = Event.objects.all().order_by('-pub_date')

    for item in list:
        item.days = -(item.offset - datetime.now(timezone.utc)).days-1
        item.time = item.offset.strftime("%Y-%m-%d")

    context = {'list': list}
    return render(request, "dday/index.html", context)


def addEvent(request):
    e = Event(title=request.POST['title'], offset=request.POST['offset'], pub_date=datetime.now(timezone.utc))
    e.save()
    return HttpResponseRedirect(reverse('dday:index'))


def addComment(request):
    event = get_object_or_404(Event, id=request.POST['id'])
    comment = Comment(event=event, text=request.POST['text'], pub_date=datetime.now(timezone.utc))
    comment.save()
    return HttpResponseRedirect(reverse('dday:index') + '#' + str(event.id))


def deleteEvent(request):
    e = get_object_or_404(Event, id=request.POST['id'])
    e.delete()
    return HttpResponseRedirect(reverse('dday:index'))
