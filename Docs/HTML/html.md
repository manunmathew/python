# HTML Overview

## What is HTML?

HTML (HyperText Markup Language) is a **markup language** that provides a set of tags suitable for creating web pages. It is a scripting language, and the output of HTML documents can be viewed in a web browser. Some key characteristics of HTML include:

- **Tag-based system**: HTML uses tags to define elements within a document.
- **No errors generated**: Web browsers won't generate errors for incorrect HTML, although they may not display content as intended.

## What is Hypertext?

Hypertext is text that contains links (called hyperlinks) to other documents or pages, allowing users to navigate between content by clicking these links.

## What is Markup?

Markup refers to the use of tags to define the structure and presentation of content within a document. In HTML, markup is used to annotate text, images, and other elements so that they are structured correctly and rendered by the browser.

## Structure of HTML Documents

### 1. Head Section
The **head section** contains metadata and control information used by the browser, as well as the title of the document. This section includes elements such as:

- `<title>`: Specifies the title of the page (shown in the browser tab).
- `<meta>`: Provides metadata about the document (e.g., charset, author, description).

### 2. Body Section
The **body section** contains the main content that is displayed on the screen. This is where tags such as headings, paragraphs, images, and links are used to create the visible structure of the web page.

Example of a simple HTML structure:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a paragraph of content displayed on the page.</p>
</body>
</html>
```
## Common HTML Tags

### Headings

HTML defines six levels of headings, ranging from `<h1>` (most important) to `<h6>` (least important).

- `<h1>`: The highest priority heading, typically used for main titles.
- `<h6>`: The lowest priority heading, often used for subheadings or smaller content.

Example:

```html
<h1>Main Title</h1>
<h2>Subheading</h2>
```

### Text Formatting Tags

- `<u>`: Underlines the enclosed text.
- `<b>`: Bolds the text.
- `<strong>`: Indicates important text, often rendered in bold.
- `<i>`: Italicizes the text.
- `<em>`: Emphasizes the text, usually italicized.
- `<mark>`: Highlights text.
- `<small>`: Displays smaller text.
- `<del>`: Strikes through (deleted) text.
- `<ins>`: Underlines inserted text.
- `<sub>`: Displays subscript text (e.g., H<sub>2</sub>O).
- `<sup>`: Displays superscript text (e.g., 10<sup>2</sup>).

### Paragraphs

The `<p>` tag defines paragraphs of text. Browsers automatically add space above and below paragraphs.

Example:

```html
<p>This is a paragraph of text.</p>
```

### Links (Anchor Tags)

The `<a>` (anchor) tag is used to create hyperlinks. It uses the `href` attribute to specify the destination URL.

Example:

```html
<a href="https://www.example.com">Visit Example</a>
```

### Horizontal Line

The `<hr>` tag creates a horizontal line, often used to separate content. It is an empty tag, meaning it doesn’t require a closing tag.

Example:

```html
<hr>
```

### HTML Attributes

HTML elements can have **attributes** that modify their behavior or provide additional information. For example, the `align` attribute can adjust text alignment:

- `align="left"`: Aligns the content to the left.
- `align="right"`: Aligns the content to the right.
- `align="center"`: Centers the content.
- `align="justify"`: Stretches the content so that it aligns evenly on both sides.

Example:

```html
<p align="center">This paragraph is centered.</p>
```

### Font Tag (Deprecated)

The `<font>` tag (now deprecated in HTML5) was once used to specify font size and color. Modern HTML encourages using CSS for this.

Example (Deprecated):

```html
<font size="4" color="blue">This is a blue font.</font>
```

Instead, use CSS:

```html
<p style="font-size: 16px; color: blue;">This is a blue font with CSS.</p>
```
