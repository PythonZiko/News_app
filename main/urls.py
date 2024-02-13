from django.urls import path
from . import views


urlpatterns = [
    # Yangiliklar
    path("", views.index, name="index"),
    path("new/<int:id>/", views.new_detail, name="new-detail"),
    path("new/create/", views.create_new, name="create-new"),
    path("new/<int:id>/detail/", views.new_update, name="new-update"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # Zonalar
    path("zone/list/", views.zone_list, name="zone-list"),
    path("zone/create/", views.zone_create, name="zone-create"),
    path("zone/<int:id>/update/", views.zone_update, name="zone-update"),
    path("zone/<int:id>/delete/", views.zone_delete, name="zone-delete"),
    path("zone/<slug:slug>/", views.zone_detail, name="zone-detail"),
    # Categoryalar
    path("category/list/", views.category_list, name="category-list"),
    path("category/create/", views.category_create, name="category-create"),
    path("category/<int:id>/update/", views.category_update, name="category-update"),
    path("category/<int:id>/delete/", views.category_delete, name="category-delete"),
    path("category/<slug:slug>/", views.category_detail, name="category-detail"),
]