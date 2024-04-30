# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Folder, Task
from .forms import FolderForm

def index(request, id):
    #すべてのフォルダを取得する
    folders = Folder.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    #選ばれたフォルダを取得する
    current_folder = get_object_or_404(Folder, id=id)
    #選ばれたフォルダのタスクを取得する
    tasks = Task.objects.filter(folder_id=current_folder.id)

    return render(request, 'index.html', {
        'folders': folders,
        'tasks': tasks,
        'current_folder_id': current_folder.id,
    })

def create_folder(request):
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.created_at = timezone.now()
            folder.save()
            return redirect('tasks.index', id=folder.id)
    else:
        form = FolderForm()
    return render(request, 'create_folders.html', {'form': form})
