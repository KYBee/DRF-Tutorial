from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""
조회 : GET
등록 : POST
수정 : PUT
삭제 : DELETE
"""

#Refactored Ver

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


'''
status codes
201 - HTTP_201_CREATED
204 - HTTP_204_NO_CONTENT
400 - HTTP_400_BAD_REQUEST
404 - HTTP_404_NOT_FOUND

'''


@api_view(['GET', 'POST'])
def snippet_list(request):
    # Get 은 Status code가 response에 필요 없나 보다.
    if request.method=="GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # JSonResponse 에서 Response 으로
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# BEFORE Refactoring

# @csrf_exempt
# def snippet_list(request):
    
#     # No need status code response
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         # Database Instance -> Python Dict
#         serializer = SnippetSerializer(snippets, many=True)
#         # Python Dict -> Json
#         return JsonResponse(serializer.data, safe=False)

#     # Need status code response
#     elif request.method == "POST":
#         # Json -> Python Dict
#         data = JSONParser().parse(request)
#         # Python Dict -> Database Instance
#         serializer = SnippetSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request, pk):

#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         # instance로 snippet을 넣어줌. Update라서
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == "DELETE":
#         snippet.delete()
#         return HttpResponse(status=204)


