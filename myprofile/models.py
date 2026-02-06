from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile', unique=True, default=1)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpeg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class Experience(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_link = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField('Skill', blank=True, related_name='experiences')
    def __str__(self):
        return f'{self.title} at {self.company}'


class Education(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=200)

    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_year = models.IntegerField()
    is_current = models.BooleanField(default=False)
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    focus = models.CharField(max_length=200, blank=True, null=True)
    skills = models.ManyToManyField('Skill', blank=True, related_name='educations')
    institution_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.degree} from {self.institution}'

    
class Skill(models.Model):
    type_choices = [
        ('technical', 'Technical'),
        ('soft', 'Soft'),
        ('language', 'Language'),
        ('other', 'Other')]
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    type = models.CharField(max_length=20, choices=type_choices, default='other')
    name = models.CharField(max_length=100)
    self_assesment_percent = models.IntegerField(blank=True, null=True, help_text='Enter a value between 0 and 100')
    months_of_experience = models.FloatField(blank=True, null=True, help_text='Total months of experience with this skill')

    def __str__(self):
        return f'{self.name} ({self.self_assesment_percent}%)'

    
class Project(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    is_alone = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=True)
    
    link = models.URLField(blank=True, null=True)
    # Corrected: Removed on_delete and null=True; pluralized name
    skills = models.ManyToManyField('Skill', blank=True, related_name='projects')

    def __str__(self):
        return self.name

class Certification(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    do_expire = models.BooleanField(default=False)

    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} from {self.issuing_organization}'

class Award(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='awards')
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_received = models.DateField()
    description = models.TextField(blank=True, null=True)
    award_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return f'{self.title} from {self.issuer}'

    
class Language(models.Model):
    level_choices = [
        ('beginner', 'Beginner'),
        ('basic', 'Basic'),
        ('medium', 'Medium'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('native', 'Native Speaker')]
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=50, choices=level_choices)


    def __str__(self):
        return f'{self.name} ({self.proficiency_level})'

    
class Interest(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='interests')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class Reference(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=200)
    contact_information = models.TextField()
    relationship = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.relationship})'

    
class SocialLink(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f'{self.platform}: {self.url}'

    
class Resume(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Resume of {self.profile.username} uploaded at {self.uploaded_at}'

    
class PortfolioItem(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='portfolio_items')
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)

    def __str__(self):
        return self.title

   
class VolunteerExperience(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='volunteer_experiences')
    organization = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.role} at {self.organization}'
