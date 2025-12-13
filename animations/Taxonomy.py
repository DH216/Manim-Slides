from manim import *
from manim_slides import Slide

class Taxonomy(Scene):
    def construct(self):
        # Title
        title = Text("Taxonomy of Generative Models", font_size=30, weight=BOLD)
        title.to_edge(UP, buff=0.3)
 
        self.play(Write(title))
        self.wait(0.5)
        
        # Root node
        root = self.create_box("Generative models", BLUE_B, scale=0.75)
        root.move_to(UP * 2)
        
        
        # Level 1 boxes
        explicit = self.create_box("Explicit density", BLUE_C, scale=0.75)
        implicit = self.create_box("Implicit density", BLUE_C, scale=0.75)
        
        explicit.move_to(LEFT * 3.5 + UP * 0.2)
        implicit.move_to(RIGHT * 3.5 + UP * 0.2)
        
        # Arrows from root
        mid_line_root = Line(root.get_bottom(),ORIGIN + UP*1.05)
        line1 = Line(mid_line_root.get_bottom(), explicit.get_top() + UP*0.5 + LEFT*0.02)
        line2 = Line(mid_line_root.get_bottom(), implicit.get_top() + UP*0.5 + RIGHT*0.02)
        arrow1 = Arrow(line1.get_left()+RIGHT*0.01, explicit.get_top(), buff=-0.5, stroke_width=3)
        arrow2 = Arrow(line2.get_right()+LEFT*0.01, implicit.get_top(), buff=-0.5, stroke_width=3)
        
        # Left and right labels
        left_label = Paragraph("Model can\ncompute P(x)", font_size=20, line_spacing=0.5,alignment="center")
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
                  run_time = 0.7
                  )
        self.play(
            GrowArrow(arrow1), GrowArrow(arrow2),
            Write(left_label),Write(right_label),
            FadeIn(explicit), FadeIn(implicit),
            run_time = 1
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
            run_time = 1
        )
        self.play(
            FadeIn(tractable), FadeIn(approximate),
            Write(autoregressive),
            Write(vae),
            run_time = 1
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
            run_time = 1
            
        )
        self.play(
            
            FadeIn(direct), FadeIn(indirect),
            Write(gan),
            Write(diffusion), 
            run_time = 1
        )

        self.next_slide()

        self.play(FadeOut(*self.mobjects))

        self.next_slide()
        # ==========================================

        
    def create_box(self, text, color, scale=1.0):
        """Create a rounded box with text inside"""
        label = Text(text, font_size=int(28 * scale))
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


# To render this animation, save this file and run:
# manim -pql filename.py GenerativeModelsTaxonomy
# 
# For higher quality:
# manim -pqh filename.py GenerativeModelsTaxonomy