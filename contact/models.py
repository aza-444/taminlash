from django.db import models


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.subject}"


class Survey(models.Model):
    question = models.CharField(max_length=500)
    step_number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['step_number']
    
    def __str__(self):
        return f"Step {self.step_number}: {self.question}"


class SurveyChoice(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.choice_text


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='responses')
    choice = models.ForeignKey(SurveyChoice, on_delete=models.CASCADE, related_name='responses')
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    
    def __str__(self):
        return f"Response to {self.survey.question}"


class HelplineStats(models.Model):
    total_calls = models.IntegerField(default=0)
    rating_5 = models.IntegerField(default=0)
    rating_4 = models.IntegerField(default=0)
    rating_3 = models.IntegerField(default=0)
    rating_2 = models.IntegerField(default=0)
    rating_1 = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Helpline Statistics"
    
    def __str__(self):
        return f"Helpline Stats - {self.total_calls} total calls"
