from CardGallery import *

#east - west - south
class CardGalleryEWS(CardGallery):

    def __init__(self):
        super().__init__("EWS", False, True, True, True)