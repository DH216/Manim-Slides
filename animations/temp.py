from manim import *
from manim_slides import Slide

def T(text, size=28, color=WHITE):
    return Text(
        text,
        font_size=size,
        color=color
    )

class Temp(Slide):
    def create_box(self,text, color, scale=1.0):
        """Create a rounded box with text inside"""
        label = Tex(text, font_size=40*scale)
        box = Rectangle(
            width=label.width + 0.6,
            height=label.height + 0.4,
            fill_color=color,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=2
        )
        box.round_corners(radius=0.1)
        label.move_to(box.get_center())
        return VGroup(box, label)
    
    def construct(self):
        # ===================================================================
        # PHẦN 4: CHI TIẾT GAN (Đã bỏ mũi tên)
        # ===================================================================
        
        try:
            # Đường dẫn trực tiếp cho từng ảnh GAN
            g_sample = ImageMobject(r"./Imgs/image11")
            g_real   = ImageMobject(r"./Imgs/image12")
            g_latent = ImageMobject(r"./Imgs/image13")
            g_gen    = ImageMobject(r"./Imgs/image14")
            g_fake   = ImageMobject(r"./Imgs/image15")
            g_disc   = ImageMobject(r"./Imgs/image16")
            g_out    = ImageMobject(r"./Imgs/image17")
        except FileNotFoundError as e:
            self.add(Text(f"Lỗi thiếu file GAN:\n{str(e).split(':')[-1].strip()}", color=RED, font_size=20))
            self.wait(2)
            return

        # Sắp xếp bố cục GAN
        # Trình chiếu GAN
        g_out.move_to(ORIGIN).to_edge(RIGHT).shift(LEFT*1)
        g_disc.next_to(g_out,LEFT,buff=0)
        g_fake.next_to(g_disc,LEFT,buff=0).shift(DOWN*1)
        g_gen.next_to(g_fake,LEFT,buff=0)
        g_latent.next_to(g_gen,LEFT,buff=0)
        g_real.next_to(g_disc,LEFT,buff=0).shift(UP*1.5)
        g_sample.next_to(g_real,LEFT,buff=0)
        gan_main_title = T("Generative Adversarial Network (GAN)", 36, BLUE).to_edge(UP)
        self.play(FadeIn(gan_main_title))
        self.next_slide()
        
        high_main_title = T("High\nDimensional\nSample", 20, WHITE).next_to(g_sample,LEFT)
        self.play(LaggedStart(
                            FadeIn(high_main_title), 
                            FadeIn(g_sample), 
                            FadeIn(g_real),
                            lag_ratio=0.2
                            ))
        self.next_slide()

        Low_main_title = T("Low\nDimensional\nLatent", 20, WHITE).next_to(g_latent,LEFT)
        self.play(LaggedStart(
            FadeIn(Low_main_title),
            FadeIn(g_latent),
            FadeIn(g_gen),
            FadeIn(g_fake),
            lag_ratio=0.2
        ))
        self.next_slide()

        self.play(FadeIn(g_disc))
        self.next_slide()

        self.play(FadeIn(g_out))
        self.next_slide()

        self.play(FadeOut(Group( gan_main_title,high_main_title,Low_main_title,g_out,g_disc,g_fake,g_gen,g_latent,g_real,g_sample)))
        self.wait(0.5)
