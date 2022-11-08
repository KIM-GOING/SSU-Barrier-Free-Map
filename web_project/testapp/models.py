from django.db import models
from config import settings
from datetime import datetime
from common.models import Location
import os
from uuid import uuid4

# Create your models here.
def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    ext = os.path.splitext(filename)[-1].lower()
    uuid_name = uuid4().hex
    return '/'.join(['test/', ymd_path, uuid_name + ext])


class TestImage(models.Model):
    fk = models.ForeignKey(Location, null=True , on_delete=models.CASCADE)
    img = models.ImageField(null=True, upload_to=get_file_path)

    def delete(self, *args, **kwargs):
        super(TestImage, self).delete(*args, **kwargs)
        os.remove(os.path.join(settings.MEDIA_ROOT, self.img.path))