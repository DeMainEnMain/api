import logging

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

from base_api import BaseAPIView
from dolibarr_api import DolibarrAPI, DolibarrAPIException
from prestataires import serializers
from pagination import CustomPagination

logger = logging.getLogger()


class PrestatairesAPIView(BaseAPIView):

    def __init__(self, **kwargs):
        super(PrestatairesAPIView, self).__init__()

    def list(self, request):
        """
        Récupérer la liste des prestataires.
        """
        language = request.GET.get('langue')
        keyword = request.GET.get('mot-cle')
        category_id = request.GET.get('categorie')
        town_id = request.GET.get('ville')
        zipcode = request.GET.get('code-postal')
        bdc = request.GET.get('bdc', False)
        euskokart = request.GET.get('euskokart', False)

        logger.debug('language=' + str(language))
        logger.debug('keyword=' + str(keyword))
        logger.debug('category_id=' + str(category_id))
        logger.debug('town_id=' + str(town_id))
        logger.debug('zipcode=' + str(zipcode))
        logger.debug('bdc=' + str(bdc))
        logger.debug('euskokart=' + str(euskokart))

        if not language:
            return Response({'error': 'The "langue" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        if language not in ('eu', 'fr'):
            return Response({'error': 'Invalid value for the "langue" parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        dolibarr = DolibarrAPI(api_key=request.user.profile.dolibarr_token)
#        return Response(dolibarr.get(model='towns', zipcode=search))

        objects = []
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(objects, request)
        return paginator.get_paginated_response(result_page)

    def retrieve(self, request, pk):
        pass
