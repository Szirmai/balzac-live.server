from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

handler404 = 'dashboard.views.handler404'
handler500 = 'dashboard.views.handler500'


urlpatterns = [  
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/<str:pk>/', views.taskPage, name='task-page'),
    path('all-users/', views.allUsers, name='all-users'),
    path('update/', views.upload, name='update'),
    path('update-article/<str:pk>', views.updateArticleForm, name='update-article'),
    path('update-video/<str:pk>', views.updateVideoForm, name='update-video'),
    path('update-team/<str:pk>', views.updateTeamForm, name='update-team'),
    path('update-about/<str:pk>', views.updateAboutForm, name='update-about'),
    path('update-whaa/<str:pk>', views.updateWhaaForm, name='update-whaa'),
    path('update-task/<str:pk>', views.updateTaskForm, name='update-task'),
    path('task/<str:pk>', views.task, name='task'),
    path('delete/article/<str:pk>', views.deleteArticle, name='delete-article'),
    path('delete/video/<str:pk>', views.deleteVideo, name='delete-video'),
    path('delete/team/<str:pk>', views.deleteTeam, name='delete-team'),
    path('delete/task/<str:pk>', views.deleteTask, name='delete-task'),
    path('contact-us/', views.notYet, name="not-yet"),
    path('message/<str:pk>', views.contact, name='contact'),
    path('delete-message/<str:pk>', views.DeleteContact, name='delete-contact'),
    path('groups/', views.manage_groups, name='groups'),
    path('manage-user-article/', views.manageArticle, name='manage-article'),
    path('approved/', views.Approved, name="approved"),
    path('rejected/', views.Rejected, name='rejected'),
    path('pending/', views.Pending, name='pending'),
    path('user-article-status-edit/<str:pk>', views.editUserArticleStatus, name='user-status'),
    path('manage/', views.Vau, name='manage-vau-pending'),
    path('choose-pending/', views.ChoosePending, name="choose-pending"),
    path('pending-video/', views.LocalVideo, name='local-video'),
    path('pending-article/', views.LocalArticle, name='local-article'),
    path('article/pending/', views.ArticlePending, name="pending-article"),
    path('article/approved/', views.ArticleApproved, name="approved-article"),
    path('article/rejected/', views.ArticleRejected, name="rejected-article"),
    path('video/rejected/', views.VideoRejected, name='rejected-video'),
    path('video/approved/', views.VideoApproved, name='approved-video'),
    path('video/pending/', views.VideoPending, name='pending-video'),
    path('change-article/<str:pk>/', views.ChangeArticleStatus, name="cas"),
    path('change-video/<str:pk>/', views.ChangeVideoStatus, name="cvs"),
]