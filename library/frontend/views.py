from django.views import generic

from .models import Book

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_book_list'

    def get_queryset(self):
        return Book.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Book
    template_name = 'detail.html'
