from manim import *
from manim_slides import Slide

class KLDivergenceScene(Slide):
    def construct(self):
        # --- Cấu hình chung ---
        # Scale 0.5 cho toàn bộ nội dung như các slide trước
        
        # ==============================================================================
        # 1. CÔNG THỨC TỔNG QUÁT (Dòng trên cùng)
        # ==============================================================================
        
        # Sử dụng underbrace để tạo chú thích (A), (B), (C)
        # Lưu ý: \text{tr} dùng để viết chữ "tr" đứng (trace)
        eq_general = MathTex(
            r"D_{KL}(P\|Q) = \frac{1}{2} \left[ \underbrace{\log \frac{|\Sigma_2|}{|\Sigma_1|}}_{\mathbf{(A)}} - k + \underbrace{\text{tr}(\Sigma_2^{-1}\Sigma_1)}_{\mathbf{(B)}} + \underbrace{(\mu_2 - \mu_1)^T \Sigma_2^{-1}(\mu_2 - \mu_1)}_{\mathbf{(C)}} \right]"
        )

        # ==============================================================================
        # 2. CÔNG THỨC RÚT GỌN (Dòng dưới)
        # ==============================================================================
        
        # Bước thay thế số 0
        eq_simplified_step1 = MathTex(
            r"D_{KL}(P\|Q) = \frac{1}{2} \left[ 0 + 0 + \frac{1}{\sigma^2}\|\mu_1 - \mu_2\|^2 \right]"
        )

        # Kết quả cuối cùng
        eq_simplified_step2 = MathTex(
            r"= \frac{1}{2\sigma^2}\|\mu_1 - \mu_2\|^2"
        )
        
        # Gom nhóm phần rút gọn lại
        simplified_group = VGroup(eq_simplified_step1, eq_simplified_step2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        # Căn chỉnh dấu bằng cho thẳng hàng
        # Dịch dòng cuối sang phải một chút để dấu "=" thẳng với dòng trên
        eq_simplified_step2.shift(RIGHT * 0.5)

        # ==============================================================================
        # SẮP XẾP VÀ SCALE
        # ==============================================================================
        
        # Gom tất cả lại
        all_content = VGroup(
            eq_general,
            simplified_group
        ).arrange(DOWN, buff=1.0, aligned_edge=LEFT) # Tăng buff lên 1.0 để tách biệt 2 phần rõ hơn

        # Scale 0.5 toàn bộ
        all_content.scale(0.5)
        
        # Đưa vào giữa màn hình
        all_content.move_to(ORIGIN)

        # ==============================================================================
        # TRÌNH CHIẾU
        # ==============================================================================

        # Slide 1: Hiện công thức tổng quát
        self.play(Write(eq_general))
        self.next_slide()

        # Slide 2: Hiện bước thay thế (Dòng rút gọn 1)
        self.play(Write(eq_simplified_step1))
        self.next_slide()

        # Slide 3: Hiện kết quả cuối (Dòng rút gọn 2)
        self.play(Write(eq_simplified_step2))
        self.next_slide()
        
        # Slide 4: Fade Out
        self.play(FadeOut(all_content))