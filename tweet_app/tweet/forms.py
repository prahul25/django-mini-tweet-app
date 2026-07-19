from django import forms
from .models import Tweet

class TweetForm():
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        