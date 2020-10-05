from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.models import User


class Tag(models.Model):
    title = models.CharField(_('Tag title'), max_length=25, unique=True)

    class Meta:
        db_table = 'TAG'
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.title


class TextSnippet(models.Model):
    title = models.CharField(_('Title'), max_length=100, unique=True)
    content = models.TextField(_('Content'), blank=False)
    timestamp = models.DateTimeField(_('Timestamp'), auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='texts')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='texts')
    is_deleted = models.BooleanField(
        _('Is deleted'),
        default=False,
        help_text=_(
            'Designates whether this should be treated as deleted or not. '))

    class Meta:
        db_table = 'TEXT'
        verbose_name = _('text_snippet')
        verbose_name_plural = _('texts')

    def __str__(self):
        return self.title
