from django.shortcuts import render, redirect, get_object_or_404
from .models import MOU, Event
from .forms import MOUForm
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import date
from .models import MOU, Department, Outcome
from django.db.models import Prefetch
from .forms import EventForm
from .forms import MOUFilterForm
def filter_mou(request):
    form = MOUFilterForm(request.GET or None)
    mous = MOU.objects.all()

    # Apply filters
    if form.is_valid():
        if form.cleaned_data['title']:
            mous = mous.filter(title__icontains=form.cleaned_data['title'])
        if form.cleaned_data['organization_name']:
            mous = mous.filter(organization_name__icontains=form.cleaned_data['organization_name'])
        if form.cleaned_data['department']:
            mous = mous.filter(department=form.cleaned_data['department'])
        if form.cleaned_data['outcome']:
            mous = mous.filter(outcome=form.cleaned_data['outcome'])
        if form.cleaned_data['status']:
            mous = mous.filter(status=form.cleaned_data['status'])
        if form.cleaned_data['start_date']:
            mous = mous.filter(start_date__gte=form.cleaned_data['start_date'])
        if form.cleaned_data['end_date']:
            mous = mous.filter(end_date__lte=form.cleaned_data['end_date'])

    return render(request, 'mou/filter_mou.html', {'form': form, 'mous': mous})
def add_event(request, mou_id):
    mou = get_object_or_404(MOU, id=mou_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.mou = mou
            event.save()
            return redirect('view_mou', mou_id=mou.id)
    else:
        form = EventForm()
    return render(request, 'mou/add_event.html', {'form': form, 'mou': mou})
def group_mous_by_department(mous):
    departments = Department.objects.filter(mous__in=mous).distinct()
    grouped = []
    for department in departments:
        grouped.append({
            'department_name': department.name,
            'mous': mous.filter(department=department),
        })
    return grouped

def mou_list(request):
    today = date.today()
    active_mous = MOU.objects.filter(end_date__gte=today).prefetch_related('department', 'outcome')
    expired_mous = MOU.objects.filter(end_date__lt=today).prefetch_related('department', 'outcome')

    active_mous_by_department = group_mous_by_department(active_mous)
    expired_mous_by_department = group_mous_by_department(expired_mous)

    return render(request, 'mou/mou_list.html', {
        'active_mous_by_department': active_mous_by_department,
        'expired_mous_by_department': expired_mous_by_department,
    })
def create_mou(request):
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mou_list')
    else:
        form = MOUForm()
    return render(request, 'mou/create_mou.html', {'form': form})


def view_mou(request, mou_id):
    mou = get_object_or_404(MOU.objects.prefetch_related('department', 'outcome'), id=mou_id)
    events = mou.events.all()
    department = ', '.join([dept.name for dept in mou.department.all()])
    outcome = ', '.join([out.name for out in mou.outcome.all()])

    return render(request, 'mou/view_mou.html', {
        'mou': mou,
        'events': events,
        'department': department,
        'outcome': outcome,
    })
def edit_mou(request, mou_id):
    mou = get_object_or_404(MOU, id=mou_id)
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES, instance=mou)
        if form.is_valid():
            form.save()
            return redirect('mou_list')
    else:
        form = MOUForm(instance=mou)
    return render(request, 'mou/edit_mou.html', {'form': form, 'mou': mou})

def delete_mou(request, mou_id):
    mou = get_object_or_404(MOU, id=mou_id)
    mou.delete()
    return redirect('mou_list')

def edit_event(request, event_id):
    print(f"Edit Event View Called for Event ID: {event_id}")
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        print("POST request received.")
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            
            print("Form is valid. Saving changes...")
            form.save()
            print("Event saved. Redirecting to view_event.")
            id=event_id
            mou_id = event.mou.id
            return redirect('view_mou', mou_id=mou_id)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = EventForm(instance=event)
    return render(request, 'mou/edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    mou_id = event.mou.id
    event.delete()
    return redirect('view_mou', mou_id=mou_id)

