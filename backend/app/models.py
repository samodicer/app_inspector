from django.db import models


def upload_path(instance, filename):
    return '/'.join(['files', str(instance.title)])


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    file = models.FileField(blank=True, null=True, upload_to=upload_path)
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(null=True)

    def __unicode__(self):
        return self.title

class Analyse(models.Model):
    id = models.AutoField(primary_key=True)
    files_id = models.CharField(max_length=250)
    user_id = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)


