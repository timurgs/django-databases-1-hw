from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)


def dict_filling(result_dict):
    objects = Book.objects.values_list()
    a = 0
    for i in objects:
        a = a + 1
        result_dict[i] = a


def same_date_filling(iter_obj, dt, same_date_list):
    for ind, res in enumerate(iter_obj):
        for ind_2, r in enumerate(iter_obj):
            if res[3] == dt and res == r:
                same_date_list.append(r)


def paginator_func(same_date_list, dt, result_dict):
    for date in same_date_list:
        if dt in date:
            page_number = result_dict[date]
            element_per_page = 10
            paginator = Paginator(same_date_list, element_per_page)
            page = paginator.get_page(page_number)
            content = page.object_list
            return content


def next_previous_pages(res, dp):
    next_date = None
    previous_date = None
    date_list = [r[3] for r in res]
    sorted_result = list(sorted(set(date_list)))
    for ind, r in enumerate(sorted_result):
        if r == dp:
            if sorted_result[ind] != sorted_result[-1]:
                next_date = sorted_result[ind + 1]
            if sorted_result[ind] != sorted_result[0]:
                previous_date = sorted_result[ind - 1]
            return next_date, previous_date


def date_books_view(request, value):
    template = 'books/books_list.html'

    result = {}
    dict_filling(result)

    date_pub = value.date()
    same_date = []
    iterate = list(result.keys())
    same_date_filling(iterate, date_pub, same_date)

    content = paginator_func(same_date, date_pub, result)

    next_prev = next_previous_pages(result, date_pub)

    context = {
        'page_books': content,
        'next_date': str(next_prev[0]),
        'previous_date': str(next_prev[1]),
        'absolute_uri': request.build_absolute_uri('/books/')
    }
    return render(request, template, context)


