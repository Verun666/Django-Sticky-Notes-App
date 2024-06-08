from django.test import TestCase
from django.urls import reverse
from .models import StickyNotes


# Create your tests here.
class NotesAppTest(TestCase):
    def setUp(self):
        self.note = StickyNotes.objects.create(
            title='Test Note',
            content='This is a test note.',
            author='Test Author'
        )

    # Test the view_note view.
    def test_view_note(self):
        response = self.client.get(reverse('view_note', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')

    # Test the add_note view.
    def test_add_note(self):
        response = self.client.post(reverse('add_note'), {
            'author': 'Author Name',
            'title': 'New Note Title',
            'content': 'Content of the new note.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(StickyNotes.objects.filter(title='New Note Title')
                        .exists())

    # Test the edit_note view.
    def test_edit_note(self):
        note = StickyNotes.objects.create(
            author='Author Name',
            title='Old Title',
            content='Old Content'
        )
        response = self.client.post(reverse('edit_note', args=[note.id]), {
            'author': 'Author Name',
            'title': 'Updated Title',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Title')
        self.assertEqual(note.content, 'Updated Content')

    # Test the delete_note view.
    def test_delete_note(self):
        note = StickyNotes.objects.create(
            author='Author Name',
            title='Title to be deleted',
            content='Content to be deleted'
        )
        response = self.client.post(reverse('delete_note', args=[note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(StickyNotes.objects.filter(id=note.id).exists())
