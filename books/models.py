from django.db import models

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Node(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name='Parent',
        related_name='children',
        db_index=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Page(models.Model):
    page_number = models.PositiveIntegerField('Page number')
    body = models.TextField('Text on the page')
    node = models.ForeignKey(
        Node,
        related_name='pages',
        verbose_name='Book Name/Part/Section/Chapter',
    )

    def __str__(self):
        return '%s - %s' % (self.page_number, self.node.get_family())
