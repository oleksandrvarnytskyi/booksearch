from django.shortcuts import render


def search_handler(request):
    if request.GET:
        q = request.GET.get('q')
        email = request.GET.get('email')
        return render(
            request,
            'books/processing_started.html',
            {'email': email}
        )
    return render(request, 'main.html')
