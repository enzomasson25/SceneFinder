from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from .models import Video, Sequence, Comment
from django.template import loader
from app.forms import VideoForm
from django.db.models import Q


def get_videos(request):
    list_video = Video.objects.all()
    template = loader.get_template('app/videos.html')
    context = {
        'list_video': list_video,
    }
    return HttpResponse(template.render(context, request))


def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VideoForm()

    context = {
        'form': form,
    }

    return render(request, 'app/add_video.html', context)


def search(request):
    query = request.GET.get("q")
    if query == None or query == "":
        list_sequences = Sequence.objects.all()
    else:
        list_sequences = Sequence.objects.filter(Q(comment__content__icontains=query))
        
    context = {
        'query': query,
        'list_sequences': list_sequences,
    }

    return render(request, 'app/search.html', context)



def get_video(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    template = loader.get_template('app/video.html')
    context = {
        'video': video,
    }
    return HttpResponse(template.render(context, request))