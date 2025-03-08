from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
import json
from .models import HealthData
from .serializers import HealthDataSerializer
from django.utils import timezone  # ✅ Import timezone
from django.utils.timezone import localtime
import pytz


# ✅ User Signup API
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

# ✅ User Login API
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# ✅ Protected API Example
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"}, status=status.HTTP_200_OK)

# ✅ Health Data Save API
@method_decorator(csrf_exempt, name='dispatch')
class SaveHealthDataView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = get_object_or_404(User, username=data.get("username"))

            # Convert lists to comma-separated strings for storage
            health_conditions = ",".join(data.get("healthConditions", []))
            medications = ",".join(data.get("medications", []))
            bad_habits = ",".join(data.get("badHabits", []))

            # ✅ Correct timestamp using IST timezone
            ist = pytz.timezone("Asia/Kolkata")  # ✅ Define IST timezone
            current_time = timezone.now().astimezone(ist).strftime("%Y-%m-%d %H:%M")  # ✅ Convert to IST properly

            health_data, created = HealthData.objects.update_or_create(
                username=user.username,
                defaults={
                    "gender": data["gender"],
                    "age": data["age"],
                    "weight": data["weight"],
                    "height": data["height"],
                    "sleep_hours": data["sleepHours"],
                    "water_intake": data["waterIntake"],
                    "activity_level": data["activityLevel"],
                    "daily_steps": data["dailySteps"],
                    "stress_level": data["stressLevel"],
                    "health_conditions": health_conditions,
                    "medications": medications,
                    "bad_habits": bad_habits,
                    "timestamp": current_time,  # ✅ Store correct IST time
                }
            )

            return JsonResponse({"message": "Health data saved successfully"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)