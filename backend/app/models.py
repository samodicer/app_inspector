from django.db import models


def upload_path(instance, filename):
    return '/'.join(['files', str(instance.title)])


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    file = models.FileField(blank=True, null=True, upload_to=upload_path)

    def __unicode__(self):
        return self.title

