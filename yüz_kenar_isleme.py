import cv2  # OpenCV kütüphanesi, görüntü işleme için kullanılır
import dlib  # dlib kütüphanesi, yüz tespiti ve özellik çıkarımı için kullanılır

# dlib'in önceden eğitilmiş yüz tespit modeli (yüz algılama için kullanılır)
detector = dlib.get_frontal_face_detector()

# dlib'in yüz köşe noktalarını (landmark) tespit eden modeli
# Bu model, "shape_predictor_68_face_landmarks.dat" dosyasını kullanır
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Kamerayı başlatma işlemi (0, varsayılan kamera anlamına gelir)
cap = cv2.VideoCapture(0)

while True:  # Kameradan sürekli olarak görüntü alabilmek için sonsuz döngü
    ret, frame = cap.read()  # Kameradan bir kare (frame) oku
    if not ret:  # Kamera bir görüntü sağlamıyorsa döngüyü bitir
        break

    # Alınan görüntüyü gri tonlamaya çevir (yüz tespiti gri görüntüde daha hızlıdır)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gri tonlamalı görüntüde yüzleri tespit et
    faces = detector(gray)  # "faces", tespit edilen yüzlerin koordinatlarını tutar

    # Tespit edilen her yüz için işlem yap
    for face in faces:
        # Tespit edilen yüz bölgesinde yüz landmark'larını belirle
        landmarks = predictor(gray, face)

        # Yüzde toplamda 68 nokta bulunur (gözler, burun, ağız gibi bölgeler)
        for n in range(0, 68):  # Her bir landmark noktası için döngü
            x = landmarks.part(n).x  # Landmark noktasının x koordinatı
            y = landmarks.part(n).y  # Landmark noktasının y koordinatı

            # Landmark noktasını ekranda yeşil bir daire olarak işaretle
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    # İşlenmiş görüntüyü ekranda göster
    # "FacialEdgeDetector" penceresi adıyla görüntü açılır
    cv2.imshow("FacialEdgeDetector", frame)

    # Kullanıcı 'q' tuşuna bastığında döngüden çık ve programı sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak (kaynakları boşalt)
cap.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()