import threading
import cv2
import face_recognition

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

# List of reference images
reference_images = ["reference.jpg", "Mama.jpg", "as1.jpg"]

# Load face encodings for each reference image
reference_encodings = [face_recognition.face_encodings(face_recognition.load_image_file(ref))[0] for ref in reference_images]

def check_face(frame):
    global face_match

    try:
        face_encoding = face_recognition.face_encodings(frame)[0]
        face_match = any(face_recognition.compare_faces([ref_encoding], face_encoding)[0] for ref_encoding in reference_encodings)
    except IndexError:
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass

        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
