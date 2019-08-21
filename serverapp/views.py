from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from serverapp.serializers import PaperSerializer
from .models import Paper


@api_view(['GET'])
def get_all_papers(request):
        papers = Paper.objects.all()

        serializer = PaperSerializer(papers, many=True)
        return Response({"papers": serializer.data})


@api_view(['GET'])
def get_paper(request, pk):
        paper = get_object_or_404(Paper.objects.all(), pk=pk)

        serializer = PaperSerializer(paper, many=False)
        return Response({"papers": serializer.data})


@api_view(['POST'])
def create_paper(request):
        paper = request.data.get('paper')
        serializer = PaperSerializer(data=paper)
        if serializer.is_valid(raise_exception=True):
            paper_saved = serializer.save()
        return Response({"success": "Paper '{}' created successfully".format(paper_saved.title)})


@api_view(['POST'])
def update_paper(request, pk):
        saved_paper = get_object_or_404(Paper.objects.all(), pk=pk)
        data = request.data.get('paper')
        serializer = PaperSerializer(instance=saved_paper, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            paper_saved = serializer.save()
        return Response({
            "success": "Paper '{}' updated successfully".format(paper_saved.title)
        })


@api_view(['POST'])
def delete_paper(request, pk):
        # Get object with this pk
        paper = get_object_or_404(Paper.objects.all(), pk=pk)
        paper.delete()
        return Response({
            "message": "Paper with id `{}` has been deleted.".format(pk)
        }, status=204)




















# def user_login(request):
#     if request.method == "POST":
#         pass
#     else:
#         pass
#     return 0
#
#
# def user_logout(request):
#     logout(request)
#     return 0
#
#
# def register(request):
#     if request.method == 'POST':
#         pass
#     else:
#         pass
#     return 0