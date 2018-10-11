from django.shortcuts import render


from .models import News
# Create your views here.

def test(request):
	widget = News.objects.get(user=request.user)
	return render(request, 'news.html', {'news' : widget.getNews()})