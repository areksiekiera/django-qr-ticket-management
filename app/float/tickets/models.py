from django.db import models
import random, string

from django.utils import timezone
from datetime import datetime, timedelta

import qrcode
from io import StringIO

from django.conf import settings


class Ticket(models.Model):
    TYPE_CHOICES = (
        ('T', 'Tank'),
        ('R', 'Room'),
    )

    room_type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        null=False)
    duration = models.IntegerField(default=0)
    redeemed = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True)
    code_path = models.CharField(max_length=150, blank=True)

    validto = models.DateField(blank=True, null=True)
    created = models.DateTimeField(blank=True)

    comment = models.CharField(max_length=5000, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.localtime(timezone.now())

        if not self.code:
            self.code, self.code_path = self.generate_code()
        
        super(Ticket, self).save(*args, **kwargs)


    def generate_code(self):
        # generate code from random
        chars = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(chars) for _ in range(16))

        # generate qr image 
        qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )

        qr.add_data("{}#{}#{}".format(code, self.room_type, self.duration))
        qr.make(fit=True)
        img = qr.make_image()

        # save locally 
        filename = "{}/codes/{}.png".format(settings.MEDIA_ROOT, code)
        url = "{}/codes/{}.png".format(settings.MEDIA_URL, code)
        img.save(filename)

        return code, url

    def __str__(self):
        return "{}min, {}".format(self.duration, self.code)

    def get_room_type(self):
        if self.room_type == 'T':
            return 'Tank'
        return 'Room'


        


