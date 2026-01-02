from manim import *
from manim_slides import Slide
import cv2  # pip install opencv-python

# ==============================================================================
# PHẦN 1: CLASS VIDEOMOBJECT (ĐÃ SỬA LỖI RGB -> RGBA)
# ==============================================================================
class VideoMobject(ImageMobject):
    def __init__(self, filename, speed=1.0, loop=False, **kwargs):
        self.filename = filename
        self.cap = cv2.VideoCapture(filename)
        self.speed = speed
        self.loop = loop
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.total_frames / self.fps
        # Biến theo dõi thời gian nội bộ của video
        self.internal_time = 0.0
        
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            super().__init__(frame, **kwargs)
        else:
            print(f"Lỗi đọc video: {filename}")
            super().__init__(np.zeros((100, 100, 4), dtype=np.uint8), **kwargs)

    def start_video(self):
        self.add_updater(self.video_updater)

    def stop_video(self):
        self.remove_updater(self.video_updater)

    def video_updater(self, mob, dt):
        # 1. Tính toán frame đích dựa trên thời gian trôi qua
        self.internal_time += dt * self.speed
        target_frame_index = int(self.internal_time * self.fps)
        
        # Lấy vị trí frame hiện tại của con trỏ file
        current_ptr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        
        frames_to_skip = target_frame_index - current_ptr

        # Nếu video đã hết
        if target_frame_index >= self.total_frames:
            if self.loop:
                self.internal_time = 0
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                frames_to_skip = 0
            else:
                self.remove_updater(self.video_updater)
                return

        # 2. Chiến thuật nhảy frame tối ưu
        ret = False
        frame = None

        if frames_to_skip > 0:
            # Nếu cần nhảy quá xa (ví dụ > 50 frame do lag), dùng set() để seek trực tiếp
            # set() chậm hơn grab() một chút nhưng nhanh hơn loop grab() rất nhiều nếu khoảng cách xa
            if frames_to_skip > 50:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame_index)
                ret, frame = self.cap.read()
            else:
                # TỐI ƯU QUAN TRỌNG: Dùng grab() để bỏ qua frame mà KHÔNG giải mã (decode)
                # Chỉ giải mã frame cuối cùng bằng read/retrieve
                for _ in range(frames_to_skip - 1):
                    self.cap.grab() 
                
                # Đọc frame đích thực sự
                ret, frame = self.cap.read()
        
            # 3. Chỉ convert màu cho frame cuối cùng sẽ hiển thị
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                mob.pixel_array = frame

    def __del__(self):
        # Giải phóng tài nguyên khi object bị hủy
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
# ==============================================================================
# PHẦN 2: SLIDE TRÌNH CHIẾU
# ==============================================================================
class video(Slide):
    def construct(self):
        self.slide_count = 36  # Số trang bắt đầu

        # 1. Hiển thị số trang ban đầu
        self.page_number = Text(f"{self.slide_count}", font_size=24, color=GRAY)
        self.page_number.to_corner(DR, buff=0.5)
        self.add(self.page_number) 
        self.wait(0.5)
        # 2. Định nghĩa hàm next_step (Dùng để thay thế self.next_slide ở đâu bạn muốn)
        def next_step():
            self.next_slide()  # Vẫn dừng slide như bình thường
            
            # Nhưng chạy tiếp thì sẽ tăng số trang
            self.slide_count += 1
            new_number = Text(f"{self.slide_count}", font_size=24, color=GRAY)
            new_number.to_corner(DR, buff=0.5)
            self.page_number.become(new_number)

        # Đường dẫn file (Bạn nhớ kiểm tra kỹ đường dẫn nhé)
        video_path = r".\Imgs\LastScene\video1.mp4"


        # --- BƯỚC 2: CHUYỂN SANG VIDEO ---
        try:
            video_obj = VideoMobject(video_path).scale_to_fit_width(5)
        except Exception as e:
            print(f"Lỗi tải video: {e}")
            return


        self.add(video_obj)
        
        # Chạy video
        video_obj.start_video()
        self.wait(video_obj.duration)
        video_obj.stop_video()
        
    