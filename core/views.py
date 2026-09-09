from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Note


def home_view(request):
  return render(request, 'home.html')


def notes_list_view(request):
  notes = Note.objects.all()
  return render(request, 'notes_list.html', {'notes': notes})


def class_notes_view(request, class_name):
  notes = Note.objects.filter(student_class=class_name)
  return render(
      request, 'class_notes.html', {'notes': notes, 'class_name': class_name}
  )


def register_view(request):
  return render(request, 'register.html')


@csrf_exempt
def custom_login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      return render(
          request,
          'login.html',
          {'error': 'ইউজারনেম অথবা পাসওয়ার্ড ভুল হয়েছে!'},
      )
  return render(request, 'login.html')


def logout_view(request):
  logout(request)
  return redirect('home')


def profile_view(request):
  return render(request, 'profile.html')


def toggle_favorite(request, note_id):
  return redirect('home')


def admin_dashboard(request):
  notes = Note.objects.all()
  return render(request, 'admin_dashboard.html', {'notes': notes})


def add_note_view(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    student_class = request.POST.get('student_class')
    subject = request.POST.get('subject')
    description = request.POST.get('description')
    pdf_file = request.FILES.get('pdf_file')

    Note.objects.create(
        title=title,
        student_class=student_class,
        subject=subject,
        description=description,
        pdf_file=pdf_file,
    )
    return redirect('admin_dashboard')
  return render(request, 'add_note.html')


def edit_note_view(request, note_id):
  note = get_object_or_404(Note, id=note_id)
  if request.method == 'POST':
    note.title = request.POST.get('title')
    note.student_class = request.POST.get('student_class')
    note.subject = request.POST.get('subject')
    note.description = request.POST.get('description')
    if request.FILES.get('pdf_file'):
      note.pdf_file = request.FILES.get('pdf_file')
    note.save()
    return redirect('admin_dashboard')
  return render(request, 'edit_note.html', {'note': note})


def delete_note_view(request, note_id):
  note = get_object_or_404(Note, id=note_id)
  note.delete()
  return redirect('admin_dashboard')