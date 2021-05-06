from django.shortcuts import render


def home_view(request):
    return render(request, 'Main/index.html')

def marketplace(request):
    return render(request, 'Main/marketplace.html')

def coming(request):
    html = "<html><body>Coming Soon.</body></html>"
    return HttpResponse(html)