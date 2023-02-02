from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Submissions, Events, Tag
from .forms import SubmissionsForm, EventsForm, ReviewForm
from .utils import searchSubmissions, searchEvents, paginateSubmissions
# Create your views here.

def home(request):
    return render(request, 'projects/home.html')

def submissions(request):
    submissions, search_query = searchSubmissions(request)
    custom_range, submissions = paginateSubmissions(request, submissions, 6)
    context = {'submissions': submissions, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/submissions.html', context)

@login_required(login_url='login')
def submission(request, pk):
    submissionObj = Submissions.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.submission = submissionObj
        review.owner = request.user.profile
        review.save()

        submissionObj.getVoteCount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('submission', pk=submissionObj.id)
    tags = submissionObj.tags.all()
    return render(request, 'projects/single-submission.html', {'submission': submissionObj, 'tags':tags, 'form': form})

def events(request):
    events, search_query = searchEvents(request)
    context = {'events': events, 'search_query': search_query}
    return render(request, 'projects/events.html', context)

@login_required(login_url='login')
def event(request, pk):
    eventObj = Events.objects.get(id=pk)
    tags = eventObj.tags.all()
    return render(request, 'projects/single-event.html', {'event': eventObj, 'tags': tags})

@login_required(login_url='login')
def createSubmission(request):
    profile = request.user.profile
    form = SubmissionsForm()
    if request.method == 'POST':
        form = SubmissionsForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.owner = profile
            submission.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateSubmission(request, pk):
    profile = request.user.profile
    submission = profile.submissions_set.get(id=pk)
    form = SubmissionsForm(instance=submission)
    if request.method == 'POST':
        form = SubmissionsForm(request.POST, request.FILES, instance=submission)
        if form.is_valid:
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteSubmission(request, pk):
    profile = request.user.profile
    submission = profile.submissions_set.get(id=pk)
    if request.method == 'POST':
        submission.delete()
        return redirect('account')
    context = {'object': submission}
    return render(request, 'delete_template.html', context)

@login_required(login_url='login')
def createEvent(request):
    profile = request.user.profile
    form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = profile
            event.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateEvent(request, pk):
    profile = request.user.profile
    event = profile.events_set.get(id=pk)
    form = EventsForm(instance=event)
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES, instance=event)
        if form.is_valid:
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteEvent(request, pk):
    profile = request.user.profile
    event = profile.events_set.get(id=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('account')
    context = {'object': submission}
    return render(request, 'delete_template_event.html', context)