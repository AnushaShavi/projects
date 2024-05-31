import cv2
import numpy as np
import face_recognition

# Load sample images and create face encodings
known_image = face_recognition.load_image_file("kiara.jpeg")  # Replace with the path to your known face image
known_encoding = face_recognition.face_encodings(known_image)[0]

# Load sample images and create face encodings
known_image = face_recognition.load_image_file("sid.jpeg")  # Replace with the path to your known face image
known_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize variables
face_locations = []
face_encodings = []
face_names = []
attendance_list = set()

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches the known face
        matches = face_recognition.compare_faces([known_encoding], face_encoding)

        name = "Unknown"

        # If a match is found, update the name
        if True in matches:
            name = "Known Person"
            attendance_list.add(name)

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
video_capture.release()
cv2.destroyAllWindows()

# Print the attendance list
print("Attendance List:")
for name in attendance_list:
    print(name)
