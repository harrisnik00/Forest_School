from django.http import HttpResponse
import traceback

def index(request):
    return HttpResponse("<h2>Hello Django this is the home page of the first app</h2>")

def about(request):
    return HttpResponse("<h2>Know more about first app</h2>")

def debug_view(request):
    try:
        return HttpResponse("Debug test - this should work")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}<br><pre>{traceback.format_exc()}</pre>")