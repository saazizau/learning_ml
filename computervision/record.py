import cv2

# Baca video yang telah direkam
video_file = "screen_recording.avi"
cap = cv2.VideoCapture(video_file)

while True:
    # Baca satu frame
    ret, frame = cap.read()

    # Keluar dari loop jika video sudah selesai
    if not ret:
        break

    # Tampilkan frame
    cv2.imshow("Screen Recording", frame)

    # Hentikan penampilan video ketika 'q' ditekan
    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

# Bebaskan sumber daya
cap.release()
cv2.destroyAllWindows()
