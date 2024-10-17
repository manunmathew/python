# CSS Overview

**CSS (Cascading Style Sheets)** is a language used to style the presentation of web pages, including layout, colors, and fonts. It enables separation of content from design and helps in enhancing the user experience by creating visually appealing web pages.

CSS can be applied in three main ways:
1. **Inline CSS**
2. **Internal CSS**
3. **External CSS**

## 1. Inline CSS

**Description:**
Inline CSS is used to apply a unique style to a single element directly within an HTML tag. This is achieved by using the `style` attribute within the HTML element.

**Syntax:**
    <tagname style="property: value;">Content</tagname>

**Example:**
    <p style="color: blue; font-size: 20px;">This is a paragraph with inline CSS.</p>

## 2. Internal CSS

**Description:**
Internal CSS is used when a single HTML document needs specific styles. The CSS rules are placed within the `<style>` tag inside the `<head>` section of the HTML document. This allows for centralized styling within a single file but limits reusability across multiple pages.

**Syntax:**
    <head>
      <style>
        selector {
          property: value;
        }
      </style>
    </head>

**Example:**
    <head>
      <style>
        p {
          color: green;
          font-size: 18px;
        }
      </style>
    </head>
    <body>
      <p>This paragraph uses internal CSS.</p>
    </body>

## 3. External CSS

**Description:**
External CSS allows for styling multiple HTML documents using a single CSS file. By linking to an external `.css` file from an HTML document, you can globally control the styles across the entire website. This is a preferred method for large projects since it promotes reusability and maintainability.

**Syntax (linking the external CSS):**
    <head>
      <link rel="stylesheet" href="styles.css">
    </head>

**Example (external CSS file `styles.css`):**
    p {
      color: red;
      font-size: 16px;
    }

**Example (HTML file):**
    <head>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <p>This paragraph is styled using external CSS.</p>
    </body>

**Key Points:**
- The external `.css` file should be saved with a `.css` extension.
- The file should not contain any HTML tags, only CSS rules.

## Code Reference
Refer to the [CSS](https://github.com/manunmathew/python/raw/main/code/CSS/inline.html)
