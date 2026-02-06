from urllib import request
from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import render, get_object_or_404
from .models import UserProfile  # adjust import according to your app structure

def profile_home(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    context = {
        'profile': profile,
        'experiences': profile.experiences.order_by('-is_current', '-start_date'),
        'educations': profile.educations.order_by('-is_current', '-start_year'),
        'skills': profile.skills.order_by('-self_assesment_percent'),
        'projects': profile.projects.filter(is_public=True).order_by('-is_finished', 'name'),
        'certifications': profile.certifications.order_by('-issue_date'),
        'awards': profile.awards.order_by('-date_received'),
        'languages': profile.languages.all(),
        'interests': profile.interests.all(),
        'social_links': profile.social_links.all(),
        'volunteer_experiences': profile.volunteer_experiences.order_by('-start_date'),
        # Add portfolio_items, references, resumes if you want to show them
    }
    return render(request, 'myprofile/home.html', context)