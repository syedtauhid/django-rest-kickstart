import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Certificate(models.Model):

    uuid = models.UUIDField(
        verbose_name=_('Unique Identifier'),
        help_text=_('Must be unique.'),
        editable=False,
        unique=True,
        default=uuid.uuid4
    )
    name = models.CharField(
        max_length=64,
        verbose_name=_('Name'),
        help_text=_('Certificate name.')
    )
    description = models.CharField(
        max_length=256,
        verbose_name=_('Description'),
        help_text=_('Certificate description.'),
        default='',
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=True,
        help_text=_('Keep this certificate active or not.')
    )
    date_created = models.DateTimeField(
        verbose_name=_('Date Created'),
        help_text=_('Created date of the certificate.'),
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name=_('Date Updated'),
        help_text=_('Last updated date of the certificate.'),
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'common'
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')
        db_table = 'common_certificates'
