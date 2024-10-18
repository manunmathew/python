# CSS Selectors Overview

CSS selectors are patterns used to select the elements you want to style in your web page. They allow you to target specific HTML elements and apply styles to them. Below are some of the common types of CSS selectors:

## 1. Element Selector

**Description:**
The element selector selects HTML elements by their tag name. This type of selector is used when you want to style all occurrences of a specific HTML element.

**Syntax:**
```html
    element {
      property: value;
    }
```
**Example:**
```html
    p {
      color: blue;
    }
```
In this example, all `<p>` elements (paragraphs) will have blue text.

## 2. ID Selector

**Description:**
The ID selector is used to select an HTML element with a specific `id` attribute. Since `id` values are unique within an HTML document, this selector applies styles to only one element at a time. It is selected using the `#` symbol followed by the `id` name.

**Syntax:**
```html
    #id-name {
      property: value;
    }
```
**Example:**
```html
    #header {
      background-color: green;
    }
```
In this example, the element with the `id="header"` will have a green background.

## 3. Class Selector

**Description:**
The class selector is used to select HTML elements that have a specific `class` attribute. Unlike IDs, the same class name can be applied to multiple elements. It is selected using the `.` symbol followed by the class name.

**Syntax:**
```html
    .class-name {
      property: value;
    }
```
**Example:**
```html
    .button {
      background-color: red;
    }
```
In this example, all elements with `class="button"` will have a red background.

## 4. Group Selector

**Description:**
The group selector allows you to apply the same styles to multiple selectors. You can group selectors by separating them with a comma. This helps avoid repetition in your CSS code.

**Syntax:**
```html
    selector1, selector2 {
      property: value;
    }
```
**Example:**
```html
    h1, h2, p {
      color: black;
    }
```
In this example, all `<h1>`, `<h2>`, and `<p>` elements will have black text.

## 5. Universal Selector

**Description:**
The universal selector is used to select all elements on the web page. It is denoted by an asterisk (`*`). This selector is often used to apply global styles or reset default browser styles.

**Syntax:**
```html
    * {
      property: value;
    }
```
**Example:**
```html
    * {
      margin: 0;
      padding: 0;
    }
```
In this example, the universal selector removes all margin and padding from every element on the page.

## Summary of Selectors

| Selector        | Symbol   | Description                                    |
|-----------------|----------|------------------------------------------------|
| Element Selector| (none)   | Selects all elements of a specific type (e.g., `p`, `h1`) |
| ID Selector     | `#`      | Selects an element by its unique `id` attribute |
| Class Selector  | `.`      | Selects elements by their `class` attribute, can be applied to multiple elements |
| Group Selector  | `,`      | Selects multiple elements and applies the same styles to them |
| Universal Selector | `*`    | Selects all elements on the web page           |


## Code Reference
Refer to the [CSS Selectors](https://github.com/manunmathew/python/raw/main/code/CSS/internal.html)
