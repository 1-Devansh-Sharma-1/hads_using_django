# hads_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HADSQuestion, HADSChoice, HADSTestResult, SubjectiveQuestion, SubjectiveResponse

def title_page(request):
    return render(request, 'hads_app/title_page.html')

def hads_test(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        mood_rating = request.POST.get("mood_rating", "")
        anxiety_score = 0
        depression_score = 0

        for question in HADSQuestion.objects.all():
            selected_choice = request.POST.get(f'{question.subscale}_{question.id}')
            if selected_choice:
                try:
                    choice_id = int(selected_choice.split('_')[-1])
                    choice = question.choices.get(id=choice_id)
                    if question.subscale == HADSQuestion.ANXIETY:
                        anxiety_score += choice.value
                    elif question.subscale == HADSQuestion.DEPRESSION:
                        depression_score += choice.value
                except (ValueError, HADSChoice.DoesNotExist, IndexError):
                    pass
        
        # Process subjective questions' responses
        for question in SubjectiveQuestion.objects.all():
            response = request.POST.get(str(question.id))
            if response:
                # Save the response in the database
                SubjectiveResponse.objects.create(question=question, response=response)

        test_result = HADSTestResult.objects.create(
            user_name=user_name,
            mood_rating=mood_rating,
            anxiety_scores=anxiety_score,
            depression_scores=depression_score
        )
        return redirect('result', test_result_id=test_result.id)

    # Query both HADS and Subjective Questions
    hads_questions = HADSQuestion.objects.all()
    subjective_questions = SubjectiveQuestion.objects.all()
    
    return render(request, 'hads_app/hads_test.html', {
        'hads_questions': hads_questions,
        'subjective_questions': subjective_questions
    })

def hads_result(request, test_result_id):
    try:
        test_result = HADSTestResult.objects.get(id=test_result_id)
        return render(request, 'hads_app/hads_result.html', {'test_result': test_result})
    except HADSTestResult.DoesNotExist:
        return HttpResponse("Test result not found.")
