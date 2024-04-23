import face_recognition
from PIL import Image, ImageDraw

def face_rec():
    tramp_face_img = face_recognition.load_image_file("img/AM2.jpg")
    tramp_face_location = face_recognition.face_locations(tramp_face_img)

    spider_img = face_recognition.load_image_file("img/as1.jpg")
    spider_faces_locations = face_recognition.face_locations(spider_img)

    # print(tramp_face_location)
    # print(spider_faces_locations)
    # print(f"Found {len(tramp_face_location)} face(s) in this image")
    # print(f"Found {len(spider_faces_locations)} face(s) in this image")

    pil_img1 = Image.fromarray(tramp_face_img)
    draw1 = ImageDraw.Draw(pil_img1)

    for (top, right, bottom, left) in tramp_face_location:
        draw1.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw1
    pil_img1.save("img/new_am.jpg")

    pil_img2 = Image.fromarray(spider_img)
    draw2 = ImageDraw.Draw(pil_img2)

    for (top, right, bottom, left) in spider_faces_locations:
        draw2.rectangle(((left, top), (right,bottom)), outline=(255,255,0),width=4)

    del draw2
    pil_img2.save("img/new_as.jpg")

def extracting_faces(img_path):
    count = 0
    faces = face_recognition.load_image_file(img_path)
    faces_locations = face_recognition.face_locations(faces)

    for face_location in faces_locations:
        top, right, bottom, left = face_location

        face_img = faces[top:bottom, left:right]
        pil_img = Image.fromarray(face_img)
        pil_img.save(f"img/{count}_face_img.jpg")
        count += 1

    return f"Found {count} face(s) in this photo"

def compare_faces(img1_path, img2_path):
    img1 = face_recognition.load_image_file(img1_path)
    img1_encodings = face_recognition.face_encodings(img1)[0]
    # print(img1_encodings)

    img2 = face_recognition.load_image_file(img2_path)
    img2_encodings = face_recognition.face_encodings(img2)[0]

    result = face_recognition.compare_faces([img1_encodings], img2_encodings)
    print(result)

def main():
    # face_rec()
    # print(extracting_faces("img/AM2.jpg"))
    compare_faces("img/Tesla.jpg","img/Tesla_comp.jpg")


if __name__ == '__main__':
    main()