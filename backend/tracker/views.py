from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ReadingProgress

class ProgressView(APIView):
    def post(self, request):
        data = request.data
        try:
            # Save or update progress
            progress, created = ReadingProgress.objects.update_or_create(
                user_id=data['user_id'],
                article_url=data['article_url'],
                defaults={
                    'progress_percentage': data['progress_percentage']
                }
            )
            return Response({"message": "Progress saved successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_id = request.GET.get('user_id')
        article_url = request.GET.get('article_url')
        try:
            progress = ReadingProgress.objects.get(user_id=user_id, article_url=article_url)
            return Response({
                "progress_percentage": progress.progress_percentage,
                "last_updated": progress.updated_at
            }, status=status.HTTP_200_OK)
        except ReadingProgress.DoesNotExist:
            return Response({"error": "Progress not found."}, status=status.HTTP_404_NOT_FOUND)
