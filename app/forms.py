from django import forms
from django.forms import ModelForm
from .models import Video, Sequence, Comment
from durationwidget.widgets import TimeDurationWidget

class VideoForm(ModelForm):

    length = forms.DurationField(widget=TimeDurationWidget(show_days=False), required=False)

    class Meta:
        model = Video
        fields = ['title','description','length','path']
