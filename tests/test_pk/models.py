from django.db import models

from localflavor.pk.models import (PKStateField,
                                   PKPostCodeField,
                                   PKPhoneNumberField)


class PakistaniPlace(models.Model):
    state = PKStateField(blank=True)
    state_required = PKStateField()
    state_default = PKStateField(default="PK-IS", blank=True)
    postcode = PKPostCodeField(blank=True)
    postcode_required = PKPostCodeField()
    postcode_default = PKPostCodeField(default="44000", blank=True)
    phone = PKPhoneNumberField(blank=True)
    name = models.CharField(max_length=20)
