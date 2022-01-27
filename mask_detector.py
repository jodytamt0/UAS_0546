import cv2

mask_on = False

faceCascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')
noseCascade = cv2.CascadeClassifier('./haarcascade/haarcascade_mcs_nose.xml')

if faceCascade.empty():
    raise IOError('File xml error')
if noseCascade.empty():
    raise IOError('File xml error')

cap = cv2.VideoCapture(0)
scale = 1

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    wajah = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in wajah:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if mask_on:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(frame, 'Mask On', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(frame, 'Mask Off', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    hidung = noseCascade.detectMultiScale(gray, 1.1, 20, )

    if len(hidung) > 0:
        mask_on = False
    else:
        mask_on = True

    cv2.putText(frame, 'Jumlah Wajah : ' + str(len(wajah)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Mask Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()