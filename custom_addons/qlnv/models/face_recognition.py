from odoo import fields, models, api
import cv2
import  os
import dlib
import face_recognition

class recognitionFace(models.Model):
    _name = 'cv.recognition_face'
    _description = ''

    name = fields.Char('name')
    
    
    def open_camera(self):
        # Khởi tạo camera
        cap = cv2.VideoCapture(0)  # 0 là chỉ số của camera mặc định, nếu có nhiều camera, bạn có thể thử các chỉ số khác nhau

        if not cap.isOpened():
            print("Không thể mở camera. Kiểm tra xem camera có được kết nối không.")
            return

        # Loop để hiển thị hình ảnh từ camera
        while True:
            ret, frame = cap.read()  # Đọc frame từ camera

            if not ret:
                print("Không thể nhận frame từ camera.")
                break

            # Hiển thị frame
            cv2.imshow('Camera', frame)

            # Nhấn 'q' để thoát khỏi vòng lặp
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Giải phóng camera và đóng cửa sổ hiển thị
        cap.release()
        cv2.destroyAllWindows()