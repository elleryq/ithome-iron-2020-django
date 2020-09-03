#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class ExampleView(APIView):
    authentication_classes = [JSONWebTokenAuthentication,]  #
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'username': request.user.username,  # `django.contrib.auth.User` instance.
        }
        return Response(content)
