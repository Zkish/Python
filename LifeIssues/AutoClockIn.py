import cv2
import dlib
import face_recognition

# Load the known face images and their names
# Replace 'path_to_person1.jpg', 'path_to_person2.jpg', etc. with the paths to your images
known_face_images = [
    face_recognition.load_image_file('path_to_person1.jpg'),
    face_recognition.load_image_file('path_to_person2.jpg'),
    # Add more images here for additional known faces
]

# Replace 'Person 1', 'Person 2', etc. with the names of the corresponding persons
known_face_names = [
    'Person 1',
    'Person 2',
    # Add more names here for additional known faces
]

# Compute the face encodings for the known face images
known_face_encodings = [face_recognition.face_encodings(image)[0] for image in known_face_images]

# Open the video stream
# Replace 'path_to_your_video.mp4' with the path to your video file or use 0 for the default camera
video_path = 'path_to_your_video.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Find face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Perform face recognition for each detected face
    for face_encoding in face_encodings:
        # Compare the face encoding with the known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # Check if there is a match
        name = "Unknown"
        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]

        # Draw a rectangle and label the recognized face in the frame
        top, right, bottom, left = face_locations[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the frame with face recognition
    cv2.imshow('Face Recognition', frame)

        # # clock the person whos face appeared in.
    # if known_face_names == "":
    #     # put the clock in info here and the name of person in the parenthesis.
    #     break
    # # add in more if statements and elif statements for however many people there are that should be clocking in.

    # Exit the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
