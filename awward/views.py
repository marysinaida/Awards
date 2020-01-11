from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Project
from .forms import ProjectsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm, ProjectsLetterForm
from django.http import JsonResponse
import datetime as dt

# Create your views here.


def index(request):
    return render(request, 'index.html')


def projects_today(request):
    date = dt.date.today()
    projects = Project.todays_projects()
    form = ProjectsLetterForm()
    return render(request, 'today-projects.html', {"date": date, "projects": projects, "letterForm": form})

    if request.method == 'POST':
        form = ProjectsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            
            recipient = ProjectsLetterRecipients(name =name , email = email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('projects_today')

    else:
        form = ProjectsLetterForm()
    return render(request, 'today-projects.html', {"date": date, "project": project, "letterForm": form})


def projectsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = ProjectsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)


def past_days_projects(request, past_date):

    try:
        # convert data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(projects_of_day)

    projects = Project.days_projects(date)

    return render(request, 'past-projects.html', {"date": date, "projects": projects})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("projects")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "project.html", {"project": project})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method =='POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('projectToday')

    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{"form":form})
