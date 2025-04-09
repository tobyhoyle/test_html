import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode1 = HTMLNode("h1", "Test Case", None, None)
        htmlnode2 = HTMLNode("h1", "Test Case", None, None)
        self.assertEqual(htmlnode1, htmlnode2)

    def test_not_eq_tag(self):
        htmlnode1 = HTMLNode("h1", "Test Case", None, None)
        htmlnode2 = HTMLNode("p", "Test Case", None, None)
        self.assertNotEqual(htmlnode1, htmlnode2)

    def test_not_eq_value(self):
        htmlnode1 = HTMLNode("h1", "Test Case", None, None)
        htmlnode2 = HTMLNode("h1", "Test Case #2", None, None)
        self.assertNotEqual(htmlnode1, htmlnode2)

    def test_props_to_html(self):
        # Create an HTMLNode with some props
        node = HTMLNode(
            tag="a", 
            value="Click me", 
            children=None, 
            props={"href": "https://example.com", "target": "_blank"}
        )
        
        # Check if props_to_html returns the expected string
        expected = " href=\"https://example.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), expected)

    def test_single_prop_to_html(self):
        node = HTMLNode(
            tag="a", 
            value="Click me", 
            children=None, 
            props={"href": "https://example.com"}
        )

        expected = " href=\"https://example.com\""
        self.assertEqual(node.props_to_html(), expected)
    
    def test_no_prop_to_html(self):
        node = HTMLNode(
            tag="a", 
            value="Click me", 
            children=None, 
            props=None
        )

        expected = ""
        self.assertEqual(node.props_to_html(), expected)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

        
