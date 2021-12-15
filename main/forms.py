from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.models import User

from main.models import Seller, Ad, AdPicture, SMSLog


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class SellerForm(ModelForm):

    class Meta:
        model = Seller
        fields = ["itn", "phone"]


class SMSLogForm(ModelForm):

    class Meta:
        model = SMSLog
        fields = ["code"]


ImageFormset = inlineformset_factory(
    Ad,
    AdPicture,
    fields=("image",),
    extra=1,
)
