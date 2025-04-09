from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url, "alt":"alternate text"})
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case _:
            raise ValueError(f"Invalid TextType: {text_node.text_type}")

def main():
    text_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(text_node)

if __name__ == "__main__":
    main()