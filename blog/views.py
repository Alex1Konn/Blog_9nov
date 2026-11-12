from django.shortcuts import render, redirect

from blog.models import Post
from blog.models import UserProfile

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})

@login_required
def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Передаем instance=profile, чтобы обновлять существующую запись
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения успешно сохранены!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {'profile': profile, 'form': form})