from django.shortcuts import render
from .forms import StudentRegistration,QuestionForm, OptionForm
from .models import User
from .models import Question,Option
from django.shortcuts import get_object_or_404
from .models import Subject


from django.contrib import messages
# Create your views here.
# for index view
def index(request):               
    return render(request,'QuestionPractice/index.html')

# for login page view 
def userlogin(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
             nm=fm.cleaned_data['name']
             ps=fm.cleaned_data['password']
             reg=User(name=nm,password=ps)
             reg.save()
             fm=StudentRegistration()
             print(messages.get_level(request))

    else:
        fm=StudentRegistration()
    stud=User.objects.all()                
    return render(request,'QuestionPractice/userlogin.html',{'form':fm,'stu':stud})

# after login this will show
def afterlogin(request):                
    return render(request,'QuestionPractice/afterlogin.html')



# for mcq_questions html file

def mcq_question_view(request):
    if request.method == "POST":
        selected_options = {}
        for key, value in request.POST.items():
            if key.startswith('answer'):
                question_id = key.replace('answer', '')
                selected_options[int(question_id)] = int(value)
        
        # Calculate total marks
        total_marks = 0
        for question_id, selected_option_id in selected_options.items():
            if Option.objects.get(pk=selected_option_id).is_correct:
                total_marks += 1
        
        # Render template with result
        return render(request,'QuestionPractice/result.html', {'total_marks': total_marks})
    else:
      subject_id = 1
      subject = get_object_or_404(Subject, pk=subject_id)
      questions = Question.objects.filter(subject=subject)
      options = Option.objects.filter(question__subject=subject)
      question_form = QuestionForm()

    #     question_form = QuestionForm()
    # questions = Question.objects.all()
    # options=Option.objects.all()
    
    return render(request, 'QuestionPractice/mcq_question.html', {'question_form': question_form, 'questions': questions,'options':options})

#############################################################################

def mcq_question_Science(request):
    if request.method == "POST":
        selected_options = {}
        for key, value in request.POST.items():
            if key.startswith('answer'):
                question_id = key.replace('answer', '')
                selected_options[int(question_id)] = int(value)
        
        # Calculate total marks
        total_marks = 0
        for question_id, selected_option_id in selected_options.items():
            if Option.objects.get(pk=selected_option_id).is_correct:
                total_marks += 1
        
        # Render template with result
        return render(request,'QuestionPractice/result.html', {'total_marks': total_marks})
    else:
        subject_id = 2
        subject = get_object_or_404(Subject, pk=subject_id)
        questions = Question.objects.filter(subject=subject)
        options = Option.objects.filter(question__subject=subject)
        question_form = QuestionForm()
    
    return render(request, 'QuestionPractice/mcq_question_science.html', {'question_form': question_form, 'questions': questions,'options':options})


###############################################################################


def mcq_question_aptitude(request):
    if request.method == "POST":
        selected_options = {}
        for key, value in request.POST.items():
            if key.startswith('answer'):
                question_id = key.replace('answer', '')
                selected_options[int(question_id)] = int(value)
        
        # Calculate total marks
        total_marks = 0
        for question_id, selected_option_id in selected_options.items():
            if Option.objects.get(pk=selected_option_id).is_correct:
                total_marks += 1
        
        # Render template with result
        return render(request,'QuestionPractice/result.html', {'total_marks': total_marks})
    else:
        subject_id = 3
        subject = get_object_or_404(Subject, pk=subject_id)
        questions = Question.objects.filter(subject=subject)
        options = Option.objects.filter(question__subject=subject)
        question_form = QuestionForm()
    
    return render(request, 'QuestionPractice/mcq_question_aptitude.html', {'question_form': question_form, 'questions': questions,'options':options})


# def submit_mcq(request):
#          return render(request, 'QuestionPractice/result.html')
    