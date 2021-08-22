from rest_framework.views import APIView
from django.http import HttpResponse
from decimal_to_hex.utils import dec_to_hex, is_integer


class DecToHexView(APIView):
    def post(self, request):
        number = request.data['number']
        if not is_integer(number):
            return HttpResponse("Number has to be an integer", status=400)
        result = dec_to_hex(number)
        return HttpResponse(result)
