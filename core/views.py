from django.shortcuts import render
import os
 
def index(request):
	s = str(os.popen('ifconfig').read())
	s =s.replace('\n', '<br>')
	return render(request, "index.html", {"interface":s})
