from django.db import models


class Blackbox(models.Model):
    aircraft = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=200, null=True)
    info_count  = models.PositiveIntegerField(default=0)
    errors_count  = models.PositiveIntegerField(default=0)
    pre_legend = models.PositiveIntegerField(default=0)
    warning = models.PositiveIntegerField(default=0)
    paired_b = models.PositiveIntegerField(default=0)
    legend = models.PositiveIntegerField(default=0)
    lower_b = models.PositiveIntegerField(default=0)
    repeat_legend = models.PositiveIntegerField(default=0)
    upper_a = models.PositiveIntegerField(default=0)
    lower_a = models.PositiveIntegerField(default=0)
    paired_a = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.aircraft)

    # class Meta:
    #     unique_together = ['product', 'value', 'name']