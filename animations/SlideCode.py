from manim import *
from manim_slides import Slide

class code(Slide):
    def construct(self):
        img1 = ImageMobject(r".\Imgs\LastScene\image1001.png")
        
        img2 = ImageMobject(r".\Imgs\LastScene\image1002.png")
        
        img3 = ImageMobject(r".\Imgs\LastScene\image1003.png")

        group_12 = Group(img1, img2).arrange(RIGHT, buff=0.5)
        
        group_12.scale_to_fit_width(13.0)
        if group_12.height > 6.5:
            group_12.scale_to_fit_height(6.5)
        
        group_12.move_to(ORIGIN)

        img3.scale_to_fit_height(6.5) 
        img3.move_to(ORIGIN)
        img1.align_to(LEFT)
        img2.next_to(img1,RIGHT, buff=1)
        img1.align_to(LEFT)
        self.play(FadeIn(group_12, shift=UP))
        self.next_slide()

        self.play(FadeOut(group_12))

        self.play(FadeIn(img3, shift=UP))
        self.next_slide()

        self.play(FadeOut(img3))