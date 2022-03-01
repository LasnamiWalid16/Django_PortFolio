from django.shortcuts import render,HttpResponse
from jobs.models import Job

def AllJobs(request):

    jobs = Job.objects.all()
    context={'jobs': jobs}
    return render(request, 'jobs/home.html',context)