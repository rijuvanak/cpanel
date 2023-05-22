from django.urls import path
from .import views

urlpatterns = [
    path('todo/', views.home, name='todo'),

    path('image_request', views.image_request, name='image_request'),
    path('login_index1/', views.login_index1, name='login_index1'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('gallery/', views.gallery),
    path('carmodel/', views.carmodel, name='carmodel'),
    path('registration/', views.registration),
    path('users/', views.users, name="users"),
    path('var_req/', views.var_req, name='var_req'),
    path('delete/<int:id>', views.todo_delete, name='delete'),
    # path('edit/<int:id>', views.todo_edit, name='edit'),
    path('dashboardmain/', views.dashboardmain, name="dashboardmain"),
    path('photos/', views.photos, name="photos"),
    # path('index',views.IndexFunc,name='index'),
    # path('inspection',views.Inspectionfunc,name='inspection'),
    path('logout/', views.logout,name='logout'),
    # path('adminhome',views.AdminHomeFunc,name='adminhome'),
    # path('update/', views.update_data, name='update_data'),
    #path('todo-edit/', views.todo_edit, name='todo-edit'),
    # path('update-table/', views.update_table, name='update-table'),
    path("", views.index1, name="index1"),
    path("save-file1", views.save_file1, name="save-file1"),
    path("delete-file1", views.delete_file1, name="delete-file1"),
    path("edit-file1", views.edit_file1, name="edit-file1"),
    path("todo1", views.todo1, name="todo1"),
    path("todo2", views.todo2, name="todo2"),
    path("save-body", views.save_body, name="save-body"),
    path("edit-body", views.edit_body, name="edit-body"),
    path("delete-body", views.delete_body, name="delete-body"),
    # path('my_view', views.my_view, name='my_view'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    # path("update-body", views.update_body, name="update-body"),
]