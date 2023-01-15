from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from knox.auth import TokenAuthentication
from django.db.models import Q, F
from rest_framework.views import APIView
from django.db.models.functions import Concat
from django.db.models import Value, CharField
from django.db.models.functions import Round
from rest_framework.exceptions import APIException

from chatproject.base_paginations import OnOffPagination
from chatproject.base_decorators import *
import chatproject.base_functions as base_f
from .models import *
# Create your views here.

# def HomeView(request):
    #! authenticated 2x users websockets data update realtime.
    # return render(request, 'index.html')

class HomeView(APIView):
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    queryset = Logs.objects.annotate(
                                user_name=Concat('user__first_name', Value(' '), 'user__last_name', output_field=CharField())
                                , percent_completed_rounded = Round('percent_completed')
                                            ).values(
                                                'status'
                                                , 'error_msg'
                                                , 'user_name'
                                                , 'percent_completed_rounded'
                                            )

    def get_filter(self):
        filter = {}
        exclude = {}
        or_filter = Q()  # New Introduce Want to include or conditon in filter
        status = self.request.query_params.get('status', None)
        from rest_framework import status as api_status
        if status and status.lower() not in ('pending', 'successful', 'failed'):
            raise APIException({'status_code': api_status.HTTP_400_BAD_REQUEST, 'request_status': 0,  'msg': 'Please provide pending, successful or failed in status prams.'})
            # raise Exception("Please provide pending, successful or failed in status prams.")

        if status:
            filter['status'] = status

        # print('filter',filter)
        queryset = self.queryset.filter(**filter).filter(or_filter).exclude(**exclude).order_by('-id')
        # queryset=queryset.annotate(company_name=F('company__name'),company=F('company'))
        # queryset=queryset.annotate(company_name=F('company__name'),)

        # choices = dict(DocumentMergeHistory._meta.get_field('status').get_choices())
        # queryset = queryset.annotate(
        #                         merge_status = Case(
        #                             When(status__in=list(choices.keys()), then = Value(choices[F('status')]))
        #                             , output_field=CharField()
        #                         )
        #                 )

        return queryset

    @response_modify_decorator_list_or_get_after_execution_for_onoff_pagination
    def get(self, request, *args, **kwargs):
        count = self.request.query_params.get('count')

        # Pagination Functionality
        paginator = OnOffPagination()
        page_size = self.request.GET['page_size']

        # Filter
        self.queryset = self.get_filter()

        # Extra Fields insert to Queryset
        #self.queryset = self.extra_field_insert_to_queryset()

        field_name = self.request.query_params.get('ordering')
        if field_name:
            self.queryset = base_f.get_sorted_by_fields(self, self.queryset)

        if page_size == '0':
            response = self.queryset
            if count:
                count = len(response)
                return Response({'total_count': count})
        else:
            result_page = paginator.paginate_queryset(self.queryset, request)
            response = paginator.get_paginated_response(result_page)
            response = response.data

        return Response(response)
