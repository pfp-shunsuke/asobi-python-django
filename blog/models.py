from django.db import models


class Blog(models.Model):

    # id=1,2,3,..... 明記していないがidが自動的に定義される（プライマリーキー、インクリメントされる）
    content = models.CharField(max_length=140)
    posted_date = models.DateTimeField(auto_now_add=True)
