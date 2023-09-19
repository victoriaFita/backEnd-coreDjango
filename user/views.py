from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.hashers import check_password
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)

@method_decorator(csrf_exempt, name='dispatch')
def change_password(request, user_id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        user = User.objects.get(pk=user_id)
        
        current_password = data.get("current_password")
        new_password = data.get("new_password")
        
        if not check_password(current_password, user.password):
            return JsonResponse({"success": False, "message": "Senha atual incorreta."}, status=400)
        
        user.set_password(new_password)
        user.save()
        
        return JsonResponse({"success": True, "message": "Senha alterada com sucesso."})

    return HttpResponse(status=405)