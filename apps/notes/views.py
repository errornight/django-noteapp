from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import AddNote, EditNote

def home(request):
    if request.user.is_authenticated:
        return redirect('NotesPage')
    return render(request, 'notes/home.html')

@login_required
def notes_page(request):
    notes = Note.objects.filter(owner=request.user).order_by('-updated')

    context = {'notes': notes}
    return render(request, 'notes/notes.html', context)

@login_required()
def note_page(request, username, uuid):
    note = get_object_or_404(Note, uuid=uuid, owner__username=username)
    if not request.user == note.owner and not note.public:
        raise Http404('Page not found!')

    context = {'note': note}
    return render(request, 'notes/note.html', context)
@login_required()
def add_note(request):
    form = AddNote()
    message = None
    if request.method == 'POST':
        form = AddNote(request.POST)
        if form.is_valid():
            note = Note.objects.create(title=form.cleaned_data['title'],
                                       body=form.cleaned_data['body'],
                                       short_desc=form.cleaned_data['short_desc'],
                                       category_id=form.cleaned_data['category'],
                                       public=form.cleaned_data['public'],
                                       owner=request.user)
            note.save()
            return redirect('NotePage', note.owner, note.uuid)

    context = {'form': form, 'message': message}
    return render(request, 'notes/add_note.html', context)

@login_required()
def delete_note(request, username, uuid):
    note = get_object_or_404(Note, uuid=uuid, owner__username=username)
    if not request.user == note.owner and not note.public:
        raise Http404('Page not found!')

    if request.method == 'GET':
        if request.GET.get('confirm'):
            note.delete()
            return redirect('NotesPage')

    message = f'deleting "{note.title}"'
    past_page = request.META.get("HTTP_REFERER") or '/'
    context = {'message': message, 'past_page': past_page}

    return render(request, 'confirmation.html', context)

@login_required()
def edit_note(request, username, uuid):
    note = get_object_or_404(Note, uuid=uuid, owner__username=username)
    form = EditNote(instance=note)
    past_page = request.META.get("HTTP_REFERER") or '/'

    if not request.user == note.owner and not note.public:
        raise Http404('Page not found!')

    if request.method == 'POST':
        form = EditNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('NotePage', note.owner, note.uuid)

    context = {'form': form, 'past_page':past_page}
    return render(request, 'notes/edit_note.html', context)