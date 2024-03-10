from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import URL, Redirect
from .serializers import URLSerializer, UserSerializer, RedirectSerializer
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from . import utils


class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            serializer.save()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if request.user.is_authenticated and instance.author == request.user:
            redirects = Redirect.objects.filter(url=instance)
            redirect_serializer = RedirectSerializer(redirects, many=True)
            data = serializer.data
            data['redirect_analytics'] = redirect_serializer.data
            return Response(data)
        else:
            return Response({'detail': 'You do not have permission to view detailed statistics.'}, status=status.HTTP_403_FORBIDDEN)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def redirect_view(request, tinyurl):
    try:
        url = URL.objects.get(tinyurl=tinyurl)
        url.numberOfRedirects += 1
        url.save()
        redirect_instance = Redirect.objects.create(
            url=url,
            ip_address=utils.get_client_ip(request),
            country='not available',
            city='not available',
        )
        redirect_instance.save()
        return redirect(url.originalUrl)
    except URL.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def view_redirect_statistics(request, tinyurl):
    try:
        url_instance = URL.objects.get(tinyurl=tinyurl)
        if request.user != url_instance.author:
            return Response({'detail': 'You do not have permission to view these statistics.'}, status=403)
        
        redirects = Redirect.objects.filter(url=url_instance)
        serializer = RedirectSerializer(redirects, many=True)
        return Response(serializer.data)
    except URL.DoesNotExist:
        return Response({'detail': 'Not Found.'}, status=404)
