from django.forms import ModelForm
from django.contrib.auth.models import User

from main.models import Seller


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class SellerForm(ModelForm):

    class Meta:
        model = Seller
        fields = ["itn"]
        