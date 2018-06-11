from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):

    STATUS_CHOICES = (
        ("ON", "on"),
        ("OFF", "off"),
        ("STANDBY", "standby")
    )

    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="off")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=40, null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    alt = models.FloatField()
    time = models.DateTimeField()

    def __unicode__(self):
        return "%s at %f,%f" % (self.user, self.lat, self.lng)

    class Meta:
        ordering = ('pk', 'user')
       # get_latest_by = ('pk')
