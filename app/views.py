"""
    buisness logic for Task
"""
import base64
from datetime import datetime
import pyotp
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

from app.models import UserOTP

# Create your views here.


class SignInView(View):
    """
    ::get
    - this method will show you template with Email field
    once you add email then post method will be called
    ::post
    - this method will genrate otp with email + current date time object
    - otp will be send to respective email and user will get otp input

    :: User Createtion Logic
    - if user is not exist with perticuler enter email then first will be cerateed user
    and then stored enrated otp to UserItp model

    """

    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        """
            - get method
        """
        context = {}
        if request.session.get("email"):
            context["email"] = request.session["email"]
            context["is_otp_send"] = True
            del request.session["email"]
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
            post method
        """
        context = {}
        email = self.request.POST.get("email")
        if not email:
            messages.error(request, "please enter email Id")
            return redirect("app:sign_in")
        key1 = str(email) + str(datetime.now())
        key = base64.b32encode(key1.encode())  # Key is generated
        generated_otp = pyotp.HOTP(key).at(1)
        try:
            print("sending mail .....")
            send_mail(
                "OTP",
                f"Your OTP -{generated_otp}",
                "my422kingheart.2728@gmail.com",
                [
                    email,
                ],
                fail_silently=False,
            )
            print("mail sent.....")
            user, created = User.objects.get_or_create(
                email=email, defaults={"username": email.split("@")[0]}
            )
            otp_object, created = UserOTP.objects.get_or_create(
                user=user, defaults={"otp": generated_otp}
            )
            if not created:
                otp_object.otp = generated_otp
                otp_object.invalid_attempt = 0
                otp_object.is_expired = False
                otp_object.save()

        except:
            messages.error(request, "please enter valid email Id")
            return redirect("app:sign_in")

        print("=======================================================")
        print(generated_otp)
        print("=======================================================")
        context["email"] = email
        context["is_otp_send"] = True
        return render(request, self.template_name, context)


class EmailVerificationView(View):
    """
    ::post
    - when user enter otp in otp field and submit that otp this fucntion will be called
    and if we get object with that email and enterd otp then we procced their
    login fucntionlity and redirect to homepage
    """

    def post(self, request, *args, **kwargs):
        """
            post method
        """
        email = request.POST.get("email")
        otp = request.POST.get("otp")
        if not otp or not email:
            try:
                del request.session["email"]
            except:
                pass
            messages.error(request, "Please enter valid input data.")
            return redirect("app:sign_in")
        valid_user = UserOTP.objects.filter(user__email=email, otp=otp).first()
        if not valid_user:
            request.session["email"] = email
            user = UserOTP.objects.filter(user__email=email).first()
            if user:
                user.invalid_attempt += 1
                if user.invalid_attempt >= 3:
                    user.is_expired = True
                    del request.session["email"]
                    messages.error(
                        request,
                        "Your otp is expired please Try again by generating new otp.!!",
                    )
                else:
                    messages.error(request, "Please enter valid otp.")
            else:
                messages.error(request, "Please enter valid otp.")
            user.save()
            return redirect("app:sign_in")
        login(request, valid_user.user)
        valid_user.delete()
        messages.success(request, "You have successfully logged in.")
        return redirect("app:home")


class HomePageView(LoginRequiredMixin, TemplateView):
    """
    - there is no meaning of this class
    i just create home page for after login redirect
    """

    template_name = "home.html"


class LogoutView(View):
    """
    - logout view
    """

    def get(self, request, *args, **kwargs):
        """
            get method
        """
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect("app:sign_in")
