from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse, Http404
from django.db.models import Q

from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status, permissions


from .serializer import feedbackSerializer
from .models import feedback
from .forms import feedbackForm
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    return render(request, 'cvapp/index.html')


def home(request):
    
    form = feedbackForm()
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            msg=form.save(commit=False)
            msg.save()
            return redirect('thnx')
        
    msg = feedback.objects.all()

    context ={'form':form,'data':msg}
    return render(request, 'cvapp/Home.html', context)

def thanks(request):

    context = {}
    return render(request, 'cvapp/tnx.html', context)


# function based DRF below...........................................................................................


@api_view(['GET'])
def endpoint(request):
    data = ['/comments', '/comment_details/name']
    return Response(data)

@api_view(['Get',"POST"])
# @permissions([IsAuthenticated])
def comments(request, format=None):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query=''


        comment = feedback.objects.filter(Q(Name__icontains=query) | Q(feed__icontains = query))
        serializer = feedbackSerializer(comment, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        comment = feedback.objects.create(
            Name=request.data['Name'],
            feed=request.data['feed']
        )
        serializer = feedbackSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)
        

@api_view(['GET','PUT','DELETE'])
def comment_details(request, Name, format=None):
    comment = feedback.objects.get(Name=Name)

    if request.method == 'GET':
        serializer = feedbackSerializer(comment, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        comment.Name = request.data['Name']
        comment.feed= request.data['feed']
        comment.save()
        serializer = feedbackSerializer(comment, many=False, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_406_NOT_ACCEPTABLE)
        
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_410_GONE)


# class based DRF below...........................................................................................   



# class comments(APIView):
#     permission_classes=[permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         comments = feedback.objects.all()
#         serializer = feedbackSerializer(comments, many=True)
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
#     def post(self, request, format=None):
#         serializer = feedbackSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
#     # def perform_create(self, serializer):
#     #     serializer.save(user = self.request.user)
    
# class comment_details(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get_objects(self, Name):
#         try:
#             return feedback.objects.get(Name=Name)
#         except feedback.DoesNotExist:
#             raise Http404

#     def get(self, request, Name, format=None):
#         comment = self.get_objects(Name)
#         serializer = feedbackSerializer(comment)
#         return Response(serializer.data)

#     def put (self, request, Name, format=None):
#         comment = self.get_objects(Name)
#         serializer = feedbackSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, Name, format=None):
#         comment = self.get_objects(Name)
#         comment.delete()
#         return Response('comment deleted......')

# class Userlist(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class Userdetails(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer