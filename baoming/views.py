import logging

from rest_framework.views import APIView
# from rest_framework import status

from django.http import JsonResponse


logger = logging.getLogger(__name__)


class Persons(APIView):

    def get(self, request):
        """ Get all persons.
        """
        result = {
            1: 2
        }
        return JsonResponse(result)

    def post(self, request):
        """ Cteate a person.
        """

        return JsonResponse()
