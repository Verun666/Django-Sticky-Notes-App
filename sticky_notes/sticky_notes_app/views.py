from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNotes


# Create your views here.
def index(request):
    notes = StickyNotes.objects.all()
    context = {
        'notes': notes,
        'page_title': 'All Notes',
    }
    return render(request, "sticky_notes_app/index.html", context)


def add_note(request):
    if request.method == "POST":
        author = request.POST.get("author")
        title = request.POST.get("title")
        content = request.POST.get("content")
        # Below is the ORM to create a new note record in the StickyNotes
        # table.
        StickyNotes.objects.create(author=author, title=title, content=content)
        # When done, return to the index.html page
        return redirect("index")
    return render(request, "sticky_notes_app/add_note.html")


def view_note(request, post_id):
    note = get_object_or_404(StickyNotes, id=post_id)
    return render(request, "sticky_notes_app/view_note.html", {"note": note})


def edit_note(request, post_id):
    note = get_object_or_404(StickyNotes, id=post_id)
    if request.method == "POST":
        author = request.POST.get("author")
        title = request.POST.get("title")
        content = request.POST.get("content")
        # Update the StickyNotes record.
        note.author = author
        note.title = title
        note.content = content
        note.save()
        # Redirect to the view_note page.
        return redirect("view_note", post_id=post_id)
    return render(request, "sticky_notes_app/edit_note.html", {"note": note})


def delete_note(request, post_id):
    note = get_object_or_404(StickyNotes, id=post_id)
    note.delete()
    return redirect('index')
