from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from .models import Sale
# Forms
from .forms import SalesSearchForm
# from reports.forms import ReportForm
# Pandas
import pandas as pd
# utils
# from .utils import get_customer_from_id, get_salesman_from_id, get_chart

def home_view(request):
    sales_df = None
    positions_df = None
    merged_df = None
    df = None
    chart = None
    no_data = None
    search_form = SalesSearchForm(request.POST or None)
    # report_form = ReportForm()

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        # results_by = request.POST.get('results_by')


    context={
    'search_form': search_form,
    }
    return render(request, 'sales/home.html', context)

# class SaleListView(LoginRequiredMixin, ListView):
#     model = Sale
#     template_name = 'sales/main.html'
#     #context_object_name = 'another_name_object_as_param'

# class SaleDetailView(LoginRequiredMixin, DetailView):
#     model = Sale
#     template_name = 'sales/detail.html'

# This is a function view approach. 
def sale_list_view(request): # use it instead of ListView
    qs = Sale.objects.all()
    return render(request, 'sales/main.html',{"object_list": qs})

def sale_detail_view(request, **kwargs): # use it instead of DetailView
    pk = kwargs.get('pk')
    obj = Sale.objects.get(pk=pk)
    # or
    # obj = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales/detail.html', {"object":obj})