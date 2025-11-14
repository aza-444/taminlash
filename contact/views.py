from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, Survey, SurveyChoice, SurveyResponse, HelplineStats
from django.http import JsonResponse


def contact_form(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
        return redirect('contact:contact')
    
    return render(request, 'contact/contact.html')


def survey_view(request):
    surveys = Survey.objects.filter(is_active=True).order_by('step_number')
    context = {
        'surveys': surveys,
    }
    return render(request, 'contact/survey.html', context)


def survey_submit(request):
    if request.method == 'POST':
        survey_id = request.POST.get('survey_id')
        choice_id = request.POST.get('choice_id')
        
        survey = Survey.objects.get(id=survey_id)
        choice = SurveyChoice.objects.get(id=choice_id)
        
        ip_address = request.META.get('REMOTE_ADDR')
        
        SurveyResponse.objects.create(
            survey=survey,
            choice=choice,
            ip_address=ip_address
        )
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})
