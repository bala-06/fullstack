# mous/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MOU, Activity
from .forms import MOUFilterForm
from django.shortcuts import render, redirect
from .forms import MOUUploadForm
from django.db.models import Q
from django.shortcuts import get_object_or_404
def mou_list(request):
    form = MOUFilterForm(request.GET or None)
    mous = MOU.objects.all()
    today = timezone.now().date()

    if form.is_valid():
        department = form.cleaned_data.get('department')
        organization = form.cleaned_data.get('organization')
        outcome = form.cleaned_data.get('outcome')
        status = form.cleaned_data.get('status')

        if department:
            mous = mous.filter(department=department)
        if organization:
            mous = mous.filter(organization=organization)
        if outcome:
            mous = mous.filter(outcomes=outcome)
        if status == 'active':
            mous = mous.filter(end_date__gte=today)
        elif status == 'expired':
            mous = mous.filter(end_date__lt=today)

    active_mous = mous.filter(end_date__gte=today)
    expired_mous = mous.filter(end_date__lt=today)

    return render(request, 'mous/mou_list.html', {
        'form': form,
        'active_mous': active_mous,
        'expired_mous': expired_mous,
    })

def complete_outcome(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == 'POST':
        activity.outcome_completed = True
        activity.status = 'completed'
        activity.save()
        return HttpResponseRedirect(reverse('mou_detail', args=[activity.mou.id]))
def upload_mou(request):
    if request.method == 'POST':
        form = MOUUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mou_list')  # Redirect to MoU list after upload
    else:
        form = MOUUploadForm()

    return render(request, 'mous/upload_mou.html', {'form': form})


def filter_results(request):
    query = Q()
    if 'department' in request.GET:
        query &= Q(department__id__in=request.GET.getlist('department'))
    if 'organization' in request.GET:
        query &= Q(organization_id=request.GET['organization'])
    if 'outcome' in request.GET:
        query &= Q(outcomes__id__in=request.GET.getlist('outcome'))

    filtered_mous = MOU.objects.filter(query).distinct()

    return render(request, 'mous/filter_results.html', {'filtered_mous': filtered_mous})
def edit_mou(request, pk):
    mou = get_object_or_404(MOU, pk=pk)
    if request.method == 'POST':
        form = MOUUploadForm(request.POST, request.FILES, instance=mou)
        if form.is_valid():
            form.save()
            return redirect('filter_results')
    else:
        form = MOUUploadForm(instance=mou)
    return render(request, 'mous/edit_mou.html', {'form': form, 'mou': mou})

def delete_mou(request, pk):
    mou = get_object_or_404(MOU, pk=pk)
    if request.method == 'POST':
        mou.delete()
        return redirect('filter_results')
    return render(request, 'mous/confirm_delete.html', {'mou': mou})