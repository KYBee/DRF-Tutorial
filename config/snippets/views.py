from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.views.decorator.csrf import csrf_exempt
from res_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""
조회 : GET
등록 : POST
수정 : PUT
삭제 : DELETE
"""

@csrf_exempt
def snippet_list(request):
    
    # No need status code response
    if request.method == "GET":
        snippets = Snippet.objects.all()
        # Database Instance -> Python Dict
        serializer = SnippetSerializer(snippets, many=True)
        # Python Dict -> Json
        return JsonResponse(serializer.data, safe=False)

    # Need status code response
    elif request.method == "POST":
        # Json -> Python Dict
        data = JSONParser().parse(request)
        # Python Dict -> Database Instance
        serializer = SnippetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):

    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        # instance로 snippet을 넣어줌. Update라서
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)


