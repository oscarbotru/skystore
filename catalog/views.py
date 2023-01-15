from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('contact_form.txt', 'w+') as form_file:
            form_file.write(f'{name};{phone};{message}')
    return render(request, 'catalog/contacts.html')
