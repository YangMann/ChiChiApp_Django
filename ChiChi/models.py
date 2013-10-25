from django.db import models

#from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(models.Model):
    #jaccount
    userId = models.CharField(max_length=64, primary_key=True)

    def __unicode__(self):
        return self.userId


class Comment(models.Model):
    content = models.CharField(max_length=4096)
    time = models.DateTimeField()
    response = models.CharField(max_length=1024, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s %s' % (self.user, self.content)
