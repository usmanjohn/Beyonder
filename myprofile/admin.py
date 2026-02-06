from django.contrib import admin

from .models import UserProfile, Experience, Education, Skill, Project, Language, Interest, Award, Certification

admin.site.register([UserProfile, Experience, Education, Skill, Project, Language, Interest, Award, Certification])
# Register your models here.
