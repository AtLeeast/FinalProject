import time
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import AccountModel
from loguru import logger
from .forms import BottlesFoundForm

from .utils.get_user_data import get_user_data


def index(request):
    return render(request, 'ecosite/index.html', get_user_data(request))


def about(request):
    return render(request, 'ecosite/about.html', get_user_data(request))


def registration(request):
    return render(request, 'ecosite/registration.html')


def login(request):
    return render(request, 'ecosite/login.html')


def statistics(request):
    return render(request, 'ecosite/statistics.html', get_user_data(request))


def profile(request):
    if "account_id" not in request.session:
        return index(request)
    return render(request, 'ecosite/profile.html', get_user_data(request))


def quit(request):
    if "account_id" in request.session:
        email = AccountModel.objects.filter(id=request.session["account_id"])[0].email
        logger.info(f"User {email} terminated session on their account")

        del request.session["account_id"]

    return render(request, 'ecosite/login.html')


@csrf_exempt
def bottles_found(request):
    if request.method == "POST":
        form = BottlesFoundForm(request.POST, request.FILES)
        if form.is_valid():
            with open(f"submissions/{request.session['account_id']}.{time.time()}.png", "wb+") as destination:
                for chunk in request.FILES["image"]:
                    destination.write(chunk)
        else:
            logger.info("Form is not valid")
    return HttpResponse("error")
