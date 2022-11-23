from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from common.models import Location,BarrierFreeInfo

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ("name", "longitude","latitude","address")

class BarrierFreeInfoForm(forms.ModelForm):
    class Meta:
        model = BarrierFreeInfo
        fields = ("elevator_count","elevator_detail","elevator_detail",
                  "entrance_form","entrance_ramp","entrance_braille",
                  "entrance_detail","entrance_img", "restroom_floor",
                  "restroom_detail","restroom_img", "parking_count",
                  "parking_detail","parking_img"
                  )