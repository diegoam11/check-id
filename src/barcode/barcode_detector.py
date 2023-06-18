import cv2
from pyzbar import pyzbar


class BarcodeDetector:

    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.id = ''

    @staticmethod
    def validate_barcode(barcode_data):
        if barcode_data is not None and len(barcode_data) == 8:
            return barcode_data
        else:
            return None

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
                validated_data = self.validate_barcode(barcode_data)
                if validated_data is not None:
                    self.id = f"{validated_data}"
                    valid_barcode_count += 1
                else:
                    self.id = "Invalid Barcode"

                cv2.putText(frame, self.id, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                if valid_barcode_count >= 10:
                    break

            cv2.imshow("Barcode Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or valid_barcode_count >= 10:
                break

        self.video_capture.release()
        cv2.destroyAllWindows()

    def get_id(self):
        return self.id
