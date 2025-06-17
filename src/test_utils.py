import unittest

from utils import extract_markdown_images, extract_markdown_links


class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [to imgur](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("to imgur", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and this is also ![image2](https://test.com)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://test.com"),
            ],
            matches,
        )

    def test_extract_markdown_links_2(self):
        matches = extract_markdown_links(
            "This is text with an [hey ho](https://i.imgur.com/zjjcJKZ.png) and this is also [ooo la la](https://test.com)"
        )
        self.assertListEqual(
            [
                ("hey ho", "https://i.imgur.com/zjjcJKZ.png"),
                ("ooo la la", "https://test.com"),
            ],
            matches,
        )

    def test_extract_markdown_image_only(self):
        matches = extract_markdown_images(
            "This is text with an [hey ho](https://i.imgur.com/zjjcJKZ.png) and this is also ![ooo la la](https://test.com)"
        )
        self.assertListEqual(
            [
                ("ooo la la", "https://test.com"),
            ],
            matches,
        )

    def test_extract_markdown_link_only(self):
        matches = extract_markdown_links(
            "This is text with an ![hey ho](https://i.imgur.com/zjjcJKZ.png) and this is also [ooo la la](https://test.com)"
        )
        self.assertListEqual(
            [
                ("ooo la la", "https://test.com"),
            ],
            matches,
        )

    def test_no_match_images(self):
        matches = extract_markdown_images(
            "This is text with an image  and this is also a link "
        )
        self.assertListEqual([], matches)

    def test_no_match_links(self):
        matches = extract_markdown_links(
            "This is text with an image  and this is also a link "
        )
        self.assertListEqual([], matches)
