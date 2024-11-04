# Bootstrap Components Guide

This guide covers Bootstrap components for creating collapsible accordions, alerts, progress bars, dropdowns, pagination, spinners, breadcrumbs, offcanvas panels, and a carousel. Each component includes example code snippets for easy implementation.

---

## Accordion

Bootstrap’s accordion is a vertically collapsing component useful for displaying sections of content that expand or collapse.

**Usage:**
1. Use the `accordion` class on the main container.
2. Each collapsible item uses `accordion-item`.
3. To control each item's button, use `accordion-button`.
4. For expanded content, add the `.show` class to `accordion-collapse`.

**Example:**
```html
<div class="accordion" id="accordionExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingOne">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Accordion Item #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        Content for the first item.
      </div>
    </div>
  </div>
</div>
```

---

## Alerts

Bootstrap alerts are useful for displaying important information. Different classes customize the color.

**Example:**
```html
<div class="alert alert-primary">
  A simple primary alert—check it out!
</div>
```

---

## Progress

A progress bar displays the progress of a task.

**Example:**
```html
<div class="progress" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar" style="width: 0%"></div>
</div>
```

---

## Dropdown

Use the dropdown component to create a menu that expands when clicked.

**Example:**
```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown button
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
```

---

## Pagination

Pagination is used to divide content across multiple pages.

**Example:**
```html
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
```

---

## Spinners

Bootstrap provides various spinner styles for loading indicators.

**Example:**
```html
<div class="spinner-border text-primary" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
```

---

## Breadcrumb

Breadcrumbs provide links back to each previous page in the navigation hierarchy.

**Example:**
```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item"><a href="#">Library</a></li>
    <li class="breadcrumb-item active" aria-current="page">Data</li>
  </ol>
</nav>
```

---

## Offcanvas

The offcanvas component displays content outside the main page, over the viewport.

**Placement Classes:**
- `.offcanvas-start` for the left side
- `.offcanvas-end` for the right side
- `.offcanvas-top` for the top side
- `.offcanvas-bottom` for the bottom side

**Example:**
```html
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasTop" aria-controls="offcanvasTop">Toggle top offcanvas</button>

<div class="offcanvas offcanvas-top" tabindex="-1" id="offcanvasTop" aria-labelledby="offcanvasTopLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasTopLabel">Offcanvas top</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    Content for offcanvas.
  </div>
</div>
```

---

## Navbar Toggler

The `navbar-toggler` is useful for toggling navigation visibility on smaller screens. Classes `me-auto` and `ms-auto` help align items to the left or right.

**Example:**
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav me-auto">
      <li class="nav-item"><a class="nav-link active" href="#">Home</a></li>
    </ul>
    <ul class="navbar-nav ms-auto">
      <li class="nav-item"><a class="nav-link" href="#">Link</a></li>
    </ul>
  </div>
</nav>
```

---

## Carousel

A carousel cycles through images, text, or custom content, using indicators, controls, and sliding animations.

**Example:**
```html
<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
  <ol class="carousel-indicators">
    <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"></li>
    <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"></li>
    <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </a>
</div>
```

---
