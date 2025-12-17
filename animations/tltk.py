from manim import *
from manim_slides import Slide

class tltk(Slide):
    def construct(self):
        font_name = "Arial"
        
        # --- Kích thước ---
        title_scale = 0.9
        subtitle_scale = 0.7
        text_scale = 0.4
        
        # ==============================================================================
        # PHẦN 1: BÀI BÁO KHOA HỌC
        # ==============================================================================
        
        # --- SỬA LỖI: Dùng Text() cho tiếng Việt ---
        title_part1 = Text("TÀI LIỆU THAM KHẢO", font=font_name, weight=BOLD).scale(title_scale)
        subtitle_part1 = Text("1. Bài báo khoa học (Papers)", font=font_name).scale(subtitle_scale)
        
        # --- NỘI DUNG CÁC BÀI BÁO (Tiếng Anh dùng Tex được) ---
        # Lưu ý: tex_environment="flushleft" giúp căn trái trong khối LaTeX
        
        # Ref 1: Goodfellow
        ref1 = Tex(
            # Chú ý đoạn: ... Courville, A., \& Bengio, Y.
            r"\textbf{Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., \& Bengio, Y. (2014).}\\"
            r"\textit{Generative Adversarial Nets.}\\"
            r"Advances in Neural Information Processing Systems (NeurIPS). arXiv:1406.2661.",
            tex_environment="flushleft"
        ).scale(text_scale)

        # Ref 2: Kingma
        ref2 = Tex(
            r"\textbf{Kingma, D. P.,  Welling, M. (2019).}\\"
            r"\textit{An Introduction to Variational Autoencoders.}\\"
            r"Foundations and Trends® in Machine Learning."
            r"arXiv:1906.02691.",
            tex_environment="flushleft"
        ).scale(text_scale)

        # Ref 3: Ho
        ref3 = Tex(
            r"\textbf{Ho, J., Jain, A.,  Abbeel, P. (2020).}\\"
            r"\textit{Denoising Diffusion Probabilistic Models.}\\"
            r"Advances in Neural Information Processing Systems (NeurIPS). arXiv:2006.11239."
            r"arXiv:2006.11239.",
            tex_environment="flushleft"
        ).scale(text_scale)

        # Ref 4: He
        ref4 = Tex(
            r"\textbf{He, K., Zhang, X., Ren, S., \ Sun, J. (2015).}\\"
            r"\textit{Deep Residual Learning for Image Recognition.}\\"
            r"Proceedings of the IEEE Conference on CVPR."
            r"arXiv:1503.03585.",
            tex_environment="flushleft"
        ).scale(text_scale)

        # --- SẮP XẾP PHẦN 1 ---
        # Gom tất cả vào một nhóm để dễ quản lý vị trí và xóa đi
        title_part1.to_edge(UP) 

        # 2. Gom nhóm Nội dung (Subtitle + Refs) riêng biệt
        content_group = VGroup(
            subtitle_part1,
            ref1,
            ref2,
            ref3,
            ref4
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT) # Căn thẳng hàng trái với nhau
        
        # 3. Đặt nhóm Nội dung: Ở sát rìa trái màn hình
        content_group.to_edge(LEFT, buff=1.0) 

        # --- TRÌNH CHIẾU PHẦN 1 ---
        self.play(FadeIn(title_part1))
        self.play(FadeIn(subtitle_part1, shift=RIGHT))
        
        self.play(FadeIn(ref1))
        
        self.play(FadeIn(ref2))
        
        self.play(FadeIn(ref3))
        
        self.play(FadeIn(ref4))
        
        self.next_slide()

        # --- CHUYỂN CẢNH: QUAN TRỌNG ---
        self.play(
            FadeOut(title_part1),
            FadeOut(content_group)
        )


        # ==============================================================================
        # PHẦN 2: VIDEO & TÀI NGUYÊN
        # ==============================================================================
        
        # Tiêu đề phần 2 (Dùng Text cho tiếng Việt)
        title_part2 = Text("2. Video & tài nguyên trực tuyến", font=font_name, weight=BOLD).scale(subtitle_scale)
        
        # Tài liệu 1
        video1_line1 = Text("Stanford University (2025).", font=font_name)
        video1_line2 = Text("CS231N: Deep Learning for Computer Vision — Lecture 13: Generative Models 1.", font=font_name, slant=ITALIC)
        video1_line3 = Text("YouTube.", font=font_name)
        video1_group = VGroup(video1_line1, video1_line2, video1_line3).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Tài liệu 2
        video2_line1 = Text("Generative AI Animated.", font=font_name)
        video2_line2 = Text("Diffusion Models: DDPM.", font=font_name, slant=ITALIC)
        video2_line3 = Text("YouTube.", font=font_name)
        video2_group = VGroup(video2_line1, video2_line2, video2_line3).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        # Gom nhóm phần 2
        group_part2 = VGroup(
            title_part2,
            video1_group,
            video2_group
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        group_part2.scale(0.5) # Scale chung cho phần video
        group_part2.move_to(ORIGIN)
        
        # --- TRÌNH CHIẾU PHẦN 2 ---
        self.play(FadeIn(group_part2), run_time=2)
        self.next_slide()
        
        # Kết thúc
        self.play(FadeOut(group_part2))