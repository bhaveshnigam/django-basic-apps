from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models import permalink

import datetime
import dateutil


class PersonType(models.Model):
  """ Person Type model """
  title = models.CharField(_('title'), max_length=100)
  slug = models.SlugField(_('slug'), prepopulate_from=('title',), unique=True)
  
  class Meta:
    verbose_name = _('person type')
    verbose_name_plural = _('person types')
    db_table = 'people_types'
    ordering = ('title',)

  class Admin:
    pass

  def __unicode__(self):
    return '%s' % self.title

  @permalink
  def get_absolute_url(self):
    return ('person_type_detail', None, { 'slug': self.slug })


class Person(models.Model):
  """ Person model """
  GENDER_CHOICES = (
    (1, 'Male'),
    (2, 'Female'),
  )
  first_name        = models.CharField(_('first name'), blank=True, max_length=100)
  middle_name       = models.CharField(_('middle name'), blank=True, max_length=100)
  last_name         = models.CharField(_('last name'), blank=True, max_length=100)
  slug              = models.SlugField(_('slug'), prepopulate_from=('first_name','last_name',), unique=True)
  gender            = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
  mugshot           = models.FileField(_('mugshot'), upload_to='mugshots', blank=True)
  mugshot_credit    = models.CharField(_('mugshot credit'), blank=True, max_length=200)
  birth_date        = models.DateField(_('birth date'), blank=True, null=True)
  person_types      = models.ManyToManyField(PersonType, blank=True)
  website           = models.URLField(_('website'), blank=True, verify_exists=True)
  
  class Meta:
    verbose_name = _('person')
    verbose_name_plural = _('people')
    db_table = 'people'
    ordering = ('last_name', 'first_name',)

  class Admin:
    list_filter   = ('person_types',)
    search_fields = ('first_name', 'last_name')

  def __unicode__(self):
    return u"%s" % self.full_name
  
  @property
  def full_name(self):
    return u"%s %s" % (self.first_name, self.last_name)
  
  @property
  def age(self):
    TODAY = datetime.date.today()
    return u"%s" % dateutil.relativedelta(TODAY, self.birth_date).years
  
  @permalink
  def get_absolute_url(self):
    return ('person_detail', None, { 'slug': self.slug })
  
  @property
  def get_mugshot_url(self):
    return u"%s%s" % (settings.MEDIA_URL, self.mugshot)


class Quote(models.Model):
  """ Quote model """
  person            = models.ForeignKey(Person)
  quote             = models.TextField(_('quote'))
  source            = models.CharField(_('source'), blank=True, max_length=255)
  
  class Meta:
    verbose_name = 'quote'
    verbose_name_plural = 'quotes'
    db_table = 'people_quotes'
  
  class Admin:
    list_display = ('person','quote')
    list_filter   = ('person',)
    search_fields = ('quote',)
  
  def __unicode__(self):
    return u"%s" % self.quote