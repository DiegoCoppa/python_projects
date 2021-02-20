#from django.shortcuts import render

# Create your views here.

"""

A view function, or view for short, is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response. This code can live anywhere you want, as long as it’s on your Python path. There’s no other requirement–no “magic,” so to speak. For the sake of putting the code somewhere, the convention is to put views in a file called views.py, placed in your project or application directory.


"""

from django.http import Http404

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.urls import reverse

from django.views import generic

from .models import Choice, Question

def vote(request, question_id): #>11< recibo como parámetor la pregunta a la que elegí la opción
    question = get_object_or_404(Question, pk=question_id)
    try:#>12< hay que ver el voto elegido que fue modificado por un post
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#y mevoyy>12<)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
"""
def index(request): #>3< sigue acá
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}# diccionario
    #print (context)
    return render(request, 'polls/index.html', context) #>4< el usuario elige uno de las cinco opciones en el contexto de index.html
#es mucho más facil...
"""
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #solo cinco preguntas ordenadas, la mas reciente primero
    #print(latest_question_list) #<QuerySet [<Question: 089076?>, <Question: bvcxz?>, <Question: trewq??>, <Question: qwert?>, <Question: wtf?>]>
    #print(latest_question_list[1])
    template = loader.get_template('polls/index.html') # le paso las variables de la función 
    #print (template) #<django.template.backends.django.Template object at 0x7f3a5ac54b80> en template se guarda lo que va al html una vez pasado por el index.html
    context = { #genero la lista llamada context
        'latest_question_list': latest_question_list,
    }
    #print(context)
    return HttpResponse(template.render(context, request)) #pero devuelve la página que vemos

"""
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
"""

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id) # elijo una pregunta, la que me pasan por la url
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

"""
"""
def detail(request, question_id): #>6< recibe como parámetro la pregunta
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) #>7< y devuelve el detail.html 

"""
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


"""
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""






