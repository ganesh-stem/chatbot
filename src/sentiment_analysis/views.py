from django.shortcuts import render, get_object_or_404, redirect
from .forms import SAForm
from .models import SA
from .charts import donut_chart
from django.http import JsonResponse, HttpResponse


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

class SAVariable:
    sa_nirvantika_view = None
    sa_image_view = None

    sa_positive = None
    sa_negative = None
    sa_neutral = None
    sa_compound = None

    sa_output_positive = None
    sa_output_negative = None
    sa_output_neutral = None
    sa_output_compound = None

    sa_list = []
    sa_list2 = []
    def __init__(self, end_result):
        self.end_result = end_result

bot = ChatBot('Buddy') 
bot = ChatBot(
    'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

trainer1 = ChatterBotCorpusTrainer(bot)

# Train based on the english corpus
# trainer1.train("chatterbot.corpus.english")

# Train based on english greetings corpus
# trainer1.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
# trainer1.train("chatterbot.corpus.english.conversations")

trainer = ListTrainer(bot)

trainer.train([
'My name is Nirvantika',
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!',
'chatterbot.corpus.english',
'chatterbot.corpus.english.greetings',
'chatterbot.corpus.english.conversations',
])

sid = SentimentIntensityAnalyzer()

def sa_view(request):
    form = SAForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SAForm()

    try:
        SAVariable.sa_positive = None
        SAVariable.sa_negative = None
        SAVariable.sa_neutral = None
        SAVariable.sa_compound = None

        input_value = None
        output_value = None
        image_url_info = None
        nirvantika_response = None

        field_name = 'input_sentence'
        input_id = SA.objects.latest('id')

        field_object = SA._meta.get_field(field_name)
        input_value = str(field_object.value_from_object(input_id))

        output_value  = sid.polarity_scores(input_value)

        labels = ['Positive', 'Negative', 'Neutral', 'Compound']
        size1 = [abs(output_value['pos']), abs(output_value['neg']), abs(output_value['neu']), abs(output_value['compound'])]
        SAVariable.sa_positive = abs(output_value['pos'])
        SAVariable.sa_negative = abs(output_value['neg'])
        SAVariable.sa_neutral = abs(output_value['neu'])
        SAVariable.sa_compound = abs(output_value['compound'])

        SAVariable.sa_list = [SAVariable.sa_positive * 100, SAVariable.sa_negative* 100, SAVariable.sa_neutral * 100]
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        print(SAVariable.sa_list)
        import json
        SAVariable.sa_list = json.dumps(SAVariable.sa_list)
        print(SAVariable.sa_list)

        nirvantika_response = bot.get_response(input_value)
        output_value  = sid.polarity_scores(str(nirvantika_response))

        SAVariable.sa_output_positive = abs(output_value['pos'])
        SAVariable.sa_output_negative = abs(output_value['neg'])
        SAVariable.sa_output_neutral = abs(output_value['neu'])
        SAVariable.sa_output_compound = abs(output_value['compound'])

        SAVariable.sa_list2 = [SAVariable.sa_output_positive * 100, SAVariable.sa_output_negative * 100, SAVariable.sa_output_neutral * 100]

        size2 = [abs(output_value['pos']), abs(output_value['neg']), abs(output_value['neu']), abs(output_value['compound'])]

        sizes = [size1, size2]
        donut_chart(sizes, colors, labels)
        image_url_info = "/../../../static/sa/images/sa.png"

        SAVariable.sa_nirvantika_view = nirvantika_response
        SAVariable.sa_image_view = "/../../../static/search/bfs/maze.png"
        # BFS.objects.all().delete()

        SA.objects.latest('id').delete()
    except:
        print("Sentiment Analysis: Error in the try statement.")

    context = {
        'form': form, 'input_text': input_value, 'output_text': output_value, 
        'image_url': image_url_info, 'nirvantika': nirvantika_response,
    }
    return render(request, "sentiment_analysis/sa.html", context)


def post_sa_view(request):
    if request.method == "POST" and request.is_ajax():
        sa_view(request)
        return JsonResponse({"success":True}, status=200)
    return JsonResponse({"success":False}, status=400)


def get_sa_view(request):
    if request.method == "GET" and request.is_ajax():
        try:
            final_view = None
            final_view = SAVariable.sa_nirvantika_view
        except:
            print("BFS ERROR: Error in the try session of BFS in view.py")
    return HttpResponse(final_view)

def get_sa_input_view(request):
    if request.method == "GET" and request.is_ajax():
        try:
            image_url_info = None
            image_url_info = SAVariable.sa_list
        except:
            print("BFS ERROR: Error in the try session of BFS in view.py")
    return HttpResponse(image_url_info)


def get_sa_output_view(request):
    if request.method == "GET" and request.is_ajax():
        try:
            image_url_info = None
            image_url_info = SAVariable.sa_list2
        except:
            print("BFS ERROR: Error in the try session of BFS in view.py")
    return HttpResponse(image_url_info)




def get_sa_state_view(request):
    if request.method == "GET" and request.is_ajax():
        try:
            states_view = None
            states_view = SAVariable.sa_list
        except:
            print("BFS ERROR: Error in the try session of BFS in view.py")
    return HttpResponse(states_view)

def get_sa_hash_view(request):
    if request.method == "GET" and request.is_ajax():
        try:
            hash_view = None
            hash_view = SAVariable.hash_value
        except:
            print("BFS ERROR: Error in the try session of BFS in view.py")
    return HttpResponse(hash_view)