from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Zone, New
from .forms import NewForm, ZoneForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from hitcount.views import HitCountMixin
from hitcount.utils import get_hitcount_model
from hitcount.models import Hit

from django.http import Http404
from django.utils.timezone import datetime

def basic_info(request):
    categoriest = Category.objects.all()
    zones = Zone.objects.all()
    news = New.objects.filter(is_active=True)[0:10]

    context = {
        "categoriest":categoriest,
        "zones":zones,
        "news":news
    }

    return context


# Create your views here.

def index(request):

    context = {}

    try:
        q = request.GET.get("q")

        news = New.objects.filter(title__icontains=q)

        context = {
            "news":news,
            "q":q,
        }
    except:
        pass
   
    return render(request, "index.html", context)


def new_detail(request, id):
    new = New.objects.get(id=id)

    hit_count = get_hitcount_model().objects.get_for_object(new)
    hits = hit_count.hits
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
       
    context = {
        "new":new,
        'hits':hits
    }

    return render(request, 'new_detail.html', context)


def zone_detail(request, slug):
    zone = Zone.objects.get(slug=slug)
    zone_news = New.objects.filter(zone=zone)

    context = {
        "zone":zone,
    }

    return render(request, "zone_detail.html", context)

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)

    category_news = New.objects.filter(category=category)

    context = {
        "category":category,
        "category_news":category_news
    }

    return render(request, "category_detail.html", context)


@login_required(login_url="index")
def create_new(request):
    form = NewForm()

    if request.POST:
        form = NewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.save()
            return redirect("index")
        else:
            return render(request, "create_new.html", {"form":form})
        
    return render(request, "create_new.html", {"form":form})

@login_required(login_url="index")
def new_update(request, id):


    new = New.objects.get(id=id)
    form = NewForm(instance=new)

    if request.user == new.author:

        if request.method == 'POST':
            form = NewForm(instance=new, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect("new-detail", new.id)


        return render(request, "new_update.html", {"form":form, "new":new})
    else:
        raise Http404("Kirish taqiqlanadi")
    
@login_required(login_url="index")
def zone_list(request):
    # zones = Zone.objects.all()

    return render(request, "zone_list.html")

@login_required(login_url="index")
def zone_create(request):
    form = ZoneForm()

    if request.method == 'POST':
        form = ZoneForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("zone-list")
        




    return render(request, 'zone_create.html', {"form":form})

@login_required(login_url="index")
def category_list(request):
    category = Category.objects.all()

    return render(request, "category_list.html", {"category":category})


@login_required(login_url="index")
def zone_update(request, id):
    zone = get_object_or_404(Zone, id=id)
    form = ZoneForm(instance=zone)

    if request.method == 'POST':
        form = ZoneForm(instance=zone ,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('zone-list')


    return render(request, "zone_update.html", {"form":form, "zone":zone})

@require_POST
@login_required(login_url="index")
def zone_delete(request, id):
    zone = get_object_or_404(Zone, id=id)
    zone.delete()
    return redirect('zone-list')


@login_required(login_url="index")
def category_create(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("category-list")



    return render(request, 'category_create.html', {"form":form})

@login_required(login_url="index")
def category_update(request, id):
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(instance=category ,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')


    return render(request, "category_update.html", {"form":form, "category":category})


@require_POST
@login_required(login_url="index")
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category-list')


@login_required(login_url="index")
def dashboard(request):
    number_news = New.objects.all().count()
    number_todays_news = New.objects.filter(created__date=datetime.now().date()).count()
    all_views = Hit.objects.all().count()
    todays_views = Hit.objects.filter(created__date=datetime.now().date()).count()

    context = {
        "number_news":number_news,
        "number_todays_news":number_todays_news,
        "all_views":all_views,
        "todays_views":todays_views,

    }

    return render(request, "dashboard.html", context)