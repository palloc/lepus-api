# encoding=utf-8
from rest_framework import generics, permissions
from .serializers import TeamSerializer, UserSerializer, QuestionSerializer, CategorySerializer, FileSerializer, \
    AnswerSerializer, NoticeSerializer


class TeamListView(generics.ListAPIView):
    serializer_class = TeamSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        i = self.kwargs.get("pk")
        return self.model.objects.filter(id=i)

class AuthView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class QuestionView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        i = self.kwargs.get("pk")
        return self.model.objects.filter(id=i)


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        i = self.kwargs.get("pk")
        return self.model.objects.filter(id=i)

class FileView(generics.ListAPIView):
    serializer_class = FileSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        i = self.kwargs.get("pk")
        return self.model.objects.filter(id=i)

class AnswerView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        i = self.kwargs.get("pk")
        return self.model.objects.filter(id=i)

class NoticeView(generics.ListAPIView):
    serializer_class = NoticeSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        i = self.kwargs.get("pk")
        return self.model.objects.filter(id=i)

# TODO:AttackPointのAPIを開発する
