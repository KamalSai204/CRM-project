from django.shortcuts import render, redirect
from .models import Teachers


def lan(request):
    teachers = Teachers.objects.all()
    return render(request, "index.html", {"teacher": teachers})


def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get("image")

        teacher = Teachers(
        name=name,
        subject=subject,
        contact=contact,
        email=email,
        image=image if image else None,
        )
        teacher.save()
        return redirect("hello")
    return render(request, "index.html")
def update(request,id):
    if request.method=="POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        teachr=Teachers(
            id=id,
            name=name,
            subject=subject,
            contact=contact,
            email=email,
            image=image if image else None,
        )
        teachr.save()
        return redirect("hello")
    return render(request,"index.html",{"teachr":teachr})
def dle(request,id):
    teacher=Teachers.objects.filter(id=id)
    teacher.delete()
    return redirect("hello")

    