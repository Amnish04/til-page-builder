from builder.toc_generator.heading_item import HeadingItem


class TestHeadingItem:
    """
    Test suite for 'HeadingItem' class
    """

    class TestHeadingItemConstructor:
        """
        Tests for 'HeadingItem' class __init__ method
        """

        def test_default_arguments(self):
            """
            Test to verify the default values for HeadingItem constructor
            """
            heading = HeadingItem()

            assert heading.value == HeadingItem.DEFAULT_HEADING_VALUE
            assert heading.id == HeadingItem.generate_heading_id(
                HeadingItem.DEFAULT_HEADING_VALUE
            )
            assert heading.children == HeadingItem.DEFAULT_CHILDREN_VALUE

        def test_value_argument(self):
            """
            Test to verify the supplied value property is correctly set
            """
            sample_heading_value = "This is a sample heading"
            heading = HeadingItem(sample_heading_value)

            assert heading.value == sample_heading_value
            assert heading.id == HeadingItem.generate_heading_id(sample_heading_value)
            assert heading.children == HeadingItem.DEFAULT_CHILDREN_VALUE

        def test_value_and_children(self):
            """
            Test to verify the supplied value and children properties are correctly set
            """
            deep_nested_heading_1 = HeadingItem("1.1.1")
            deep_nested_heading_2 = HeadingItem("1.1.2")

            nested_heading_1 = HeadingItem(
                "1.1", [deep_nested_heading_1, deep_nested_heading_2]
            )
            nested_heading_2 = HeadingItem("1.2")

            top_heading = HeadingItem("1", [nested_heading_1, nested_heading_2])

            # Check for values
            assert top_heading.value == "1"
            assert nested_heading_1.value == "1.1"
            assert nested_heading_2.value == "1.2"

            # Check nested values
            assert top_heading.children[0].value == "1.1"
            assert top_heading.children[1].value == "1.2"

            # Check deep nested values
            assert top_heading.children[0].children[0].value == "1.1.1"
            assert top_heading.children[0].children[1].value == "1.1.2"

            # Check if children are correctly set
            assert nested_heading_1 in top_heading.children
            assert nested_heading_2 in top_heading.children

            # Check if deep nested children are correctly set
            assert deep_nested_heading_1 in top_heading.children[0].children
            assert deep_nested_heading_2 in top_heading.children[0].children

        def test_bad_values(self):
            """
            Check if default values are assigned when 'None' is passed as arguments
            """
            heading = HeadingItem(None, None)

            assert heading.value == HeadingItem.DEFAULT_HEADING_VALUE
            assert heading.id == HeadingItem.generate_heading_id(
                HeadingItem.DEFAULT_HEADING_VALUE
            )
            assert heading.children == HeadingItem.DEFAULT_CHILDREN_VALUE
