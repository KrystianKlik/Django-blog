from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Krystian',
		'title': 'Blog Post 1',
		'content': 'Firts post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'Adam',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'August 29, 2018'
	}
]


def home(request):
	context = {	'posts': posts	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

