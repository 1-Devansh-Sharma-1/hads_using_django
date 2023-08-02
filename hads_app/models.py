# hads_app/models.py

from django.db import models

class HADSQuestion(models.Model):
    ANXIETY = 'ANX'
    DEPRESSION = 'DEP'
    SUBSCALE_CHOICES = [
        (ANXIETY, 'Anxiety'),
        (DEPRESSION, 'Depression'),
    ]

    subscale = models.CharField(max_length=3, choices=SUBSCALE_CHOICES)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.subscale} Question: {self.text}"


class HADSChoice(models.Model):
    question = models.ForeignKey(HADSQuestion, on_delete=models.CASCADE, related_name='choices')
    value = models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')])
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.question.text} - Option {self.value}: {self.text}"


class HADSTestResult(models.Model):
    user_name = models.CharField(max_length=100, blank=True, null=True)
    anxiety_scores = models.IntegerField(default=0)
    depression_scores = models.IntegerField(default=0)
    date_completed = models.DateTimeField(auto_now_add=True)
    mood_rating = models.IntegerField(default=0)

    def __str__(self):
        return f"HADS Test Result {self.id}"
    
class SubjectiveQuestion(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
class SubjectiveResponse(models.Model):
    test_result = models.ForeignKey(HADSTestResult, on_delete=models.CASCADE, null=True, default=None)
    question = models.ForeignKey(SubjectiveQuestion, on_delete=models.CASCADE)
    response = models.TextField()

    def __str__(self):
        return f"Response for {self.question} in Test Result {self.test_result}"


    

