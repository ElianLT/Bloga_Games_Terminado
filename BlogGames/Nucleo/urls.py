from django.urls import path
from .views import dates, HomeListView, PostDetailView, CategoryListView, AuthorListView, PostCreateView, PostUpdateView, PostDeleteView, AboutPageView

urlpatterns = [
    # Pagina inicio
    path('', HomeListView.as_view(), name='home'),

    # Detalle del post
    path('post/<pk>', PostDetailView.as_view(), name='post'),

    # Filtrado por categoria
    path('category/', CategoryListView.as_view(), name='category'),

    # Filtrado por author
    path('author/', AuthorListView.as_view(), name='author'),

    # Pagina filtrado por fecha
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),

    # Crear Post
    path('create/', PostCreateView.as_view(), name='create'),

    # Editar Post
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),

    # Eliminar Post
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),

    # About - Acerca de nosotros
    path('about/', AboutPageView.as_view(), name='about'),
]