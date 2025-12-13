from manim import *
from manim_slides import Slide
from manim_voiceover import VoiceoverScene

import numpy as np
import sys

sys.path.append("../")


class Scene2_6(MovingCameraScene, Slide):
    def construct(self):

        tex_to_color_map = {
            r"\theta": BLUE,
        }

        # Explain what the q distributions are
        self.next_section(skip_animations=False)

        elbo_simplified = MathTex(
            r"- \mathbb{E}_q \left[",
            r"\sum_{t > 1} D_{\mathrm{KL}}(",
            r"q(x_{t-1} \mid x_t, x_0)",
            r"\mid \mid ",
            r"p_{\theta}(x_{t-1} \mid x_t)",
            r")",
            r"\right]",
            color=WHITE,
            font_size=28,
            tex_to_color_map=tex_to_color_map,
        ).to_edge(UP, buff=0.5)

        self.add(elbo_simplified)

        xt_circle = Circle(radius=0.5, color=WHITE).move_to(RIGHT * 2)
        xt1_circle = Circle(radius=0.5, color=WHITE).move_to(LEFT * 2)
        x0_circle = Circle(radius=0.5, color=WHITE).next_to(xt_circle, DOWN, buff=1.5)
        x0xt_line = DashedLine(
            start=xt_circle.get_bottom(),
            end=x0_circle.get_top(),
            color=WHITE,
        )
        xt_image = (
            ImageMobject("Imgs/Scene2/ffhq_1_noise_61.png")
            .scale_to_fit_width(1.5)
            .next_to(xt_circle, RIGHT, buff=0.75)
        )
        xt_image_rect = SurroundingRectangle(
            xt_image,
            color=WHITE,
            buff=0.0,
        )
        xt_img_line = DashedLine(
            start=xt_circle.get_right(),
            end=xt_image.get_left(),
            color=WHITE,
            buff=0.0,
        )
        xt1_image = (
            ImageMobject("Imgs/Scene2/ffhq_1_noise_30.png")
            .scale_to_fit_width(1.5)
            .next_to(xt1_circle, LEFT, buff=0.75)
        )
        xt1_image_rect = SurroundingRectangle(
            xt1_image,
            color=WHITE,
            buff=0.0,
        )
        xt1_img_line = DashedLine(
            start=xt1_circle.get_left(),
            end=xt1_image.get_right(),
            color=WHITE,
            buff=0.0,
        )
        x0_image = (
            ImageMobject("Imgs/Scene2/ffhq_1.png")
            .scale_to_fit_width(1.5)
            .next_to(x0_circle, RIGHT, buff=0.75)
        )
        x0_image_rect = SurroundingRectangle(
            x0_image,
            color=WHITE,
            buff=0.0,
        )
        x0_img_line = DashedLine(
            start=x0_circle.get_right(),
            end=x0_image.get_left(),
            color=WHITE,
            buff=0.0,
        )

        xt_label = MathTex(
            r"x_t",
            color=WHITE,
            font_size=32,
        ).move_to(xt_circle)

        xt1_label = MathTex(
            r"x_{t-1}",
            color=WHITE,
            font_size=32,
        ).move_to(xt1_circle)
        x0_label = MathTex(
            r"x_0",
            color=WHITE,
            font_size=32,
        ).move_to(x0_circle)

        q_arrow = CurvedArrow(
            start_point=xt1_circle.get_top() + UP * 0.05,
            end_point=xt_circle.get_top() + UP * 0.05,
            color=WHITE,
            angle=-PI / 2,
        )
        q_label = MathTex(
            r"q(x_t \mid x_{t-1})",
            tex_to_color_map=tex_to_color_map,
            color=WHITE,
            font_size=32,
        ).next_to(q_arrow, UP, buff=0.1)
        p_arrow = DashedVMobject(
            CurvedArrow(
                start_point=xt_circle.get_bottom() + DOWN * 0.05,
                end_point=xt1_circle.get_bottom() + DOWN * 0.05,
                color=BLUE,
                angle=-PI / 2,
            )
        )
        p_label = MathTex(
            r"p_{\theta}(x_{t-1} \mid x_t)",
            color=WHITE,
            font_size=32,
            tex_to_color_map=tex_to_color_map,
        ).next_to(p_arrow, DOWN, buff=0.1)
        q_posterior_arrow = CurvedArrow(
            start_point=x0xt_line.get_center() + LEFT * 0.05,
            end_point=xt1_circle.get_bottom() + DOWN * 0.5,
            color=WHITE,
            angle=-2 * PI / 3,
        )
        q_posterior_label = MathTex(
            r"q(x_{t-1} \mid x_t, x_0)",
            color=WHITE,
            font_size=32,
            tex_to_color_map=tex_to_color_map,
        ).next_to(q_posterior_arrow, DOWN, buff=0.1)

        self.next_slide()
        self.play(
            FadeIn(xt1_circle, xt1_image, xt1_image_rect, xt1_label, xt1_img_line)
        )
        self.play(
            LaggedStart(Create(q_arrow), Write(q_label), lag_ratio=0.5),
            run_time=1.5,
        )
        self.play(FadeIn(xt_circle, xt_image, xt_image_rect, xt_label, xt_img_line))

        self.play(
            LaggedStart(Create(p_arrow), Write(p_label), lag_ratio=0.5),
            run_time=1.5,
        )

        self.play(
            LaggedStart(
                Create(x0xt_line),
                FadeIn(x0_circle, x0_image, x0_image_rect, x0_label, x0_img_line),
                lag_ratio=0.7,
            ),
            run_time=1,
        )

        self.play(
            LaggedStart(Create(q_posterior_arrow), Write(q_posterior_label)),
            run_time=1.5,
        )

        self.next_slide()
        
        self.play(Indicate(VGroup(x0_circle, x0_label), color=WHITE))
        self.play(Indicate(VGroup(x0_circle, x0_label), color=WHITE))

        ax = (
            Axes(
                x_range=[-4, 4],
                y_range=[0, 1],
                axis_config={"include_tip": False, "stroke_width": 1},
                z_index=2,
            )
            .scale(0.3)
            .next_to(q_label, UP, buff=0.4)
        )

        def gaussian(x, mu, sigma):
            return np.exp(-((x - mu) ** 2) / (2 * sigma**2)) / (
                sigma * np.sqrt(2 * np.pi)
            )

        def mixture_gaussian(x, mus, sigmas, weights):
            return sum(
                w * gaussian(x, mu, sigma) for mu, sigma, w in zip(mus, sigmas, weights)
            )

        x = np.linspace(-4, 4, 100)

        # First mixture: two components
        p_plot = ax.plot(
            lambda x: mixture_gaussian(x, [-1.8, -0.3], [0.6, 0.3], [0.7, 0.3]),
            color=BLUE,
            fill_opacity=0.5,
            stroke_width=1,
        )

        # Second mixture: two components
        q_plot = ax.plot(
            lambda x: mixture_gaussian(x, [0.7, 2.1], [0.7, 0.3], [0.4, 0.6]),
            color=RED,
            fill_opacity=0.5,
            stroke_width=1,
        )
        p_plot_label = ax.get_graph_label(
            p_plot,
            label=MathTex(
                r"p_{\theta}(x_{t-1} \mid x_t)",
                tex_to_color_map=tex_to_color_map,
                font_size=10,
            ),
            x_val=-2,
            direction=UP,
            buff=0.5,
            color=WHITE,
        ).shift(0.6 * UP + 0.8 * LEFT)
        q_plot_label = ax.get_graph_label(
            q_plot,
            label=MathTex(
                r"q(x_{t-1} \mid x_t, x_0)",
                tex_to_color_map=tex_to_color_map,
                font_size=10,
            ),
            x_val=2,
            direction=UP,
            buff=2,
            color=WHITE,
        ).shift(0.6 * UP + 0.2 * RIGHT)

        self.next_slide()
        # ========================= NV 3 ============================
        self.play(FadeOut(*self.mobjects)) 
        # --- Cấu hình font chữ ---
        # Lưu ý: Không đặt font_size cố định ở đây nữa để dùng scale sau
        font_name = "Arial" 

        # ==============================================================================
        # 1. CÔNG THỨC ĐẦU TIÊN (Xuất hiện trước nhất)
        # ==============================================================================
        equation = MathTex(
            r"q(x_{t-1} | x_t, x_0) = \frac{1}{\sqrt{2\pi\beta}} \exp \left( -\frac{1}{2\beta}{x_{t-1}}^2 + \frac{\mu}{\beta}x_{t-1} - \frac{1}{2\beta}\mu^2 \right)"
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
            r"q(x_{t-1} | x_0) = \frac{1}{(2\pi(1 - \bar{\alpha}_{t-1}))^{d/2}} \exp \left[ -\frac{1}{2(1 - \bar{\alpha}_{t-1})} \|x_{t-1} - \sqrt{\bar{\alpha}_{t-1}}x_0\|^2 \right]"
        )
        eq_detailed_2 = MathTex(
            r"q(x_t | x_{t-1}) = \frac{1}{(2\pi\beta_t)^{d/2}} \exp \left[ -\frac{1}{2\beta_t} \|x_t - \sqrt{\alpha_t}x_{t-1}\|^2 \right]"
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

        self.next_slide()

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
        self.next_slide()

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
       
        # =============== Set up lại ============
        self.play(
            FadeIn(xt1_circle, xt1_image, 
                   xt1_image_rect, xt1_label, xt1_img_line,q_arrow,q_label,
                   xt_circle, xt_image, xt_image_rect, xt_label, xt_img_line,
                   p_arrow,p_label,x0xt_line,x0_circle, x0_image, x0_image_rect, x0_label, x0_img_line,
                   q_posterior_arrow,q_posterior_label
                   )
        )
        
        # ===============================================================
        # Start the axes small and zoomed out

        self.next_slide()
        self.play(
            LaggedStart(
                FadeIn(ax, p_plot, q_plot),
                self.camera.frame.animate.scale(0.3).move_to(ax),  # Zoom in
                lag_ratio=0.8,
            ),
            run_time=4,
        )

        self.next_slide()
        
        self.play(Write(p_plot_label))
        self.play(Write(q_plot_label))

        # What shape we choose for the p distributions
        self.next_section(skip_animations=False)

        q_expression = MathTex(
            r"q(x_{t-1} \mid x_t, x_0)",
            r"= \mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_t)",
            color=WHITE,
            font_size=10,
        ).move_to(q_plot_label, aligned_edge=LEFT)

        self.next_slide()
        self.play(Write(q_expression[1]))

        q_gaussian = ax.plot(
            lambda x: gaussian(x, 0.7, 0.5),
            color=RED,
            fill_opacity=0.5,
            stroke_width=1,
        )

        self.next_slide()
        self.play(Transform(q_plot, q_gaussian))

        p_gaussian = ax.plot(
            lambda x: gaussian(x, -1.8, 0.6),
            color=BLUE,
            fill_opacity=0.5,
            stroke_width=1,
        )

        p_expression = MathTex(
            r"p_\theta (x_{t-1} \mid x_t)",
            r"= \mathcal{N}(\mu_\theta, \sigma_\theta)",
            color=WHITE,
            font_size=10,
            tex_to_color_map=tex_to_color_map,
        ).move_to(p_plot_label, aligned_edge=LEFT)

        self.next_slide()

        self.play(
            LaggedStart(
                Transform(p_plot, p_gaussian),
                Write(p_expression[3:]),
                lag_ratio=0.8,
            )
        )

        p_line = DashedLine(
            start=ax.c2p(-1.8, gaussian(-1.8, -1.8, 0.6)),
            end=ax.c2p(-1.8, 0),
            color=BLUE,
            stroke_width=1,
        )
        p_line_label = MathTex(
            r"\mu_\theta",
            color=WHITE,
            font_size=10,
            tex_to_color_map=tex_to_color_map,
        ).next_to(p_line, DOWN, buff=0.1)
        p_line_label.add_updater(lambda m: m.next_to(p_line, DOWN, buff=0.1))

        q_line = DashedLine(
            start=ax.c2p(0.7, gaussian(0.7, 0.7, 0.5)),
            end=ax.c2p(0.7, 0),
            color=RED,
            stroke_width=1,
        )
        q_line_label = MathTex(
            r"\tilde{\mu}_t",
            color=WHITE,
            font_size=10,
            tex_to_color_map=tex_to_color_map,
        ).next_to(q_line, DOWN, buff=0.1)

        self.next_slide()
        self.play(
            LaggedStart(Create(p_line), Write(p_line_label), lag_ratio=0.9),
            run_time=1.5,
        )

        # Create double-ended arrows to show the spread (standard deviation)
        p_spread = DoubleArrow(
            ax.c2p(-2.4, gaussian(-2.4, -1.8, 0.6)),
            ax.c2p(-1.2, gaussian(-1.2, -1.8, 0.6)),
            color=BLUE,
            buff=0,
            stroke_width=1,
            tip_length=0.05,
            max_tip_length_to_length_ratio=0.2,
        )
        p_spread_label = MathTex(
            r"\sigma_\theta",
            color=WHITE,
            font_size=10,
        ).next_to(p_spread, UP, buff=0.1)
        p_spread_label.add_updater(lambda m: m.next_to(p_spread, UP, buff=0.1))

        self.next_slide()
        self.play(
            LaggedStart(Create(p_spread), Write(p_spread_label), lag_ratio=0.9),
            run_time=1.5,
        )

        p_expression_2 = MathTex(
            r"p_\theta (x_{t-1} \mid x_t)",
            r"= \mathcal{N}(\mu_\theta, \sigma_t)",
            color=WHITE,
            font_size=10,
            tex_to_color_map=tex_to_color_map,
        ).move_to(p_plot_label, aligned_edge=LEFT)

        p_spread_label_2 = MathTex(
            r"\sigma_t",
            color=WHITE,
            font_size=10,
            tex_to_color_map=tex_to_color_map,
        ).next_to(p_spread, UP, buff=0.1)

        self.next_slide()
        self.play(
            LaggedStart(
                Transform(p_expression[3:], p_expression_2[3:]),
                Transform(p_spread_label, p_spread_label_2),
                lag_ratio=0.5,
            ),
            run_time=2,
        )

        self.play(Circumscribe(p_line_label, color=WHITE, stroke_width=1))

        self.play(
            LaggedStart(Create(q_line), Write(q_line_label), lag_ratio=0.9),
            run_time=1.5,
        )

        new_p_gaussian = ax.plot(
            lambda x: gaussian(x, -0.4, 0.45),
            color=BLUE,
            fill_opacity=0.5,
            stroke_width=1,
        )

        self.next_slide()

        self.play(
            FadeOut(p_spread, p_spread_label),
            Transform(p_plot, new_p_gaussian),
            p_line.animate.put_start_and_end_on(
                start=ax.c2p(-0.4, gaussian(-0.4, -0.4, 0.45)),
                end=ax.c2p(-0.4, 0),
            ),
            run_time=2,
        )

        kl_expression = MathTex(
            r"D_{\mathrm{KL}}(q(x_{t-1} \mid x_t, x_0) \mid \mid p_\theta (x_{t-1} \mid x_t)) = \frac{1}{2 \sigma_t^2}} \| \tilde{\mu}_t - \mu_\theta \|^2",
            color=WHITE,
            font_size=10,
            tex_to_color_map=tex_to_color_map,
        ).next_to(p_expression, UP, buff=0.05, aligned_edge=LEFT)

        self.next_slide()
        self.play(Write(kl_expression))

        # Show that we try to match all distributions at the same time
        self.next_section(skip_animations=False)

        self.remove(
            x0_image,
            x0_circle,
            x0_image_rect,
            x0_label,
            x0_img_line,
            xt1_image,
            xt1_image_rect,
            xt1_img_line,
            xt_image,
            xt_image_rect,
            xt_img_line,
            q_posterior_arrow,
            q_posterior_label,
            x0xt_line,
        )

        xt2_circle = Circle(radius=0.5, color=WHITE).next_to(xt1_circle, LEFT, buff=3)
        xt2_label = MathTex(
            r"x_{t-2}",
            color=WHITE,
            font_size=32,
        ).move_to(xt2_circle)

        xt11_circle = Circle(radius=0.5, color=WHITE).next_to(xt_circle, RIGHT, buff=3)
        xt11_label = MathTex(
            r"x_{t+1}",
            color=WHITE,
            font_size=32,
        ).move_to(xt11_circle)

        q_arrow_t2 = CurvedArrow(
            start_point=xt2_circle.get_top() + UP * 0.05,
            end_point=xt1_circle.get_top() + UP * 0.05,
            color=WHITE,
            angle=-PI / 2,
        )

        q_label_t2 = MathTex(
            r"q(x_{t-1} \mid x_{t-2})",
            tex_to_color_map=tex_to_color_map,
            color=WHITE,
            font_size=32,
        ).next_to(q_arrow_t2, UP, buff=0.1)

        q_arrow_t1 = CurvedArrow(
            start_point=xt_circle.get_top() + UP * 0.05,
            end_point=xt11_circle.get_top() + UP * 0.05,
            color=WHITE,
            angle=-PI / 2,
        )
        q_label_t1 = MathTex(
            r"q(x_{t-1} \mid x_{t+1})",
            tex_to_color_map=tex_to_color_map,
            color=WHITE,
            font_size=32,
        ).next_to(q_arrow_t1, UP, buff=0.1)

        p_arrow_t2 = DashedVMobject(
            CurvedArrow(
                start_point=xt1_circle.get_bottom() + DOWN * 0.05,
                end_point=xt2_circle.get_bottom() + DOWN * 0.05,
                color=BLUE,
                angle=-PI / 2,
            )
        )
        p_label_t2 = MathTex(
            r"p_{\theta}(x_{t-2} \mid x_{t-1})",
            color=WHITE,
            font_size=32,
            tex_to_color_map=tex_to_color_map,
        ).next_to(p_arrow_t2, DOWN, buff=0.1)
        p_arrow_t1 = DashedVMobject(
            CurvedArrow(
                start_point=xt11_circle.get_bottom() + DOWN * 0.05,
                end_point=xt_circle.get_bottom() + DOWN * 0.05,
                color=BLUE,
                angle=-PI / 2,
            )
        )
        p_label_t1 = MathTex(
            r"p_{\theta}(x_{t} \mid x_{t+1})",
            color=WHITE,
            font_size=32,
            tex_to_color_map=tex_to_color_map,
        ).next_to(p_arrow_t1, DOWN, buff=0.1)

        ax2 = (
            Axes(
                x_range=[-4, 4],
                y_range=[0, 1],
                axis_config={"include_tip": False, "stroke_width": 1},
                z_index=2,
            )
            .scale(0.3)
            .next_to(q_label_t1, UP, buff=0.4)
        )

        p2_plot = ax2.plot(
            lambda x: gaussian(x, 1.2, 0.7),
            color=BLUE,
            fill_opacity=0.5,
            stroke_width=1,
        )
        q2_plot = ax2.plot(
            lambda x: gaussian(x, -0.2, 0.5),
            color=RED,
            fill_opacity=0.5,
            stroke_width=1,
        )

        ax3 = (
            Axes(
                x_range=[-4, 4],
                y_range=[0, 1],
                axis_config={"include_tip": False, "stroke_width": 1},
                z_index=2,
            )
            .scale(0.3)
            .next_to(q_label_t2, UP, buff=0.4)
        )
        p3_plot = ax3.plot(
            lambda x: gaussian(x, -0.4, 0.55),
            color=BLUE,
            fill_opacity=0.5,
            stroke_width=1,
        )
        q3_plot = ax3.plot(
            lambda x: gaussian(x, 1.2, 0.6),
            color=RED,
            fill_opacity=0.5,
            stroke_width=1,
        )

        self.add(
            xt2_circle,
            xt11_circle,
            xt2_label,
            xt11_label,
            q_arrow_t2,
            q_label_t2,
            q_arrow_t1,
            q_label_t1,
            p_arrow_t2,
            p_label_t2,
            p_arrow_t1,
            p_label_t1,
            ax2,
            p2_plot,
            q2_plot,
            ax3,
            p3_plot,
            q3_plot,
        )
        # =================== NV 4 ======================================

        self.next_slide()
        origin_pos = self.camera.frame.copy()
        self.play(self.camera.frame.animate.scale(1 / 0.3).shift(UP*7))
        # ===============================================================

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
        all_content.move_to(ORIGIN+UP*9)

        # ==============================================================================
        # TRÌNH CHIẾU
        # ==============================================================================

        # Slide 1: Hiện công thức tổng quát
        self.next_slide()

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
        self.play(self.camera.frame.animate.scale(0.3).become(origin_pos))
        # ===============================================================



        # Reset camera position
        self.next_slide()

        self.play(
            self.camera.frame.animate.scale(1 / 0.3).move_to(ORIGIN),
            FadeOut(
                kl_expression,
                p_expression[3:],
                p_plot_label,
                q_plot_label,
                p_line_label,
                q_line_label,
                q_line,
                p_line,
                q_expression,
            ),
            run_time=2.5,
        )

        # Animate 3 times, each time bringing p closer to q
        self.next_slide()
        for i in range(3):
            # For each iteration, move p means closer to q means using weighted average
            weight = (i + 1) / 3
            p3_mean = -0.4 * (1 - weight) + 1.2 * weight  # Move from -0.4 to 1.2
            p2_mean = 1.2 * (1 - weight) + (-0.2) * weight  # Move from 1.2 to -0.2
            p_mean = -0.4 * (1 - weight) + 0.7 * weight  # Move from -0.4 to 0.7

            p3_plot_new = ax3.plot(
                lambda x: gaussian(x, p3_mean, 0.55),
                color=BLUE,
                fill_opacity=0.5,
                stroke_width=1,
            )
            p2_plot_new = ax2.plot(
                lambda x: gaussian(x, p2_mean, 0.7),
                color=BLUE,
                fill_opacity=0.5,
                stroke_width=1,
            )
            p_plot_new = ax.plot(
                lambda x: gaussian(x, p_mean, 0.6),
                color=BLUE,
                fill_opacity=0.5,
                stroke_width=1,
            )

            self.play(
                LaggedStart(
                    Transform(p3_plot, p3_plot_new),
                    Transform(p2_plot, p2_plot_new),
                    Transform(p_plot, p_plot_new),
                    lag_ratio=0.1,
                    run_time=2,
                )
            )

        self.next_slide()
        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene2_6()
    scene.render()
