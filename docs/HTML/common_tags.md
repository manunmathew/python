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
- `<br>`: Inserts a line break without starting a new paragraph.

---

## Headings

HTML defines six levels of headings, ranging from `<h1>` (most important) to `<h6>` (least important).

- `<h1>`: The highest priority heading, typically used for main titles.
- `<h6>`: The lowest priority heading, often used for subheadings or smaller content.

Example:
```html
<h1 align="center"><u>HTML <em>Introduction</em></u></h1>
<h2 align="right">Subheading</h2>
```
---

## Text Formatting Tags

These tags are used to style text elements in different ways:

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
- `<br>`: Adds a line break without starting a new paragraph.

Example:
```html
<p>This is a <mark>highlighted</mark> paragraph.</p>
<p>This is <strong>important</strong> text.</p>
<p>This is another sentence.<br>This sentence appears on a new line due to the `<br>` tag.</p>
```
---

## Paragraphs

The `<p>` tag defines paragraphs of text. Browsers automatically add space above and below paragraphs.

Example:
```html
<p>This is a paragraph of text.</p>
<p align="justify">
UTF-8 (Unicode Transformation Format - 8-bit) is a character encoding system designed to encode all possible characters (called code points) in the Unicode standard using one to four bytes. It is widely used because it supports a vast range of characters from many languages and symbols, while being backward compatible with ASCII (which only uses one byte per character).
</p>
```
---

## Links (Anchor Tags)

The `<a>` (anchor) tag is used to create hyperlinks. It uses the `href` attribute to specify the destination URL.

Example:
```html
<a href="https://www.google.com" target="_blank">Google</a>
<a href="src/Application.png" download>Download Image</a>
```
---

## Images

The `<img>` tag is used to embed images in a web page. The `src` attribute specifies the image source, and `width` and `height` attributes can control the size.

Example:
```html
<center>
<img src="src/Application.png" height="400px" width="600px">
</center>
```
---

## Videos

The `<video>` tag is used to embed a video in a webpage. You can add attributes like `controls`, `loop`, `muted`, and `autoplay`.

Example:
```html
<video src="src/video1.mp4" controls loop muted autoplay height="400px" width="600px"></video>
```
---

## Audio

The `<audio>` tag is used to embed audio content. Adding the `controls` attribute allows the user to control playback.

Example:
```html
<audio src="src/audio1.m4a" controls></audio>
```
---

## Horizontal Line

The `<hr>` tag creates a horizontal line, often used to separate content. It is an empty tag, meaning it doesn’t require a closing tag.

Example:
```html
<hr>
```
---

## Line Break

The `<br>` tag inserts a line break without starting a new paragraph. Unlike `<p>`, it does not create extra spacing between lines. It is useful for single-line breaks within paragraphs or other block-level elements.

Example:
```html
<p>This sentence is on one line.<br>This sentence starts on a new line due to the `<br>` tag.</p>
```
---

## Code Reference
Refer to the [HTML Tags](https://github.com/manunmathew/python/raw/main/code/HTML/Introduction.html)
