import cv2

# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to perform face detection
def detect_faces(image):
    # Convert the image to grayscale (Haar cascades work on grayscale images)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image

# Load an image from file
image_path = '/Images/alotPeople.jpg'
image = cv2.imread(image_path)

# Perform face detection on the image
image_with_faces = detect_faces(image)

# Display the result
cv2.imshow('Face Detection', image_with_faces)
cv2.waitKey(0)
cv2.destroyAllWindows()