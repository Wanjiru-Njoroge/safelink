from django.shortcuts import render, redirect
from reports.forms import ReportForm
from reports.models import Resource
from reports.forms import ResourceForm





def report_create_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_success')  # Redirect to the success page after form submission
    else:
        form = ReportForm()

    return render(request, 'report.html', {'form': form})

def report_success_view(request):
    return render(request, 'succes.html')

def resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})
def add_resource(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')  # Redirect to the resources list page
    else:
        form = ResourceForm()
    return render(request, 'add_resource.html', {'form': form})

def index(request):
    return render(request, 'index.html')