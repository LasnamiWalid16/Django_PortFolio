from django.shortcuts import render,HttpResponse,get_object_or_404
from jobs.models import Job

def AllJobs(request):

    jobs = Job.objects.all()
    context={'jobs': jobs}
    return render(request, 'jobs/home.html',context)

def detail(request, job_id):
    job_detail = get_object_or_404(Job,pk=job_id)
    return render(request, 'jobs/detail.html',{'job':job_detail})
