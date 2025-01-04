	1.	detector ve predictor Tanımları:
	•	detector: Yüz algılamak için kullanılır. Gri tonlamalı görüntüde yüzün yerini belirler.
	•	predictor: Yüzdeki 68 köşe noktasını belirler. Örneğin, gözlerin ve ağzın köşe noktaları.
	2.	Kamera Kullanımı:
	•	cv2.VideoCapture(0): Bilgisayarın varsayılan kamerasını açar.
	•	ret, frame = cap.read(): Kameradan görüntü alır. Eğer ret değeri False ise görüntü alınamamış demektir.
	3.	Yüz Tespiti:
	•	detector(gray): Gri tonlamalı görüntüde yüzleri bulur.
	•	face: Tespit edilen yüzün konum bilgilerini tutar.
	4.	Landmark Tespiti:
	•	predictor(gray, face): Tespit edilen yüz bölgesinde 68 noktanın konumlarını çıkarır.
	•	Her noktanın x ve y koordinatları bulunur.
	5.	Görüntü İşaretleme:
	•	cv2.circle(frame, (x, y), 2, (0, 255, 0), -1): Landmark noktalarını ekranda küçük yeşil dairelerle gösterir.
	6.	Çıkış Koşulu:
	•	'q' tuşuna basıldığında program durur ve kamera serbest bırakılır.
