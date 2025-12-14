from manim import *
from manim_slides import Slide

def T(text, size=28, color=WHITE):
    return Text(
        text,
        font_size=size,
        color=color
    )

class Intro(Slide):
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
        
        self.next_slide()
        # Tiêu đề nhóm
        title = Text(
            "Nhóm 17",
            font="Roboto",
            color=WHITE
        ).scale(1).to_edge(UP)
        self.add(title)

        # Chủ đề DDPM
        topic = Text(
            "Chủ đề: DDPM (Diffusion Probabilistic Models)",
            font="Roboto",
            color=YELLOW
        ).scale(0.6).next_to(title, DOWN, buff=0.7)
        self.add(topic)
       

        # Danh sách thành viên
        members = [
            "24520402 - Trần Nguyễn Hà Duy",
            "24520501 - Nguyễn Duy Hiếu",
            "24520504 - Nguyễn Minh Hiếu",
            "24520491 - Lê Đình Hiếu",
            "23520705 - Phạm Minh Bảo Khang"
        ]

        member_texts = VGroup(
            *[
                Text(m,font="Roboto", color=WHITE).scale(0.5)
                for m in members
            ]
        ).arrange(DOWN, aligned_edge=LEFT).next_to(topic, DOWN, buff=0.7)

       
        self.add(member_texts)
        self.wait()
        self.next_slide()
        

        group1 = VGroup(title, topic, member_texts)
        self.play(FadeOut(group1, shift=LEFT*7))
        self.next_slide()

        # Hình 1
        img1 = ImageMobject("./Imgs/tao_anh_bang_ai_1_0ff81bed08.jpg")
        img1.scale(0.7).to_edge(LEFT)
        img1.shift(UP * 1)
        self.play(FadeIn(img1))
        self.next_slide()

        # Hình 2
        img2 = ImageMobject("./Imgs/bombardiro-crocodilo-la-gi")
        img2.scale(1.0).move_to(ORIGIN)
        self.play(FadeIn(img2))
        self.next_slide()

        # Hình 3
        img3 = ImageMobject("./Imgs/40bb7ab560b14a079ce3ebf5aaef6cd2.jpg")
        img3.scale(0.7).to_edge(RIGHT)
        img3.shift(UP * 1)
        self.play(FadeIn(img3))
        self.next_slide()

        group2 = Group(img1, img2, img3)
        self.play(FadeOut(group2))
        self.next_slide()
        
        # =================Taxonomy=====================
        # Title
        title = Text("Taxonomy of Generative Models", font_size=30, weight=BOLD)
        title.to_edge(UP, buff=0.3)
 
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)
        
        # Root node
        root = self.create_box("Generative models", BLUE_B, scale=0.75,)
        root.move_to(UP * 2)
        
        
        # Level 1 boxes
        explicit = self.create_box("Explicit density", BLUE_C, scale=0.75, )
        implicit = self.create_box("Implicit density", BLUE_C, scale=0.75, )
        
        explicit.move_to(LEFT * 3.5 + UP * 0.2)
        implicit.move_to(RIGHT * 3.5 + UP * 0.2)
        
        # Arrows from root
        mid_line_root = Line(root.get_bottom(),ORIGIN + UP*1.05)
        line1 = Line(mid_line_root.get_bottom(), explicit.get_top() + UP*0.5 + LEFT*0.02)
        line2 = Line(mid_line_root.get_bottom(), implicit.get_top() + UP*0.5 + RIGHT*0.02)
        arrow1 = Arrow(line1.get_left()+RIGHT*0.01, explicit.get_top(), buff=-0.5, stroke_width=3)
        arrow2 = Arrow(line2.get_right()+LEFT*0.01, implicit.get_top(), buff=-0.5, stroke_width=3)
        
        # Left and right labels
        left_label = Paragraph("Model can\ncompute P(x)", font_size=20, line_spacing=0.5,alignment="center", )
        left_label.next_to(arrow1, UP, buff=0.5)
        
        right_label = Paragraph("Cannot compute p(x) but\ncan sample from P(x)", font_size=20, line_spacing=0.5,alignment="center")
        right_label.next_to(arrow2, UP, buff=0.5)
        
        self.next_slide()

        self.play(FadeIn(root))
        
        self.wait(0.5)

        self.next_slide()

        self.play(GrowFromPoint(mid_line_root,root.get_bottom()), run_time=0.5)
        self.play(GrowFromPoint(line1, mid_line_root.get_bottom()),
                  GrowFromPoint(line2,mid_line_root.get_bottom()),
                  run_time = 0.5
                  )
        self.play(
            GrowArrow(arrow1), GrowArrow(arrow2),
            Write(left_label),Write(right_label),
            FadeIn(explicit), FadeIn(implicit),
            run_time = 0.7
        )
        self.wait(0.5)
        
       
        # Level 2 boxes - Left side
        tractable = self.create_box("Tractable density", BLUE_D, scale=0.6)
        approximate = self.create_box("Approximate density", BLUE_D, scale=0.6)
        
        tractable.move_to(LEFT * 5 + DOWN * 1.8)
        approximate.move_to(LEFT * 2 + DOWN * 1.8)
        
        explicit_mid_line = Line(explicit.get_bottom(),explicit.get_bottom()+DOWN*0.85)
        line3 = Line(explicit_mid_line.get_bottom(), tractable.get_top()+ UP*0.5 )
        line4 = Line(explicit_mid_line.get_bottom(), approximate.get_top()+ UP*0.5)
        arrow3 = Arrow(line3.get_left()+RIGHT*0.01, tractable.get_top(), buff=-0.5, stroke_width=3)
        arrow4 = Arrow(line4.get_right()+LEFT*0.01, approximate.get_top(), buff=-0.5, stroke_width=3)
        
        # Level 2 boxes - Right side
        direct = self.create_box("Direct", BLUE_D, scale=0.6)
        indirect = self.create_box("Indirect", BLUE_D, scale=0.6)
        
        direct.move_to(RIGHT * 2 + DOWN * 1.8)
        indirect.move_to(RIGHT * 5 + DOWN * 1.8)
        
        implicit_mide_line = Line(implicit.get_bottom(), implicit.get_bottom()+DOWN*0.85)
        line5 = Line(implicit_mide_line.get_bottom(), direct.get_top()+UP*0.5)
        line6 = Line(implicit_mide_line.get_bottom(), indirect.get_top()+UP*0.5)
        arrow5 = Arrow(line5.get_left()+RIGHT*0.01, direct.get_top(), buff=-0.5, stroke_width=3)
        arrow6 = Arrow(line6.get_right()+LEFT*0.01, indirect.get_top(), buff=-0.5, stroke_width=3)
        
         # Left side labels
        left_side_label1 = Paragraph("Really\ncompute\nP(x)", font_size=20,line_spacing=0.5,alignment="center")
        left_side_label1.next_to(line3, LEFT, buff=0.1).shift(UP*0.5)
        
        left_side_label2 = Paragraph("Approximate\nP(x)", font_size=20,line_spacing=1,alignment="center")
        left_side_label2.next_to(line4, RIGHT, buff=0.1).shift(UP*0.5)
        
        # Right side labels
        right_side_label1 = Paragraph("Can directly\nsample\nfrom P(x)", font_size=20,alignment="center")
        right_side_label1.next_to(line5, LEFT, buff=0.2).shift(UP*0.5)

        right_side_label2 = Paragraph("Iterative\nprocedure to\napproximate\nsamples\nfrom P(x)", 
                                 font_size=20,alignment="center")
        right_side_label2.next_to(line6, RIGHT, buff=0.3).shift(UP*0.5)
        
        # Bottom level - Model names
        autoregressive = Text("Autoregressive", font_size=20)
        autoregressive.next_to(tractable, DOWN, buff=0.3)
        
        vae = Paragraph("Variational Autoencoder\n(VAE)", font_size=20,line_spacing=1,alignment="center")
        vae.next_to(approximate, DOWN, buff=0.3).align_to(vae.get_center())
        
        gan = Paragraph("Generative Adversarial\nNetwork (GAN)", font_size=20,line_spacing=1,alignment="center")
        gan.next_to(direct, DOWN, buff=0.3).align_to(gan.get_center())
        
        diffusion = Text("Diffusion Models", font_size=20)
        diffusion.next_to(indirect, DOWN, buff=0.3)
        self.wait(0.5)

        self.next_slide()

        self.play(GrowFromPoint(explicit_mid_line, explicit.get_bottom()), run_time=0.5)
        self.play(
            GrowFromPoint(line3,explicit_mid_line.get_bottom()),
            GrowFromPoint(line4,explicit_mid_line.get_bottom()),
            run_time = 0.5
        )
        self.play(
            GrowArrow(arrow3), GrowArrow(arrow4),
            Write(left_side_label1), 
            Write(left_side_label2),
            run_time = 0.7
        )
        self.play(
            FadeIn(tractable), FadeIn(approximate),
            Write(autoregressive),
            Write(vae),
            run_time = 0.5
        )

        self.next_slide()

        self.play(GrowFromPoint(implicit_mide_line, implicit.get_bottom()), run_time = 0.5)
        self.play(
            GrowFromPoint(line5,implicit_mide_line.get_bottom()),
            GrowFromPoint(line6, implicit_mide_line.get_bottom()),
            run_time = 0.5
        )
        self.play(
            GrowArrow(arrow5), GrowArrow(arrow6),
            Write(right_side_label1), 
            Write(right_side_label2),
            run_time = 0.7
            
        )
        self.play(
            
            FadeIn(direct), FadeIn(indirect),
            Write(gan),
            Write(diffusion), 
            run_time = 0.5
        )

        self.next_slide()

        self.play(FadeOut(*self.mobjects))

        self.next_slide()
        # ==========================================

        # ================= TITLE ==================
        title = Text("Generative Model Architectures Overview", font_size=35).to_edge(UP)
        self.play(FadeIn(title))
        self.next_slide()

        # ================= GAN =====================
        gan_title = T("GAN: Adversarial\ntraining", 20, color=WHITE).next_to(title, DOWN, buff=1).to_edge(LEFT).shift(RIGHT)
        gan = ImageMobject(r"./Imgs/image1").next_to(gan_title, RIGHT, buff=2)
        
        vae = ImageMobject(r"./Imgs/image2").next_to(gan, DOWN, buff=0)
        vae_title = T("VAE: Maximize\nvariational lower bound", 20, color=WHITE).next_to(vae, LEFT, buff=1.5)
        
        f = ImageMobject(r"./Imgs/image3").next_to(vae, DOWN, buff=0)
        f_title = T("Flow-based models:\ninvertible transform of\ndistributions", 20, color=WHITE).next_to(f, LEFT, buff=1.5)

        dm = ImageMobject(r"./Imgs/image4").next_to(f, DOWN, buff=0)
        dm_title = T("Diffusion models: gradually\n add Gaussiannoise\n and then reverse", 20, color=WHITE).next_to(dm, LEFT, buff=1.3)

        all_contents = Group(
            gan_title, gan,
            vae_title, vae,
            f_title, f,
            dm_title, dm, title
        )
        self.play(FadeIn(gan_title,gan))
        self.next_slide() 

        self.play(FadeIn(vae_title,vae))
        self.next_slide()

        self.play(FadeIn(f_title,f))
        self.next_slide()

        self.play(FadeIn(dm_title,dm))
        self.next_slide()

        self.play(FadeOut(all_contents))
    
        # --- CẤU HÌNH ---
        path_prefix = r"./Imgs"

        files = {
            "input":   f"{path_prefix}\\image5",
            "encoder": f"{path_prefix}\\image6",
            "latent":  f"{path_prefix}\\image7",
            "decoder": f"{path_prefix}\\image8",
            "output":  f"{path_prefix}\\image9",
            "loss":    f"{path_prefix}\\image10",
        }

        try:
            img_input   = ImageMobject(files["input"])
            img_encoder = ImageMobject(files["encoder"])
            img_latent  = ImageMobject(files["latent"])
            img_decoder = ImageMobject(files["decoder"])
            img_output  = ImageMobject(files["output"])
            img_loss    = ImageMobject(files["loss"])
        except FileNotFoundError:
            self.add(Text("Lỗi: Vui lòng cắt ảnh và đặt đúng tên file!", color=RED))
            return

        main_height = 2.5
        for img in [img_input, img_encoder, img_latent, img_decoder, img_output,]:
            img.scale_to_fit_height(main_height)

        main_group = Group(
            img_input,
            img_encoder,
            img_latent,
            img_decoder,
            img_output
        ).arrange(RIGHT, buff=0.2)

        all_objects = Group(main_group, img_loss).move_to(ORIGIN).scale(2).shift(RIGHT*1)

        title = Text("Variational Autoencoder (VAE)", font_size=40, color=BLUE).to_edge(UP)
        self.play(FadeIn(title))
        self.next_slide()

        img_encoder.next_to(img_input,RIGHT,buff=0)

        img_latent.next_to(img_encoder,RIGHT,buff=0)

        img_decoder.next_to(img_latent,RIGHT,buff=0)

        img_output.next_to(img_decoder,RIGHT,buff=0)
      
        img_loss.next_to(main_group, DOWN, buff=0).scale(0.63)
        
        self.play(LaggedStart(
                    FadeIn(img_input), FadeIn(img_encoder),
                    FadeIn(img_latent), FadeIn(img_decoder),
                    FadeIn(img_output), FadeIn(img_loss, shift=UP),
                    lag_ratio=0.2
                    ))
        self.play(FadeOut(all_objects), FadeOut(title))

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
        
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        # Giữ màn hình một chút 
        self.wait(1)