from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show

def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)


def new(request):
    return render(request, 'add_new_show.html')


def create(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')

        else:

            new_show = Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                description=request.POST['description'],
                )
            messages.success(request, "Show successfully created")
        return redirect(f'/shows/{new_show.id}/show')
            
    return redirect('/show/new')


def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'tv_show.html', context)


def edit(request, show_id):
    if request.method == 'GET':
        one_show = Show.objects.get(id=show_id)
        context = {
            'show': one_show
        }
    return render(request, 'edit_show.html', context)


def update(request, show_id):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{{show.id}}/edit')
        else:
            show = Show.objects.get(id=show_id)
            show.title = request.POST['title']
            show.release_date = request.POST['release_date']
            show.network = request.POST['network']
            show.description = request.POST['description']
            show.save()

    return redirect('/')


def delete(request, show_id):
    if request.method == 'POST':
        show_to_delete = Show.objects.get(id=show_id)
        show_to_delete.delete()
    return redirect('/')