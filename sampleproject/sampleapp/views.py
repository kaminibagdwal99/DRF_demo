from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentView(APIView):
    def get(self, request,id):
        result= Student.objects.get(id=id)
        if id:
            serializer = StudentSerializer(result)
            return Response({'status':'success', 'students':serializer.data}, status=200)

        result = Student.objects.all()
        serializer = StudentSerializer(result, many= True)
        return Response({'status':'success', 'students':serializer.data}, status=200)

    def post(self,request):
        seriliazer = StudentSerializer(data = request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response({"status": "success", "data": seriliazer.data}, status=status.HTTP_200_OK)  
        else:
            return Response({"status": "error", "data": seriliazer.errors}, status=status.HTTP_400_BAD_REQUEST) 

    def patch(self,request,id):
        result = Student.objects.get(id=id)
        serializer = StudentSerializer(result,data =request.data,partial = True)
        if serializer.is_valid():
            serializer.save() 

            return Response({"status": "success", "data": serializer.data})  
        else:
            return Response({"status": "error", "data": serializer.errors}) 

    def delete(self, request, id=None):  
        result = get_object_or_404(Student, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})  

