from django.shortcuts import render

def test(request):
	return render(request, '../templates/teacher/test.html', {})