import cv2

# inisialisasi object tracker
tracker = cv2.TrackerCSRT_create()

# baca video dari kamera web
cap = cv2.VideoCapture(0)

# baca frame pertama
ret, frame = cap.read()

# tentukan ROI (Region of Interest)
roi = cv2.selectROI(frame, False)

# inisialisasi tracker dengan ROI
tracker.init(frame, roi)

# loop untuk membaca setiap frame dari video
while True:
    # baca frame berikutnya dari video
    ret, frame = cap.read()

    # update tracker dengan frame terbaru
    success, roi = tracker.update(frame)

    # gambar kotak di sekitar objek yang dilacak
    if success:
        (x, y, w, h) = tuple(map(int, roi))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # tampilkan frame
    cv2.imshow("Frame", frame)

    # jika user menekan tombol q, keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        breakc

# stop video stream dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()