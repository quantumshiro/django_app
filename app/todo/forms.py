from django import forms
from .models import Folder

class FolderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {
                'class': 'form-control'
            }
    class Meta:
        model = Folder
        fields = ('title',)
        labels = {'title': 'フォルダー名'}