from django.db.models import Q
from django.views.generic import ListView

from staff.models import StaffModel


class Staffview(ListViewfrom django.db.models import Q
from django.views.generic import ListView

from staff.models import StaffModel


class Staffview(ListView):
    template_name = 'staff.html'
    model = StaffModel

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return StaffModel.objects.filter(Q(name__icontains=q) |
                                         Q(position__icontains=q)
                                         )
