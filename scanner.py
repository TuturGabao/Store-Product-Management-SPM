import ctypes
import cv2
from pyzbar.pyzbar import decode

def barcode_scanner():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    cv2.namedWindow('Scanner', cv2.WND_PROP_VISIBLE)
    cv2.resizeWindow('Scanner', 640, 480)
    
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video device.")
        return
    
    while True:
        ret, frame = cap.read()

        detectedBarcodes = decode(frame)
        for barcode in detectedBarcodes:
            barcode_data = barcode.data.decode('utf-8')
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data
        
        cv2.imshow('Scanner', frame)
        user32.SetForegroundWindow(user32.FindWindowW(None, 'Scanner'))
            
        if cv2.waitKey(1) == ord('q'):
            break

        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()
