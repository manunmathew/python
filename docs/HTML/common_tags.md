# Common HTML Tags

## Types of HTML Tags

HTML tags can be classified into two types:

### 1. Block Tags

Block tags create elements that typically start on a new line and take up the full width available. Some examples include:
- `<hr>`: Defines a thematic break or horizontal line.
- `<p>`: Defines a paragraph.
- `<h1>`, `<h2>`, `<h3>`, etc.: Define headings.

### 2. Inline Tags

Inline tags create elements that do not start on a new line and only take up as much width as necessary. Some examples include:
- `<a>`: Defines a hyperlink (anchor tag).
- `<b>`: Bolds the text.
- `<i>`: Italicizes the text.

---

## Headings

HTML defines six levels of headings, ranging from `<h1>` (most important) to `<h6>` (least important).

- `<h1>`: The highest priority heading, typically used for main titles.
- `<h6>`: The lowest priority heading, often used for subheadings or smaller content.

Example:
```html
<h1>Main Title</h1>
<h2>Subheading</h2>
```
---

## Text Formatting Tags

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

---

## Paragraphs

The `<p>` tag defines paragraphs of text. Browsers automatically add space above and below paragraphs.

Example:
```html
<p>This is a paragraph of text.</p>
```
---

## Links (Anchor Tags)

The `<a>` (anchor) tag is used to create hyperlinks. It uses the `href` attribute to specify the destination URL.

Example:
```html
<a href="https://www.example.com">Visit Example</a>
```
To open the link in a new tab, add `target="_blank"`:
```html
<a href="https://www.example.com" target="_blank">Visit Example</a>
```
---

## Horizontal Line

The `<hr>` tag creates a horizontal line, often used to separate content. It is an empty tag, meaning it doesn’t require a closing tag.

Example:
```html
<hr>
```
