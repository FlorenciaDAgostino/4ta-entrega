from django.urls import path

from .views import (saludo, saludo_con_template, crear_familiar,
                    inicio, crear_curso, crear_estudiante, buscar_cursos, cursos, crear_profesores,
                    CelularesCreateView, CelularesListView, HeladerasCreateView, HeladerasListView, LavarropasCreateViews,LavarropasListView)

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
    path('crear-curso/', crear_curso, name= 'crear-curso'),
    path('crear-estudiante/', crear_estudiante, name= 'crear-estudiante'),
    path('crear-profesores/', crear_profesores, name= 'crear-profesores'),
    path('cursos/', cursos, name='cursos'),
    path('cursos/buscar', buscar_cursos, name='buscar-cursos'),

    # urls con vistas basadas en clase
    path('listar-celulares/', CelularesListView.as_view(), name= 'listar-celulares'),
    path('crear-celulares/', CelularesCreateView.as_view(), name= 'crear-celulares'),
    path('listar-heladeras/', HeladerasListView.as_view(), name= 'listar-heladeras'),
    path('crear-heladeras/', HeladerasCreateView.as_view(), name= 'crear-heladeras'),
    path('listar-lavarropas/', LavarropasListView.as_view(), name= 'listar-lavarropas'),
    path('crear-lavarropas/', LavarropasCreateViews.as_view(), name= 'crear-lavarropas'),

]
    
    

 