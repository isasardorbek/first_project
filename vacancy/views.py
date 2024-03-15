from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.models import CustomUser
from candidate.models import Profile, Click
from vacancy.models import Vacancy


@login_required(login_url='/login')
# Create your views here.
def employer_view(request):
        user = request.user
        profiles = Profile.objects.all()
        return render(request, 'profiles.html', context={'profiles': profiles,'user': user})

def employer_detail(request, id):
        try:
                profile = Profile.objects.get(id=id)
        except Profile.DoesNot:
                return HttpResponse("Bunday foydalanuvchi yo'q")
        return render(request, 'profile_detail.html', context={'profile': profile})

def new_job(request, id):
        try:
                job_poster = CustomUser.objects.get(pk=id)
        except CustomUser.DoesNotExist:
                return HttpResponse("Bunday foydalanuvchi yo'q")
        if request.method == 'POST':
                Vacancy.objects.create(
                        job_poster=job_poster,
                        location=request.POST.get('location'),
                        min_exp=request.POST.get('min_exp'),
                        max_exp=request.POST.get('max_exp'),
                        title=request.POST.get('title'),
                        type_remote=request.POST.get('type_remote'),
                        type_work=request.POST.get('type_work'),
                        level=request.POST.get('level'),
                        description=request.POST.get('description'),
                        tags=request.POST.get('tags')
                )
                return redirect('/vacancy')
        return render(request, 'new_job.html')

def my_job(request, id):
        try:
                job_poster = CustomUser.objects.get(pk=id)
        except CustomUser.DoesNotExist:
                return HttpResponse("Bunday foydalanuvchi yo'q")
        vacancies = Vacancy.objects.filter(job_poster=job_poster)
        return render(request, 'my_job.html', context={'vacancies': vacancies})

def clicks(request, id):
        clicks = Click.objects.filter(vacancy=id)
        return render(request, 'clicks.html', context={'clicks': clicks})