from CardGallery import *

#possible end point
class CardGalleryEnd(CardGallery):
    
    def __init__(self,isGoal):
        self.isGoal = isGoal
        super().__init__("End", True, True, True, True)