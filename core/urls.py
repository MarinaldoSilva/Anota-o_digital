from django.urls import path
from .views import AnotacaoDetailAPIView, AnotacaoListCreateAPIVIew

urlpatterns = [
    path("anotacao/", AnotacaoListCreateAPIVIew.as_view(), name="anotacao-list-create"),
    path("anotacao/<int:pk>/", AnotacaoDetailAPIView.as_view(), name="anotacao-detail")
]

