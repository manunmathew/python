
# HTML Tables Overview

HTML tables are used to display tabular data. Each table consists of rows and columns, and various tags help define the structure.

## Table Creation with `<table>`
- The `<table>` tag is used to create a table.

## Table Rows with `<tr>`
- Each table row is defined by the `<tr>` tag (stands for **table row**).

## Table Data with `<td>`
- Each table cell is defined by the `<td>` tag (stands for **table data**).

## Table Header with `<th>`
- The `<th>` tag is used for table headers instead of the `<td>` tag.
- Headers typically define titles for each column or row.

## HTML Table Tags

| Tag          | Description                                                    |
|--------------|----------------------------------------------------------------|
| `<table>`    | Defines a table                                                |
| `<th>`       | Defines a header cell in a table                               |
| `<tr>`       | Defines a row in a table                                       |
| `<td>`       | Defines a cell in a table                                      |
| `<caption>`  | Defines a table caption                                        |
| `<colgroup>` | Specifies a group of columns for formatting                    |
| `<col>`      | Specifies properties for columns within a `<colgroup>` element |
| `<thead>`    | Groups the header content in a table                           |
| `<tbody>`    | Groups the body content in a table                             |
| `<tfoot>`    | Groups the footer content in a table                           |

## Example Usage of a Table

Use the `<table border="1">` attribute to create a table with a border.

## Table Colspan & Rowspan

### Colspan
- Use the `colspan` attribute to make a cell span over multiple columns.
  - Example:
    `<td colspan="2">Content</td>`

### Rowspan
- Use the `rowspan` attribute to make a cell span over multiple rows.
  - Example:
    `<td rowspan="2">Content</td>`

## Code Reference
Refer to the [HTML Tables](https://github.com/manunmathew/python/raw/main/code/HTML/table.html)
