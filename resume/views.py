from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")


def projects (request):
    projects_show=[
        {
            'title': 'Devara',
            'path': 'images\Devara.png',
        },
        {
            'title': 'Lift',
            'path': 'images\Lift.jpeg',
        },

        {
            'title': 'Fighter',
            'path': 'images\Fighter.png',
        },
        {
            'title': 'Munjya',
            'path': 'images\Munjya.png',
        },

         {
            'title': 'Kalki',
            'path': 'images\Kalki.jpg',
        },
          {
            'title': 'Borderland',
            'path': 'images\Borderland.png',
        },
         {
            'title': 'Portfolio',
            'path': 'images/portfolio.PNG',
        },
                  {
            'title': 'Bade Miyan Chote Miyan',
            'path': 'images\Bade Miyan Chote Miyan.jpg',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})


def experience(request):
    experience=[
        {"company":"Double Negative (DNEG)",
         "position":"Pipeline TD (July 2022 to Present - Chennai)"},
        {"company":"Future Works Media Limited",
         "position":"Pipeline Developer (Jan 2022 to June 2022 - Chennai)"},
        {"company":"Silvercloud Studio ( After Studio)",
         "position":"Pipeline Developer (Sept 2021 to Nov 2021 - Mumbai)"},
        {"company":"Assemblage Entertainment",
         "position":"JR.Pipeline Developer (Jan 2021 to July 2021 - Mumbai)"},
        {"company":"Atomic Arts VFx",
         "position":"JR.Pipeline Developer (Sept 2019 to Oct 2020 - Mumbai)"},
        {"company":"Team247 Informatics",
         "position":"Python Developer (Aug 2018 to July 2019 - Hyderabad)"},
        {"company":"Next Education India Pvt Ltd",
         "position":"E-learning Support Engineer (July 2015 to Sept 2017 - Hyderabad)"}
    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
