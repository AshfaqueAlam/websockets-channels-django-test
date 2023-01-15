from django.shortcuts import render

# Create your views here.

def HomeView(request):
    # ! instead of rendering, fetch from Logs model and show response. using authenticated drf. and authenticated 2x users websockets data update realtime.
    return render(request, 'index.html')
