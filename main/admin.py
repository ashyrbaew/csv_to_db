from django.contrib import admin
from .models import Blackbox

@admin.register(Blackbox)
class BlackboxAdmin(admin.ModelAdmin):
    list_display = [
        'aircraft', 'status', 'type', 'info_count', 'errors_count',
        'pre_legend', 'warning', 'paired_b', 'legend', 'lower_b',
        'repeat_legend', 'upper_a', 'lower_a', 'paired_a'
    ]



# aircraft
# status
# type
# info_count
# errors_count
# pre_legend
# warning
# paired_b
# legend
# lower_b
# repeat_legend
# upper_a
# lower_a
# paired_a
