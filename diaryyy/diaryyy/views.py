from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect


class IndexView(TemplateView):
	template_name = 'index.html'

@login_required
def Home(request):
    return redirect(reverse('blogs:random_blog_list',
					kwargs={'username' :request.user.username }))
