from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author =models.ForeignKey("auth.User",on_delete=models.Case, verbose_name="Yazar")
    title= models.CharField(max_length=50,verbose_name="Başlık")
    #content=models.TextField(verbose_name="İçerik")
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image=models.FileField(blank= True, null=True, verbose_name="Makaleye Ffotoğraf ekleyin")
    def __str__(self):
        return self.title

#yorum yapılma tarihine göre en son yapılan en başta olmak üzere sıralamak için meta yaptık
#Meta sitesinde bir sürü meta seçeneğinden orderingi seçtik.
#Bu sayede en son eklenen ilk gösterilecek
class Meta:
    ordering=['-order_date']
class Comment(models.Model):
    #Artickle silindiğinde yorumları da silinmesi lazım.
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="İsim")
    comment_content=models.CharField(max_length= 200,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
    #özelleştirmek için,... yorum görünsün diye

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering=['-comment_date']
