from django.db.models import Q
from django.views.generic import TemplateView, ListView
from .models import Searchdb


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Searchdb
    template_name = 'search_results.html'
    def get_queryset(self):
        # return Searchdb.objects.filter(
        #     Q(timedata__icontains="April"))
    # def get_quearyset(self):
    #     query = self.request.GET.get('q')
    #     object_list = Searchdb.objects.filter(
    #         Q(timedata__icontains=query)
    #     )
    #     return object_list
        query = self.request.GET.get('q')
        object_list =Searchdb.objects.filter(
            Q(timedata__icontains=query)
        )
        return object_list