# admin.py

from django.contrib import admin
from .models import HADSQuestion, HADSChoice, HADSTestResult, SubjectiveQuestion, SubjectiveResponse
from .forms import HADSQuestionAdminForm, SubjectiveQuestionForm

class HADSChoiceInline(admin.TabularInline):
    model = HADSChoice
    extra = 4  # Set the number of choices to show for each question (0 to 3)

class HADSQuestionAdmin(admin.ModelAdmin):
    form = HADSQuestionAdminForm
    inlines = [HADSChoiceInline]

admin.site.register(HADSQuestion, HADSQuestionAdmin)

class SubjectiveQuestionAdmin(admin.ModelAdmin):
    form = SubjectiveQuestionForm

admin.site.register(SubjectiveQuestion, SubjectiveQuestionAdmin)

class SubjectiveResponseInline(admin.TabularInline):
    model = SubjectiveResponse
    extra = 0
    readonly_fields = ['question', 'response']

class HADSTestResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'mood_rating', 'anxiety_scores', 'depression_scores', 'date_completed']
    list_filter = ['date_completed']
    search_fields = ['user_name']
    # inlines = [SubjectiveResponseInline]

admin.site.register(HADSTestResult, HADSTestResultAdmin)

class SubjectiveResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'test_result', 'question', 'response']

admin.site.register(SubjectiveResponse, SubjectiveResponseAdmin)




