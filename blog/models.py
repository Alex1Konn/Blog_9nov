from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Текст')
    image = models.ImageField('Картинка', upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title[:50]}"


def user_avatar_path(instance, filename):
    """
    Генерирует путь для аватара: user_{id}/avatars/{filename}
    """
    ext = filename.split('.')[-1]
    filename = f"avatar_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext}"
    return os.path.join('users', f'user_{instance.user.id}', 'avatars', filename)

def user_document_path(instance, filename):
    """
    Организует документы по датам: documents/2025/01/filename
    """
    today = datetime.now()
    return os.path.join(
        'documents',
        str(today.year),
        str(today.month).zfill(2),
        filename
    )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    resume = models.FileField(upload_to=user_document_path, blank=True, null=True)