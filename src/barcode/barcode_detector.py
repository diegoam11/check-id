import cv2
from pyzbar import pyzbar


class BarcodeDetector:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)

    def is_valid_barcode(self, barcode_data):
        if barcode_data is not None and len(barcode_data) == 7:
            return True
        return False

    def detect_barcodes(self):
        valid_barcode_count = 0

        while True:
            ret, frame = self.video_capture.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            barcodes = pyzbar.decode(gray)

            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                barcode_data = barcode.data.decode("utf-8")

                if self.is_valid_barcode(barcode_data):
                    text = f"{barcode_data}"
                    return text
                    valid_barcode_count += 1
                else:
                    text = "Invalid Barcode"

                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(f"Barcode: {barcode_data}")

                if valid_barcode_count >= 3:
                    break

            cv2.imshow("Barcode Detection", frame)

            if cv2.waitKey(0) or valid_barcode_count >= 3:
                break

        self.video_capture.release()
        cv2.destroyAllWindows()
