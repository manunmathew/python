
# HTML `div` Element

The `<div>` element is a versatile HTML element used as a container for other HTML elements. It is commonly used to group together blocks of content or to structure the layout of a webpage.

## `display: flex`

To make your `<div>` container flexible, you can use the `display: flex` property. This allows the elements inside the container to align and distribute space based on flexbox layout rules.

**CSS Example:**

    div {
      display: flex;
    }

### `justify-content` Property

The `justify-content` property is used to align the flex items inside a container along the main axis. It can be used with various values to achieve different alignments:

- **flex-start**: Default value. Items are positioned at the beginning of the container.
- **flex-end**: Items are positioned at the end of the container.
- **center**: Items are positioned in the center of the container.
- **space-between**: Items have space between them.
- **space-around**: Items have space before, between, and after them.
- **space-evenly**: Items have equal space around them.
- **initial**: Sets the property to its default value.
- **inherit**: Inherits the property from its parent element.

**CSS Example:**

    div {
      display: flex;
      justify-content: space-between;
    }

This example will align the items inside the `div` with equal space between them.

## `border-radius` Property

The `border-radius` property defines the radius of the corners of an element, allowing you to add rounded corners.

**CSS Example:**

    div {
      border-radius: 10px;
    }

### Tip:

This property is useful for creating buttons, cards, and other elements with smooth, rounded corners.

## `overflow` Property

The `overflow` property controls what happens to content that overflows the bounds of an element's box. It can have the following values:

- **visible**: The overflow is not clipped. It renders outside the element's box (default).
- **hidden**: The overflow is clipped, and the rest of the content is invisible. Content can still be scrolled programmatically (e.g., using `scrollLeft` or `scrollTo()`).
- **clip**: The overflow is clipped, and the rest of the content is invisible. It also prevents any form of scrolling.
- **scroll**: The overflow is clipped, but a scroll bar is added to see the rest of the content.
- **auto**: Adds a scroll bar if the content overflows.
- **initial**: Sets the property to its default value.
- **inherit**: Inherits the property from its parent element.

**CSS Example:**

    div {
      overflow: hidden;
    }

This example will clip the content inside the `div` and hide any overflow.

## Including Font Awesome

To include Font Awesome icons in your project, add the following script tag:

**HTML Example:**

    <script src="https://kit.fontawesome.com/4477b93826.js" crossorigin="anonymous"></script>


