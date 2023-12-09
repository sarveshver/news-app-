# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Comment
from .forms import CommentForm
import requests

API_KEY = '5411a0bbaff14a469f846ec50121a4b0'

def get_article_url_for_index(articles, index):
    # Implement the logic to retrieve the article URL based on the index
    # This assumes that 'articles' is a list of dictionaries
    try:
        return articles[index].get('url', '')
    except IndexError:
        return ''

def home(request):
    language = request.GET.get('language', '')
    category = request.GET.get('category', '')

    if language:
        url = f'https://newsapi.org/v2/top-headlines?language={language}&apiKey={API_KEY}'
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    # Retrieve comments for each article
    article_comments = {}
    for i, article in enumerate(articles):
        article_url = article.get('url')
        comments = Comment.objects.filter(article_url=article_url)
        article_comments[i] = comments

    return render(request, 'home.html', {'articles': enumerate(articles), 'comment_form': CommentForm(), 'comments': article_comments})

def post_comment(request, article_index):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            # Set the article URL using the get_article_url_for_index function
            comment.article_url = get_article_url_for_index(articles, article_index)

            # Set other fields, if needed
            comment.save()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'user_name': comment.user_name,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'comment_text': comment.comment_text,
                })
            else:
                return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Invalid form submission.'}, status=400)
            else:
                return redirect('home')
    else:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Invalid request method.'}, status=405)
        else:
            return redirect('home')