""" File: views.py:
     index view: button that calls function
     serveData view: reads someJSON.txt and serves it to incoming requests
"""
from django.http import HttpResponse
from django.views.decorators.http import require_GET
import pyBack.getSaveStuff as gst
# Index view:
def index(request):
    if(request.GET.get('mybtn')):
        gst.saveJSON()
        return HttpResponse("Requested")
    else:
        text = """
        <form action="#" method="get">
            <input type="submit" class="btn" value="Get Data" name="mybtn">
        </form>"""
        return HttpResponse(text)
# serveData view:

@require_GET
def serveData(request):
    f = open("pyBack/data/someJSON.txt", "r")
    response = HttpResponse(f.read(), content_type="text/plain")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
