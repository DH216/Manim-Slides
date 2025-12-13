from manim import *
from manim_slides import Slide

class DiffusionPresentation(Slide):
    def construct(self):
        # --- Cấu hình font chữ ---
        # Lưu ý: Không đặt font_size cố định ở đây nữa để dùng scale sau
        font_name = "Arial" 

        # ==============================================================================
        # 1. CÔNG THỨC ĐẦU TIÊN (Xuất hiện trước nhất)
        # ==============================================================================
        equation = MathTex(
            r"q(x_{t-1} | x_t, x_0) = \frac{1}{\sqrt{2\pi\beta}} \exp \left( -\frac{1}{2\beta}\left({x_{t-1}}\right)^2 + \frac{\mu}{\beta}x_{t-1} - \frac{1}{2\beta}\mu^2 \right)"
        )

        # ==============================================================================
        # 2. CÁC NHÓM NỘI DUNG SAU (Định lý Bayes & Gaussian)
        # ==============================================================================

        # --- Nhóm Bayes ---
        text_bayes = Text(
            "Theo định lý Bayes, xác suất hậu nghiệm tỉ lệ thuận với tích của likelihood và prior:",
            font=font_name
        )
        eq_bayes = MathTex(
            r"q(x_{t-1} | x_t, x_0) = \frac{q(x_t|x_{t-1})q(x_{t-1}|x_0)}{q(x_t|x_0)} \propto q(x_t|x_{t-1})q(x_{t-1}|x_0)"
        )
        group_bayes = VGroup(text_bayes, eq_bayes).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # --- Nhóm Gaussian ngắn gọn ---
        text_gaussian = Text(
            "Với các phân phối thành phần là Gaussian:",
            font=font_name
        )
        eq_short_1 = MathTex(
            r"q(x_t|x_{t-1}) = \mathcal{N}(x_t; \sqrt{\alpha_t}x_{t-1}, \beta_t \mathbf{I})"
        )
        eq_short_2 = MathTex(
            r"q(x_{t-1}|x_0) = \mathcal{N}(x_{t-1}; \sqrt{\bar{\alpha}_{t-1}}x_0, (1 - \bar{\alpha}_{t-1})\mathbf{I})"
        )
        short_eq_group = VGroup(eq_short_1, eq_short_2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        group_gaussian_intro = VGroup(text_gaussian, short_eq_group).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        # --- Nhóm Gaussian chi tiết ---
        eq_detailed_1 = MathTex(
            r"q(x_{t-1} | x_0) = \frac{1}{(2\pi(1 - \bar{\alpha}_{t-1}))^{d/2}} \exp \left[ -\frac{1}{2(1 - \bar{\alpha}_{t-1})} \|x_{t-1} - \sqrt{\bar{\alpha}_{t-1}}x_0\|^2 \right]."
        )
        eq_detailed_2 = MathTex(
            r"q(x_t | x_{t-1}) = \frac{1}{(2\pi\beta_t)^{d/2}} \exp \left[ -\frac{1}{2\beta_t} \|x_t - \sqrt{\alpha_t}x_{t-1}\|^2 \right]."
        )
        group_detailed = VGroup(eq_detailed_1, eq_detailed_2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # ==============================================================================
        # SẮP XẾP VÀ SCALE (0.5)
        # ==============================================================================
        
        # Gom TẤT CẢ vào một nhóm lớn, bao gồm cả equation đầu tiên
        all_content = VGroup(
            equation,              # 1. Công thức đầu
            group_bayes,           # 2. Bayes
            group_gaussian_intro,  # 3. Gaussian ngắn
            group_detailed         # 4. Gaussian chi tiết
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        # --- THỰC HIỆN SCALE 0.5 CHO TẤT CẢ TẠI ĐÂY ---
        all_content.scale(0.5)

        # Đưa vào giữa màn hình
        all_content.move_to(ORIGIN)

        # ==============================================================================
        # TRÌNH CHIẾU (SLIDES)
        # ==============================================================================

        # Slide 1: Hiện công thức đầu tiên (equation)
        self.play(Write(equation))
        self.next_slide() 

        # Slide 2: Hiện nhóm Bayes
        self.play(Write(group_bayes))
        self.next_slide()

        # Slide 3: Hiện nhóm Gaussian ngắn
        self.play(Write(group_gaussian_intro))
        self.next_slide()

        # Slide 4: Hiện nhóm Gaussian chi tiết
        self.play(Write(eq_detailed_1))
        self.next_slide()
        self.play(Write(eq_detailed_2))
        self.next_slide()
        self.play(FadeOut(equation),FadeOut(group_bayes),FadeOut(group_gaussian_intro),FadeOut(eq_detailed_1),FadeOut(eq_detailed_2))
        self.next_slide()
        # ==============================================================================
        # 1. CÔNG THỨC TỪ ẢNH TRƯỚC (Log-likelihood)
        # ==============================================================================
        eq_log_posterior = MathTex(
            r"-\log q(x_{t-1}|x_t, x_0) \propto \frac{1}{2\beta_t}(x_t - \sqrt{\alpha_t}x_{t-1})^2 + \frac{1}{2(1-\bar{\alpha}_{t-1})}(x_{t-1} - \sqrt{\bar{\alpha}_{t-1}}x_0)^2"
        )

        # ==============================================================================
        # 2. CÔNG THỨC TỪ ẢNH VỪA GỬI (Khai triển & Nhóm)
        # ==============================================================================
        
        # Dòng khai triển (bắt đầu bằng dấu =)
        eq_expansion = MathTex(
            r"= \frac{1}{2\beta_t} \left(x_t^2 - 2\sqrt{\alpha_t}x_t x_{t-1} + \alpha_t x_{t-1}^2\right) + \frac{1}{2(1-\bar{\alpha}_{t-1})} \left(x_{t-1}^2 - 2\sqrt{\bar{\alpha}_{t-1}}x_0 x_{t-1} + \bar{\alpha}_{t-1}x_0^2\right)"
        )

        # Dòng nhóm A, B (Sử dụng underbrace)
        eq_grouped = MathTex(
            r"= \frac{1}{2} \underbrace{\left[ \frac{\alpha_t}{\beta_t} + \frac{1}{1 - \bar{\alpha}_{t-1}} \right]}_{\mathbf{A}} x_{t-1}^2 - \underbrace{\left[ \frac{\sqrt{\alpha_t}}{\beta_t}x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}}{1 - \bar{\alpha}_{t-1}}x_0 \right]}_{\mathbf{B}} x_{t-1} + C(x_t, x_0)"
        )

        # ==============================================================================
        # SẮP XẾP VÀ SCALE 0.5
        # ==============================================================================
        
        # Gom 3 công thức này lại
        all_content = VGroup(
            eq_log_posterior,
            eq_expansion,
            eq_grouped
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT) # Căn lề trái thẳng hàng dấu bằng (nếu viết tách rời cần chỉnh lại chút, nhưng align LEFT là ổn nhất cho khối này)

        # Scale 0.5 cho tất cả
        all_content.scale(0.5)

        # Đặt vào giữa màn hình
        all_content.move_to(ORIGIN)

        # ==============================================================================
        # TRÌNH CHIẾU
        # ==============================================================================

        # Slide 1: Hiện dòng Log-likelihood
        self.play(Write(eq_log_posterior))
        self.next_slide()

        # Slide 2: Hiện dòng Khai triển
        self.play(Write(eq_expansion))
        self.next_slide()

        # Slide 3: Hiện dòng Nhóm (A, B)
        self.play(Write(eq_grouped))
        self.next_slide()

        # Slide 4: Fade out toàn bộ
        self.play(FadeOut(all_content))
        self.next_slide()# ==============================================================================
# ==============================================================================
        # 1. PHẦN CŨ (Tính nghịch đảo phương sai)
        # ==============================================================================
        
        # Tiêu đề
        text_start = Text("Từ hệ số", font=font_name)
        text_A = MathTex(r"\mathbf{A}")
        text_end = Text(", ta có nghịch đảo của phương sai:", font=font_name)
        header_group = VGroup(text_start, text_A, text_end).arrange(RIGHT, buff=0.1)
        
        # Các bước khai triển (Steps 1-4)
        eq_step1 = MathTex(r"\frac{1}{\tilde{\beta}_t} = \frac{\alpha_t}{\beta_t} + \frac{1}{1 - \bar{\alpha}_{t-1}}")
        eq_step2 = MathTex(r"= \frac{\alpha_t(1 - \bar{\alpha}_{t-1}) + \beta_t}{\beta_t(1 - \bar{\alpha}_{t-1})}")
        
        # Step 3 + Chú thích
        eq_step3_main = MathTex(r"= \frac{\alpha_t - \bar{\alpha}_t + 1 - \alpha_t}{\beta_t(1 - \bar{\alpha}_{t-1})}")
        note_text1 = Text("(với ", font=font_name,font_size=32)
        note_math1 = MathTex(r"\beta_t = 1 - \alpha_t")
        note_text2 = Text(" và ", font=font_name, font_size=32)
        note_math2 = MathTex(r"\bar{\alpha}_t = \alpha_t \bar{\alpha}_{t-1})", )
        note_group = VGroup(note_text1, note_math1, note_text2, note_math2).arrange(RIGHT, buff=0.2)
        eq_step3_full = VGroup(eq_step3_main, note_group).arrange(RIGHT, buff=0.5)

        eq_step4 = MathTex(r"= \frac{1 - \bar{\alpha}_t}{\beta_t(1 - \bar{\alpha}_{t-1})}")

        # Gom nhóm cũ
        old_equations = VGroup(eq_step1, eq_step2, eq_step3_full, eq_step4).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        # Căn chỉnh dấu bằng (Shift sang phải)
        shift_amount = 0.6 * RIGHT 
        eq_step2.shift(shift_amount)
        eq_step3_full.shift(shift_amount)
        eq_step4.shift(shift_amount)

        # ==============================================================================
        # 2. PHẦN MỚI (Suy ra phương sai hậu nghiệm)
        # ==============================================================================
        
        # Văn bản dẫn dắt
        text_conclusion = Text("Suy ra phương sai hậu nghiệm:", font=font_name)
        
        # Công thức cuối cùng
        eq_final = MathTex(
            r"\tilde{\beta}_t = \frac{1 - \bar{\alpha}_{t-1}}{1 - \bar{\alpha}_t} \beta_t"
        )
        
        # Gom nhóm mới
        conclusion_group = VGroup(text_conclusion, eq_final).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        # ==============================================================================
        # SẮP XẾP TỔNG THỂ
        # ==============================================================================
        
        # Gom tất cả vào một khối lớn
        all_content = VGroup(
            header_group,   # Tiêu đề
            old_equations,  # Các bước tính toán trên
            conclusion_group # Kết quả cuối cùng (MỚI)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT) # Căn trái toàn bộ

        # Scale 0.5
        all_content.scale(0.5)
        all_content.move_to(ORIGIN)

        # ==============================================================================
        # TRÌNH CHIẾU
        # ==============================================================================

        # Slide 1-5: Nội dung cũ
        self.play(Write(header_group))
        self.next_slide()

        self.play(Write(eq_step1))
        self.next_slide()

        self.play(Write(eq_step2))
        self.next_slide()

        self.play(Write(eq_step3_full))
        self.next_slide()

        self.play(Write(eq_step4))
        self.next_slide()

        # Slide 6: Hiện dòng chữ "Suy ra..."
        self.play(Write(text_conclusion))
        self.next_slide()

        # Slide 7: Hiện công thức cuối cùng
        self.play(Write(eq_final))
        self.next_slide()
        
        # Slide 8: Fade Out
        self.play(FadeOut(all_content))
# ==============================================================================
        # 1. TIÊU ĐỀ: TỪ HỆ SỐ B VÀ PHƯƠNG TRÌNH...
        # ==============================================================================
        
        # Tạo các thành phần text và math riêng để dễ format
        text_1 = Text("Từ hệ số", font=font_name)
        math_B = MathTex(r"\mathbf{B}")
        text_2 = Text("và phương trình", font=font_name)
        math_eq_ref = MathTex(r"\tilde{\mu}_t = \tilde{\beta}_t \cdot \mathbf{B}:")
        
        # Gom lại thành 1 dòng
        header_group = VGroup(text_1, math_B, text_2, math_eq_ref).arrange(RIGHT, buff=0.15)
        
        # ==============================================================================
        # 2. KHAI TRIỂN TÍNH TOÁN MU_TILDE
        # ==============================================================================
        
        # Dòng 1: Thay thế Beta_tilde và B vào
        eq_mean_step1 = MathTex(
            r"\tilde{\mu}_t = \left( \frac{1 - \bar{\alpha}_{t-1}}{1 - \bar{\alpha}_t} \beta_t \right) \left( \frac{\sqrt{\alpha_t}}{\beta_t}x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}}{1 - \bar{\alpha}_{t-1}}x_0 \right)"
        )
        
        # Dòng 2: Rút gọn
        eq_mean_step2 = MathTex(
            r"= \frac{\sqrt{\alpha_t}(1 - \bar{\alpha}_{t-1})}{1 - \bar{\alpha}_t}x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1 - \bar{\alpha}_t}x_0"
        )
        
        # Gom nhóm khai triển
        derivation_group = VGroup(eq_mean_step1, eq_mean_step2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        # Căn chỉnh dấu bằng cho đẹp (Dịch dòng 2 sang phải một chút)
        # Shift amount ước lượng để dấu bằng thẳng hàng
        eq_mean_step2.shift(RIGHT * 0.8)

        # ==============================================================================
        # 3. KẾT LUẬN
        # ==============================================================================
        
        # Text kết luận
        # Dùng Text với weight="BOLD" để in đậm giống trong ảnh
        text_conclusion = Text("Kết luận: Phân phối hậu nghiệm được xác định chính xác là:", font=font_name, weight="BOLD")
        
        # Công thức phân phối chuẩn cuối cùng
        eq_final_distribution = MathTex(
            r"q(x_{t-1}|x_t, x_0) = \mathcal{N}(x_{t-1}; \tilde{\mu}_t(x_t, x_0), \tilde{\beta}_t \mathbf{I})"
        )
        
        # Gom nhóm kết luận
        conclusion_group = VGroup(text_conclusion, eq_final_distribution).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        # ==============================================================================
        # SẮP XẾP TỔNG THỂ VÀ SCALE
        # ==============================================================================
        
        # Gom tất cả các phần lại
        all_content = VGroup(
            header_group,
            derivation_group,
            conclusion_group
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT) # Tăng buff một chút giữa các phần lớn cho thoáng

        # Scale 0.5 toàn bộ
        all_content.scale(0.5)
        
        # Đưa vào giữa màn hình
        all_content.move_to(ORIGIN)

        # ==============================================================================
        # TRÌNH CHIẾU
        # ==============================================================================

        # Slide 1: Hiện tiêu đề
        self.play(Write(header_group))
        self.next_slide()

        # Slide 2: Hiện dòng thế số
        self.play(Write(eq_mean_step1))
        self.next_slide()

        # Slide 3: Hiện kết quả rút gọn
        self.play(Write(eq_mean_step2))
        self.next_slide()

        # Slide 4: Hiện dòng chữ Kết luận
        self.play(Write(text_conclusion))
        self.next_slide()

        # Slide 5: Hiện công thức cuối cùng
        self.play(Write(eq_final_distribution))
        self.next_slide()
        
        # Slide 6: Fade out
        self.play(FadeOut(all_content))