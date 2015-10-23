from django.db import models
from django.forms import ModelForm


class fill(models.Model):
    Full_name = models.CharField(max_length=200)
    Add = models.CharField(max_length=200)
    ipadd = models.IntegerField(default=0)
    email = models.EmailField(default=0)
    phoneno = models.IntegerField(default=0)
    class Meta:
        db_table=u'fill'

    def __unicode__(self):
        return u"%s %s %d %s %d" % (self.full_name, self.Add, self.ipadd, self.email,self.phoneno)


