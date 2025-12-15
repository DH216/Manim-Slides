from manim import *
from manim_slides import Slide
import cv2  # pip install opencv-python

# ==============================================================================
# PHẦN 1: CLASS VIDEOMOBJECT (ĐÃ SỬA LỖI RGB -> RGBA)
# ==============================================================================
class VideoMobject(ImageMobject):
    def __init__(self, filename, speed=1.0, **kwargs):
        self.filename = filename
        self.cap = cv2.VideoCapture(filename)
        self.speed = speed
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.total_frames / self.fps
        
        ret, frame = self.cap.read()
        if ret:
            # QUAN TRỌNG: Dùng BGR2RGBA (4 kênh) thay vì BGR2RGB (3 kênh)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            super().__init__(frame, **kwargs)
        else:
            print(f"Lỗi đọc video: {filename}")
            # Tạo ảnh rỗng 4 kênh nếu lỗi
            super().__init__(np.zeros((100, 100, 4), dtype=np.uint8), **kwargs)

    def start_video(self):
        self.add_updater(self.video_updater)

    def stop_video(self):
        self.remove_updater(self.video_updater)

    def video_updater(self, mob, dt):
        frames_to_skip = int(self.fps * dt * self.speed)
        # Nếu máy chậm, ít nhất phải load 1 frame để video chạy
        for _ in range(max(1, frames_to_skip)):
            ret, frame = self.cap.read()
            if ret:
                # QUAN TRỌNG: Cũng phải dùng BGR2RGBA ở đây
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                mob.pixel_array = frame
            else:
                # Hết video thì dừng update
                mob.remove_updater(self.video_updater)
                break

# ==============================================================================
# PHẦN 2: SLIDE TRÌNH CHIẾU
# ==============================================================================
class video(Slide):
    def construct(self):
        # Đường dẫn file (Bạn nhớ kiểm tra kỹ đường dẫn nhé)
        image_path = r".\Imgs\LastScene\img1.png"
        video_path = r".\Imgs\LastScene\video1.mov"

        # --- BƯỚC 1: HIỆN ẢNH TĨNH ---
        try:
            image = ImageMobject(image_path)
            self.add(image)
        except IOError:
            print(f"Lỗi: Không tìm thấy file ảnh '{image_path}'!")
            return

        # Dừng chờ bấm nút Next
        self.next_slide() 

        # --- BƯỚC 2: CHUYỂN SANG VIDEO ---
        try:
            video_obj = VideoMobject(video_path)
        except Exception as e:
            print(f"Lỗi tải video: {e}")
            return
        image.scale(0.5)
        # Khớp kích thước video với ảnh
        video_obj.match_width(image)
        video_obj.move_to(image.get_center())

        # Xóa ảnh, thêm video ngay lập tức
        self.play(FadeIn(image))
        self.next_slide()
        self.remove(image)
        self.add(video_obj)
        
        # Chạy video
        video_obj.start_video()
        self.wait(video_obj.duration)
        video_obj.stop_video()
        
        self.next_slide()