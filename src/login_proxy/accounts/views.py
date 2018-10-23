from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse


@login_required(login_url="accounts:login")
def profile(request):
    return TemplateResponse(template="profile.html", request=request)
