from django.shortcuts import render


context = {
  'blog title': 'Khmer Web MyTV'
}

def index(request):
    return render(request, 'index.html', context=context)
