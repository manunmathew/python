
# Bootstrap Documentation

## What is Bootstrap?

**Bootstrap** is a popular front-end framework for developing responsive, mobile-first websites and web applications. It includes HTML, CSS, and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components. Bootstrap helps developers create consistent and efficient layouts, making web development faster and easier.

---

## How to Start with Bootstrap

To start using Bootstrap in your project, you need to include its CSS file. Here is the easiest way to include Bootstrap using a Content Delivery Network (CDN):

### Using Bootstrap CSS via CDN

Add the following `<link>` tag to the `<head>` of your HTML file:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Project</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Your content here -->
</body>
</html>
```

This will include Bootstrap's CSS, enabling you to use its classes to style your website.

---

## Built-in Stylesheet

Bootstrap includes a built-in stylesheet that provides various classes to help design responsive websites quickly and easily. Below are some commonly used classes and features:

---

## Containers

Bootstrap containers provide a means to center and horizontally pad the content. There are two types of containers:

1. **`.container`**:
   - This class provides a responsive fixed-width container.
   - It adjusts its width based on the current screen size, offering a center alignment for the content.

```
<div class="container">
    <!-- Content here will be centered and padded -->
</div>
```

2. **`.container-fluid`**:
   - This class provides a full-width container that spans the entire width of the viewport.
   - Useful for creating layouts that are meant to stretch across the screen.

```
<div class="container-fluid">
    <!-- Content here will stretch across the entire screen -->
</div>
```

---

## Background Colors

Bootstrap provides several classes for setting background colors. Each class applies a different background color to the selected element:

- **`.bg-primary`**: Applies a blue background.
- **`.bg-success`**: Applies a green background.
- **`.bg-info`**: Applies a light blue background.
- **`.bg-warning`**: Applies a yellow background.
- **`.bg-danger`**: Applies a red background.
- **`.bg-secondary`**: Applies a gray background.
- **`.bg-dark`**: Applies a dark background.
- **`.bg-light`**: Applies a light background.

Example:

```
<div class="bg-primary text-white">Primary Background</div>
<div class="bg-success text-white">Success Background</div>
<div class="bg-warning text-dark">Warning Background</div>
```

---

## Grid System

The Bootstrap grid system is built with **flexbox** and uses containers, rows, and columns to create responsive layouts. It supports up to **12 columns** across the page.

### Basic Structure:

- **Containers**: Hold the rows and columns.
- **Rows**: Wrap columns and provide horizontal alignment.
- **Columns**: Define the number of columns to use, creating a responsive grid.

```
<div class="container">
    <div class="row">
        <div class="col-6">
            <!-- This column takes up half the row's width -->
        </div>
        <div class="col-6">
            <!-- This column also takes up half the row's width -->
        </div>
    </div>
</div>
```

### Key Points:

- **Up to 12 columns** can be used per row, but you can use fewer.
- Bootstrap's responsive grid allows you to define different column sizes for different screen sizes using classes like `col-sm-*`, `col-md-*`, `col-lg-*`, and `col-xl-*`.
- The **flexbox-based system** provides flexibility for arranging and aligning content within the grid.

Example:

```
<div class="container">
    <div class="row">
        <div class="col-md-4">Column 1 (4 units)</div>
        <div class="col-md-4">Column 2 (4 units)</div>
        <div class="col-md-4">Column 3 (4 units)</div>
    </div>
</div>
```

This setup creates three equal-width columns on medium and larger screens.

---

## Official Bootstrap Link

For more information and documentation, visit the [Bootstrap Official Website](https://getbootstrap.com/).

---
