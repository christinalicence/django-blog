from django.shortcuts import render
from .models import About

# Create your views here.
def about_me(request):
    """
    Display the About Me page.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about_me.html`
    """

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )