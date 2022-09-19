from datetime import datetime
from django.shortcuts import render

# from django.http import HttpResponse


# Create your views here.
def all_rooms(request):
    now = datetime.now()
    hungry = True
    # return HttpResponse(content="hello")
    context = {
        "now": now,
        "hungry": hungry,
    }
    return render(request, "all_rooms.html", context=context)


1
