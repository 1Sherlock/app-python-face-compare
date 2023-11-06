from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import face_recognition

@api_view(['POST'])
@permission_classes([AllowAny])
def create_post(request):
    if request.method == 'POST':
        # Process the POST data and perform actions
        # ...

        # Return a JSON response
        return JsonResponse({'message': 'Post created successfully'})
    else:
        # Return an error response for other HTTP methods
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@api_view(['POST'])
@permission_classes([AllowAny])
def compare_faces(request):
    if request.method == 'POST':
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')

        # Load the face images
        image1 = face_recognition.load_image_file(file1)
        image2 = face_recognition.load_image_file(file2)

        # Encode the face images
        encoding1 = face_recognition.face_encodings(image1)[0]
        encoding2 = face_recognition.face_encodings(image2)[0]

        # Compare the face encodings
        results = face_recognition.compare_faces([encoding1], encoding2)

        # Check the results
        if results[0]:
            return JsonResponse({'message': 'Faces match', 'code': 0})
        else:
            return JsonResponse({'message': 'Faces do not match', 'code': -1})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)