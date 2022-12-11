from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from common.models import Location,BarrierFreeInfo,Reply

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ["name", "longitude","latitude","address"]
        widgets = {'longitude':forms.HiddenInput,
                   'latitude':forms.HiddenInput,
                   'address':forms.HiddenInput,}

class BarrierFreeInfoForm(forms.ModelForm):
    is_elevator = forms.BooleanField()
    elevator_img = forms.ImageField(required=False)
    entrance_img = forms.ImageField(required=False)
    parking_img = forms.ImageField(required=False)
    toilet_img = forms.ImageField(required=False)
    is_braille = forms.BooleanField()
    is_ramp = forms.BooleanField()
    is_accessible_toilet = forms.BooleanField()
    class Meta:
        model = BarrierFreeInfo
        fields = ["is_elevator","elevator_img",
                  "is_ramp","is_braille",
                  "entrance_img", "is_accessible_toilet",
                  "toilet_img", "parking_count",
                  "parking_img","detail"
                  ]
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text', 'writer']