from django.shortcuts import render

finches = [
  {'name': 'Felix', 'species': 'Zebra Finch', 'description': 'Small and social finch species.', 'age': 1},
  {'name': 'Penny', 'species': 'Gouldian Finch', 'description': 'Colorful and vibrant finch species.', 'age': 2},
  {'name': 'Oliver', 'species': 'Society Finch', 'description': 'Hardy and adaptable finch species.', 'age': 3},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })