from django.db import models
from django.contrib.auth.models import User

def upload_path(instance, filename):
    return '/'.join(['files', str(instance.title)])


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    file = models.FileField(blank=True, null=True, upload_to=upload_path)
    user_id = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    analyse_id = models.ForeignKey('Analyse',null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

class Analyse(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id


