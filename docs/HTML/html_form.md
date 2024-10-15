
# HTML Forms Overview

HTML forms are used to collect user input and send it to a server for processing. Below are some commonly used HTML elements and their attributes.

## The `<form>` Element
- The `<form>` element is used to create an HTML form for user input.

## The `<input>` Element
- The `<input>` element is the most common form element. It can be used in various ways based on its `type` attribute.
- Example:
  `<input type="text" name="username">`

## Common HTML Input Types

- **Button**:
  - `<input type="button">` defines a clickable button.

- **Checkbox**:
  - `<input type="checkbox">` allows the user to select one or more options from a set.

- **Color**:
  - `<input type="color">` allows the user to select a color.

- **Date**:
  - `<input type="date">` allows the user to select a date.

- **Email**:
  - `<input type="email">` validates an email input.

- **File**:
  - `<input type="file">` lets the user select a file to upload.

- **Password**:
  - `<input type="password">` hides the input characters.

- **Radio**:
  - `<input type="radio">` allows the user to select one option from a set.

- **Submit**:
  - `<input type="submit">` submits the form to a server.

## The `<label>` Element
- The `<label>` element defines labels for `<input>` elements. Labels help identify what the input is for.
- Example:
  `<label>Username</label>`

## The `<select>` Element
- The `<select>` element creates a dropdown list.
- Example:
  `<select name="state">
    <option>--select--</option>
    <option>Kerala</option>
    <option>Tamil Nadu</option>
  </select>`

## The `<textarea>` Element
- The `<textarea>` element defines a multi-line text input.
- Example:
  `<textarea name="message"></textarea>`

## The `<button>` Element
- The `<button>` element defines a clickable button.
- Example:
  `<button type="submit">Submit</button>`

## Input Validation Attributes
- **required**: Specifies that an input field must be filled out before submitting.
  `<input type="text" name="username" required>`

- **minlength / maxlength**: Specifies the minimum and maximum number of characters allowed.
  `<input type="text" name="username" minlength="5" maxlength="20">`

- **pattern**: Specifies a regular expression that the input's value must match.
  `<input type="text" name="phone" pattern="[0-9]{10}">`

## Code Reference
Refer to the [HTML Forms ](../../code/HTML/forms.html)
