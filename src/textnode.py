from enum import Enum

class Bender(Enum):
    AIR_BENDER = "air"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"
    WATER_BENDER = "water"

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    LINK = "link"
    CODE = "code"
    IMAGE = "image"
    TEXT = "text"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type.value == other.text_type.value and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
