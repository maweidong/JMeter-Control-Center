import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def index(request):
    context = {}
    return render(request, 'jltc/index.html', context)

