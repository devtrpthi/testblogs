from django.shortcuts import redirect, render
from.models import Category,Posts
from .forms import CommentForm

def frontpage(request):
    posts= Posts.objects.all()

    context = {
            'posts': posts
            }
    return render(request, 'blog/templates/frontpage.html', context)

def detail(request, slug):
    post= Posts.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            obj= form.save(commit= False)
            obj.post = post
            obj.save()

            return redirect('detail', slug = post.slug)
    else:
        form =  CommentForm()

    context = {
            'post': post,
            'form': form
            }

    return render(request, 'blog/templates/detail.html',context)

def category(request,slug):
    category= Category.objects.get(slug=slug) 

    context = {
           'category': category
           }
    return render(request,'blog/templates/category.html', context)



