from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def home(request):
    return render(request, "Home.html")

def signUp(request):
    if request.method == "GET":
        return render(request, "signUp.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("reservation")
            except IntegrityError:
                return render(
                    request,
                    "SignUp.html",
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )
        else:
            return render(
                request,
                "SignUp.html",
                {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
            )

def reservation(request):
    return render(request, "Reservation.html")