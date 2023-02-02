from .models import Tag, Submissions, Events
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateSubmissions(request, submissions, results):

    page = request.GET.get('page')
    results = 4
    paginator = Paginator(submissions, results)
    try:
        submissions = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        submissions = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        submissions = paginator.page(page)
    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    custom_range = range(leftIndex, rightIndex)

    return custom_range, submissions


def searchSubmissions(request):

    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    submissions = Submissions.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return submissions, search_query

def searchEvents(request):

    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    events = Events.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return events, search_query