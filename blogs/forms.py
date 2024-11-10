from django import forms 
from blogs.models import Comment

class PostCommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',  # Deja la etiqueta vacía
        widget=forms.Textarea(attrs={
            'placeholder': 'Ingrese su comentario',
            'class': 'form-control mb-3',
            'rows': 3,
        })
    )

    class Meta:
        model = Comment
        fields = ['content']
