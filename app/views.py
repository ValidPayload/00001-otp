from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import datetime
import random

from .models import PIN
from .forms import PhoneNumberForm, VerifyPINForm
from .utils import (
    gen_pin,
    gen_pin_v2,
)


@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        form.is_valid()  # I don't care about invalid. It's just for a video

        # Generate PIN
        pin_len = settings.PIN_LENGTH
        if settings.PIN_GEN_V2:
            pin = gen_pin_v2(pin_len)
        else:
            pin = gen_pin()

        # Create a PIN
        PIN.objects.create(
            phone_number=form.cleaned_data["phone_number"],
            pin=pin,
            valid_until=datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        )

        # Render verification form
        return render(
            request,
            "verify_pin.html",
            {
                "form": VerifyPINForm(),
                "phone_number": form.cleaned_data["phone_number"]
            }
        )

    return render(
        request,
        "index.html",
        {"form": PhoneNumberForm()}
    )


@csrf_exempt
@require_http_methods(["POST"])
def verify_pin(request):
    form = VerifyPINForm(request.POST)
    form.is_valid()  # I don't care about invalid. It's just for a video

    try:
        obj = PIN.objects.get(
            phone_number=form.cleaned_data["phone_number"],
            pin=form.cleaned_data["pin"],
            valid_until__gt=datetime.datetime.utcnow(),
        )
        obj.delete()
        success = True
    except PIN.DoesNotExist:
        success = False

    return render(
        request,
        "verify_pin_result.html",
        {"success": success}
    )