# --- CẤU HÌNH MÀU SẮC & STYLE ---
        # Lấy màu giống trong hình/video
        COLOR_FORWARD = "#FF5252"  # Màu đỏ cam
        COLOR_REVERSE = "#4FC3F7"  # Màu xanh dương sáng
        TEXT_COLOR = WHITE
        
        # --- 1. TIÊU ĐỀ ---
        title = Text("Diffusion Models", font_size=48, weight=BOLD).to_edge(UP)
        self.play(Write(title), run_time=0.5)
        
        # --- 2. CÁC NÚT (NODES) ---
        # Tạo hai vòng tròn đại diện cho x_{t-1} và x_t
        radius = 0.7
        distance = 3.5
        
        # Nút bên trái (x_{t-1})
        circle_left = Circle(radius=radius, color=WHITE, stroke_width=2)
        tex_left = MathTex("x_{t-1}", font_size=40)
        group_left = VGroup(circle_left, tex_left).move_to(LEFT * distance)
        
        # Nút bên phải (x_t)
        circle_right = Circle(radius=radius, color=WHITE, stroke_width=2)
        tex_right = MathTex("x_t", font_size=40)
        group_right = VGroup(circle_right, tex_right).move_to(RIGHT * distance)
        
        self.play(FadeIn(group_left), FadeIn(group_right))
        
        # --- 3. MŨI TÊN (ARROWS) ---
        
        # Mũi tên Thuận (Forward - Red) - Cong lên trên
        arrow_forward = CurvedArrow(
            start_point=circle_left.get_top(),
            end_point=circle_right.get_top(),
            angle=-TAU/4, # Độ cong
            color=COLOR_FORWARD,
            stroke_width=3
        )
        label_forward = MathTex("q(x_t | x_{t-1})", font_size=36, color=WHITE)
        label_forward.next_to(arrow_forward, UP, buff=0.1)
        
        # Mũi tên Ngược (Reverse - Blue) - Cong xuống dưới, nét đứt
        arrow_reverse_base = CurvedArrow(
            start_point=circle_right.get_bottom(),
            end_point=circle_left.get_bottom(),
            angle=-TAU/4,
            color=COLOR_REVERSE,
            stroke_width=3
        )
        # Tạo hiệu ứng nét đứt (Dashed Line)
        arrow_reverse = DashedVMobject(arrow_reverse_base, num_dashes=15)
        
        label_reverse = MathTex("p_{\\theta}(x_{t-1} | x_t)", font_size=36, color=WHITE)
        label_reverse.next_to(arrow_reverse, DOWN, buff=0.1)

        # Animation vẽ mũi tên
        self.play(Create(arrow_forward), Write(label_forward), run_time=0.5)
        self.play(Create(arrow_reverse), Write(label_reverse), run_time=0.5)

        # --- 4. PHÂN PHỐI GAUSSIAN (CENTER) ---
        # Tạo hệ trục ảo để vẽ đồ thị (ẩn trục đi)
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1, 1],
            x_length=4,
            y_length=2,
            axis_config={"include_tip": False, "stroke_opacity": 0} # Ẩn trục
        ).move_to(ORIGIN + DOWN * 0.2) # Dịch xuống một chút cho cân đối

        # Hàm Gaussian (Normal Distribution)
        def gaussian(x, mu, sigma):
            return np.exp(-((x - mu)**2) / (2 * sigma**2))

        # Đồ thị Đỏ (Forward) - Lệch trái một chút
        graph_red = axes.plot(lambda x: 0.8 * gaussian(x, -0.5, 0.6), color=COLOR_FORWARD)
        area_red = axes.get_area(graph_red, color=COLOR_FORWARD, opacity=0.5)
        
        # Đồ thị Xanh (Reverse) - Lệch phải một chút
        graph_blue = axes.plot(lambda x: 0.8 * gaussian(x, 0.5, 0.6), color=COLOR_REVERSE)
        area_blue = axes.get_area(graph_blue, color=COLOR_REVERSE, opacity=0.5)
        
        # Đường kẻ ngang phía dưới (trục hoành tượng trưng)
        baseline = Line(start=LEFT*2, end=RIGHT*2, color=GREY, stroke_width=1).move_to(axes.c2p(0, 0))

        # Nhóm đồ thị lại
        plots = VGroup(baseline, area_red, graph_red, area_blue, graph_blue)
        
        # Animation xuất hiện đồ thị từ dưới lên
        self.play(FadeIn(plots, shift=UP * 0.5))
        
        # Giữ màn hình một chút 
        self.wait(3)