from manim import *
from manim_slides import Slide

class ELBOSlide(Slide):
    def construct(self):
# --- 1. CẤU HÌNH MÀU SẮC ---
        COLOR_MATH = WHITE
        COLOR_HIGHLIGHT = "#FF5252" # Màu đỏ cam để nhấn mạnh

        # --- 2. ĐỊNH NGHĨA CÔNG THỨC ---
        
        # Công thức 1
        eq1 = MathTex(
            r"L = \mathbb{E}_q \left[ -\log \frac{p_\theta(\mathbf{x}_{0:T})}{q(\mathbf{x}_{1:T}|\mathbf{x}_0)} \right]",
            color=COLOR_MATH
        )

        # Công thức 2
        eq2 = MathTex(
            r"= \mathbb{E}_q \left[ -\log \frac{p(\mathbf{x}_T) \prod_{t=1}^T p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{\prod_{t=1}^T q(\mathbf{x}_t|\mathbf{x}_{t-1})} \right]",
            color=COLOR_MATH
        )

        # Công thức 3
        eq3 = MathTex(
            r"= \mathbb{E}_q \left[ -\log p(\mathbf{x}_T) - \sum_{t \ge 1} \log \frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{q(\mathbf{x}_t|\mathbf{x}_{t-1})} \right]",
            color=COLOR_MATH
        )

        # Công thức 4 (Dòng dài nhất - cần chú ý)
        eq4 = MathTex(
            r"= \mathbb{E}_q \Bigg[ -\log p(\mathbf{x}_T) - \sum_{t > 1} \log \frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{q(\mathbf{x}_t|\mathbf{x}_{t-1})} ",
            r"- \log \frac{p_\theta(\mathbf{x}_0|\mathbf{x}_1)}{q(\mathbf{x}_1|\mathbf{x}_0)} \Bigg]",
        )
        # Tô màu phần quan trọng của dòng 4
        eq4[1].set_color(COLOR_HIGHLIGHT)

        # --- 3. SẮP XẾP VỊ TRÍ ---
        
        # Nhóm tất cả lại
        equations = VGroup(eq1, eq2, eq3, eq4)
        
        # Căn lề trái và dãn dòng (giảm buff xuống 0.5 để tiết kiệm chỗ dọc)
        equations.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        # Thu nhỏ toàn bộ khối (scale 0.75)
        equations.scale(0.5)

        # Đẩy lên sát mép trên (cách lề trên 1 đơn vị)
        equations.to_edge(UP, buff=1.0)

        # --- 4. TRÌNH CHIẾU (SLIDES) ---
        
        # SLIDE 1
        self.play(Write(eq1), run_time=1.5)
        self.next_slide() 

        # SLIDE 2
        self.play(TransformFromCopy(eq1, eq2), run_time=1.5)
        self.next_slide()

        # SLIDE 3
        self.play(FadeIn(eq3, shift=DOWN * 0.2), run_time=1.5)
        self.next_slide()

        # SLIDE 4
        self.play(FadeIn(eq4, shift=DOWN * 0.2), run_time=1.5)
        self.play(Indicate(eq4[1], color=COLOR_HIGHLIGHT))
        
        self.next_slide() 
        
        COLOR_MATH = WHITE
        COLOR_HIGHLIGHT = "#FF5252"
        COLOR_BOX = WHITE # Màu của khung viền

        # Các công thức cũ (Bên trái)
        # Ban đầu ở bên phải (để chuẩn bị di chuyển)
        equations.to_edge(UP, buff=1.0)
        self.add(equations)

        # Công thức mới (Sẽ hiện bên phải)
        new_equation = MathTex(
            r"q(\mathbf{x}_t|\mathbf{x}_{t-1}) = \frac{q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0) \cdot q(\mathbf{x}_t|\mathbf{x}_0)}{q(\mathbf{x}_{t-1}|\mathbf{x}_0)}",
            color=COLOR_MATH
        )
        new_equation.scale(0.5)
        new_equation.to_edge(RIGHT, buff=1.0) # Căn phải

        # --- 2. HOẠT CẢNH DI CHUYỂN VÀ HIỆN CÔNG THỨC ---
        self.next_slide()

        # Di chuyển công thức cũ sang trái
        self.play(equations.animate.to_edge(LEFT, buff=1.0), run_time=1.5)
        self.next_slide()

        # Hiện công thức mới bên phải
        self.play(Write(new_equation), run_time=1.5)
        self.next_slide()

        # --- 3. HIỆU ỨNG ĐƯỜNG VIỀN CHẠY QUANH (MỚI THÊM) ---
        
        # Tạo khung hình chữ nhật bao quanh công thức mới
        box = SurroundingRectangle(new_equation, color=COLOR_BOX, buff=0.2, stroke_width=4)
        
        # Hiệu ứng vẽ đường viền (Create)
        self.play(Create(box), run_time=1.5)
        
        # Dừng lại để thuyết trình về công thức được đóng khung
        self.next_slide()
        top_group = VGroup(eq1, eq2, eq3, eq4)
        eq5 = MathTex(
            r"= \mathbb{E}_q \Bigg[ -\log \frac{p(\mathbf{x}_T)}{q(\mathbf{x}_T|\mathbf{x}_0)} - \sum_{t>1} \log \frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0)} - \log p_\theta(\mathbf{x}_0|\mathbf{x}_1) \Bigg]",
            color=COLOR_MATH
        )
        
        # Công thức 6 (Eq 22): Chuyển sang KL Divergence
        # D_KL(...) || ...)
        eq6 = MathTex(
            r"= \mathbb{E}_q \Bigg[ ", 
            r"D_{KL}(q(\mathbf{x}_T|\mathbf{x}_0) \| p(\mathbf{x}_T))", 
            r" + \sum_{t>1} ", 
            r"D_{KL}(q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0) \| p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t))", 
            r" - \log p_\theta(\mathbf{x}_0|\mathbf{x}_1) \Bigg]"
        )
        
        # Tô màu nổi bật các phần tử KL Divergence
        eq6[1].set_color(COLOR_HIGHLIGHT) # D_KL thứ nhất
        eq6[3].set_color(COLOR_HIGHLIGHT) # D_KL thứ hai

        # Nhóm 2 công thức mới
        new_group = VGroup(eq5, eq6)
        new_group.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        new_group.scale(0.5) # Kích thước vừa phải, lớn hơn nhóm trên 1 chút để dễ đọc
        
        # Đặt vị trí: Dưới nhóm cũ
        new_group.next_to(top_group, DOWN, buff=0.2).to_edge(LEFT, buff=1.0)

        # --- 4. TRÌNH CHIẾU ---
        
        # Bước 1: Hiện lại 4 công thức cũ (dạng Recap)
        # Bước 2: Viết công thức 5
        self.play(Write(eq5), run_time=2.0)
        self.next_slide()

        # Bước 3: Biến đổi sang công thức 6 (KL Divergence)
        self.play(TransformFromCopy(eq5, eq6), run_time=2.0)
        
        # Highlight KL Terms
        self.play(Indicate(eq6[1]), Indicate(eq6[3]), color=COLOR_HIGHLIGHT)
        
        self.next_slide()
        
        # Kết thúc
        self.play(FadeOut(top_group), FadeOut(new_group),FadeOut(new_equation),FadeOut(box))
        