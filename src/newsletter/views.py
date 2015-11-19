from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
		title = 'welcome'
		form = SignUpForm(request.POST or None)
		#if request.user.is_authenticated():
		#	title = "Current user is %s" %(request.user)
		# if request.method =="POST":
		# print request.POST
		context = {
			"template_title": title,
			 "form": form
		}

		if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				context = {
					"template_title":"Whoop there it is!"
				}


		return render(request, "home.html", context)