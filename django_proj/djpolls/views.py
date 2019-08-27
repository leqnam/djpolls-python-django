from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Answer
from django.utils.translation import ugettext
from .serializers import QuestionSerializer
from rest_framework import viewsets

# def home(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = '<br>'.join([q.question for q in latest_question_list])
#     return HttpResponse(output)

# def home(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('djpolls/home.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:50]
    message = ugettext('Welcome!')
    context = {'latest_question_list': latest_question_list, 'message': message}
    return render(request, 'djpolls/home.html', context)

def login(request):
    return render(request, 'djpolls/login.html')

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return render(request, 'djpolls/404.html')
    return render(request, 'djpolls/detail.html', {'question': question})

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer_set.get(pk=request.POST['choice'])
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'djpolls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('djpolls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'djpolls/result.html', {'question': question})

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer