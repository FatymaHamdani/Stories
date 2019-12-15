from django.urls import include, path
from .views import classroom, students, teachers



urlpatterns = [
    path('', classroom.home, name='home'),

    path('teachers/', include(([
        path('', teachers.TeachersListView.as_view(), name='stories_list'),
        path('studies/tables/', teachers.TableListView.as_view(), name='table_list'),
        path('comments/<int:pk>/', teachers.EvaluerlistView, name='comment_list'),
        path('case/<int:pk>/', teachers.take_quiz, name='take_quiz'),
        

        
#<int:pk>/

    ], 'stories'), namespace='teachers')),

   path('students/', include(([    
        path('', students.HomeListView.as_view(), name='students_home'),
        path('board/', students.StudiesListView.as_view(), name='students_borad'),
        path('board/tables/', students.TableListView.as_view(), name='table_list'),
        path('board/dates/', students.DatesListView.as_view(), name='dates_list'),
        path('studies/', students.StudiesView.as_view(), name='studies_change_list'),
        path('case/add/', students.CaseCreateView.as_view(), name='case_add'),
        path('case/<int:pk>/change', students.CaseUpdateView.as_view(), name='case_change'),
        path('case/<int:pk>/delete/', students.QuizDeleteView.as_view(), name='case_delete'),
        path('case/<int:pk>/display', students.post_detail, name='post_detail'),
        ], 'stories'), namespace='students')),

]

