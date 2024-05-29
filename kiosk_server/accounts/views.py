# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def post(self, request):
        user = request.user
        user.IsDeleted = True
        user.save()
        return Response({'message': '사용자 프로필이 삭제되었습니다.'}, status=status.HTTP_200_OK)

    def patch(self, request):
        user = request.user
        name = request.data.get('name')
        password = request.data.get('password')
        
        if name:
            user.name = name
        if password:
            user.set_password(password)  # 비밀번호를 해시하여 저장합니다.

        user.save()

        # 사용자 정보를 다시 불러와서 직렬화합니다.
        serializer = CustomUserSerializer(user)
        
        return Response({'message': '프로필 수정 완료.', 'data': serializer.data}, status=status.HTTP_200_OK)
