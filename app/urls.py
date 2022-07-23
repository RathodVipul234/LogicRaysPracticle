"""
    - App url routing
"""
from django.urls import path
from graphene_django.views import GraphQLView

from app.views import (
    SignInView, EmailVerificationView, HomePageView, LogoutView
)

app_name = "app"

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('login/', SignInView.as_view(), name="sign_in"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('email-varify/', EmailVerificationView.as_view(), name="varification"),

    path("graphql/", GraphQLView.as_view(graphiql=True), name="graphql"),
]
