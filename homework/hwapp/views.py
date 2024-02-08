from django.shortcuts import render
from django.http import HttpResponse
import logging

LOGGER = logging.getLogger(__name__)

# Create your views here.

def main(request):
    LOGGER.info("main page visited")
    return HttpResponse("""<h1>header<h/h1>
    <p>this is main page</p>""")

def about(request):
    LOGGER.info("visited page about me")
    return  HttpResponse("""<h1>header 2</h1>
    <p>this page about me<p>""")

