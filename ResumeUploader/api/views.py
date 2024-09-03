from rest_framework.views import APIView
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Profile


class ProfileView(APIView):
    def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':"Resume Uploaded Successfullly...",
                'Candidate':serializer.data,
            },status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def get(self,request,format=None):
        Candidates = Profile.objects.all()
        serializer = ProfileSerializer(Candidates,many=True)
        return Response({
            'status':'Success',
            'Candidates':serializer.data
        },status=status.HTTP_200_OK)