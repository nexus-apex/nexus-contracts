import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Contract, Party, Amendment


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['contract_count'] = Contract.objects.count()
    ctx['contract_service'] = Contract.objects.filter(contract_type='service').count()
    ctx['contract_employment'] = Contract.objects.filter(contract_type='employment').count()
    ctx['contract_nda'] = Contract.objects.filter(contract_type='nda').count()
    ctx['contract_total_value'] = Contract.objects.aggregate(t=Sum('value'))['t'] or 0
    ctx['party_count'] = Party.objects.count()
    ctx['party_client'] = Party.objects.filter(party_type='client').count()
    ctx['party_vendor'] = Party.objects.filter(party_type='vendor').count()
    ctx['party_partner'] = Party.objects.filter(party_type='partner').count()
    ctx['amendment_count'] = Amendment.objects.count()
    ctx['amendment_extension'] = Amendment.objects.filter(amendment_type='extension').count()
    ctx['amendment_modification'] = Amendment.objects.filter(amendment_type='modification').count()
    ctx['amendment_termination'] = Amendment.objects.filter(amendment_type='termination').count()
    ctx['recent'] = Contract.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def contract_list(request):
    qs = Contract.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(contract_type=status_filter)
    return render(request, 'contract_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def contract_create(request):
    if request.method == 'POST':
        obj = Contract()
        obj.title = request.POST.get('title', '')
        obj.party = request.POST.get('party', '')
        obj.contract_type = request.POST.get('contract_type', '')
        obj.value = request.POST.get('value') or 0
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/contracts/')
    return render(request, 'contract_form.html', {'editing': False})


@login_required
def contract_edit(request, pk):
    obj = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.party = request.POST.get('party', '')
        obj.contract_type = request.POST.get('contract_type', '')
        obj.value = request.POST.get('value') or 0
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/contracts/')
    return render(request, 'contract_form.html', {'record': obj, 'editing': True})


@login_required
def contract_delete(request, pk):
    obj = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/contracts/')


@login_required
def party_list(request):
    qs = Party.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(party_type=status_filter)
    return render(request, 'party_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def party_create(request):
    if request.method == 'POST':
        obj = Party()
        obj.name = request.POST.get('name', '')
        obj.contact_person = request.POST.get('contact_person', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.party_type = request.POST.get('party_type', '')
        obj.active_contracts = request.POST.get('active_contracts') or 0
        obj.save()
        return redirect('/parties/')
    return render(request, 'party_form.html', {'editing': False})


@login_required
def party_edit(request, pk):
    obj = get_object_or_404(Party, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.contact_person = request.POST.get('contact_person', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.party_type = request.POST.get('party_type', '')
        obj.active_contracts = request.POST.get('active_contracts') or 0
        obj.save()
        return redirect('/parties/')
    return render(request, 'party_form.html', {'record': obj, 'editing': True})


@login_required
def party_delete(request, pk):
    obj = get_object_or_404(Party, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/parties/')


@login_required
def amendment_list(request):
    qs = Amendment.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(contract_title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(amendment_type=status_filter)
    return render(request, 'amendment_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def amendment_create(request):
    if request.method == 'POST':
        obj = Amendment()
        obj.contract_title = request.POST.get('contract_title', '')
        obj.amendment_type = request.POST.get('amendment_type', '')
        obj.effective_date = request.POST.get('effective_date') or None
        obj.description = request.POST.get('description', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/amendments/')
    return render(request, 'amendment_form.html', {'editing': False})


@login_required
def amendment_edit(request, pk):
    obj = get_object_or_404(Amendment, pk=pk)
    if request.method == 'POST':
        obj.contract_title = request.POST.get('contract_title', '')
        obj.amendment_type = request.POST.get('amendment_type', '')
        obj.effective_date = request.POST.get('effective_date') or None
        obj.description = request.POST.get('description', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/amendments/')
    return render(request, 'amendment_form.html', {'record': obj, 'editing': True})


@login_required
def amendment_delete(request, pk):
    obj = get_object_or_404(Amendment, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/amendments/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['contract_count'] = Contract.objects.count()
    data['party_count'] = Party.objects.count()
    data['amendment_count'] = Amendment.objects.count()
    return JsonResponse(data)
