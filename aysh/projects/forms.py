from django.forms import ModelForm
from django import forms
from .models import Submissions, Events, Review

class SubmissionsForm(ModelForm):
    class Meta:
        model = Submissions
        fields = ['title', 'description', 'featured_image', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super(SubmissionsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': name})
    

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'location', 'description', 'featured_image', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(EventsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': name})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input', 'placeholder': 'Add Title'}
        # )

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add your comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
