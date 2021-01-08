from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    #forms.Form parametrede vardı yerine model formları kullanacağız artık!

    class Meta:
        model=Article
        # models.pydakilerle istediklerimizden input oluşturduk.
        fields=["title","content","article_image"]







