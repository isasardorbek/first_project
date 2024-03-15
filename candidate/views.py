from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.models import CustomUser
from candidate.models import Click, Profile
from vacancy.models import Vacancy


def candidate_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'candidate.html', context={'jobs': vacancies})


@login_required(login_url='/login')
def job_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return HttpResponse("Bunday vakansiya yo'q", status=404)
    if request.method == 'POST':
        click_text = request.POST.get('click_text')
        try:
            profile = Profile.objects.filter(account=request.user).first()

        except Profile.DoesNotExist:
            return HttpResponse("Bunday profil yo'q", status=404)
        if profile:
            Click.objects.create(
                vacancy=vacancy,
                text=click_text,
                profile=profile
            )
            messages.add_message(request, messages.INFO, "Your application submitted successfully!")
        else:
            messages.add_message(request, messages.INFO, "First, complete your profile, before submitting application!")
    return render(request, 'vacancy.html', context={'job': vacancy, 'messages': messages})