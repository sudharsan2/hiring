from django.shortcuts import render
from userManagement.serializer import RegisterSerializer, loginSerializer, userRolesSerializer, userSerializer
from rest_framework import generics, status, views, permissions, parsers
from .models import user, UserRoles
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class RegistrationView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    # renderer_classes = (UserRenderer,)

    def post(self, request):
        userpayload = request.data
        serializer = self.serializer_class(data=userpayload)
        serializer.is_valid(raise_exception=True)  # this is going to run a method called
        serializer.save()
        user_data = serializer.data
        user_obj = user.objects.get(email=user_data.get('email'))
        token = RefreshToken.for_user(user_obj).access_token
        
        
        #frontend_uri = os.environ.get('EMAIL_VERIFICATION_URL')
        #abs_urls = frontend_uri + '?token=' + str(token)
        return Response(user_data, status=status.HTTP_201_CREATED)
    
    
class LoginView(generics.GenericAPIView):
    serializer_class=loginSerializer
    def post(self, request):
         user = request.data
         serializer = self.serializer_class(data=user)
         serializer.is_valid(raise_exception=True)
         return Response(serializer.data, status=status.HTTP_200_OK)
     
class GetAllUsersView(generics.ListAPIView):
    serializer_class=userSerializer
    queryset=user.objects.all()
    permission_classes = [IsAuthenticated]
    
class GetAllRolesView(generics.ListAPIView):
    serializer_class=userRolesSerializer
    queryset=UserRoles.objects.all()
    permission_classes = [IsAuthenticated]
    
    