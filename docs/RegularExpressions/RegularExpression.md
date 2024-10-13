# Regular Expression

Regular Expression (RegEx) is a special sequence of characters used to search for patterns in strings.

The `re` module is used for regular expressions in Python.

## Common Functions in the `re` Module:

- **`fullmatch()`**: Returns a match object if the entire string matches the pattern.
- **`search()`**: Returns a match object for the first occurrence of the pattern anywhere in the string.
- **`findall()`**: Returns a list of all matches of the pattern in the string.
- **`split()`**: Splits the string at each match of the pattern.
- **`sub()`**: Replaces all matches with a specified string.

## Creating a Regular Expression

A regular expression is created using a mix of characters, special sequences, and sets.

### Characters

- `[]`: Represents a set of characters or numbers.
- `\`: Represents a special sequence (e.g., `\s`, `\d`, `\w`).
- `^`: Represents patterns present at the beginning of a string.
- `*`: Represents 0 or more occurrences.
  Example: `[0-9]*`
- `+`: Represents 1 or more occurrences.
  Example: `[0-9]+`
- `{}`: Specifies the number of occurrences of a pattern.
  Example: `[a-z]{2}`
- `|`: Represents "this or that" in the pattern.

## Rules of Regex:

- **`[abc]`**: Matches either `a`, `b`, or `c`.
- **`[^abc]`**: Matches anything except `a`, `b`, or `c`.
- **`[a-z]`**: Matches any lowercase letter (`a` to `z`).
- **`[A-Z]`**: Matches any uppercase letter (`A` to `Z`).
- **`[a-zA-Z]`**: Matches both lowercase and uppercase letters.
- **`[0-9]`**: Matches any digit (`0` to `9`).
- **`[a-zA-Z0-9]`**: Matches lowercase, uppercase letters, or digits.

## Special Sequences:

- **`\s`**: Matches a space.
- **`\d`**: Matches a digit.
- **`\D`**: Matches anything except a digit.
- **`\w`**: Matches a word character (alphanumeric).

## Quantifiers:

- **`[a-z]+`**: Matches one or more lowercase letters.
- **`[a-z]*`**: Matches zero or more lowercase letters.
- **`[a]?`**: Matches if `a` is included or not included (0 or 1 occurrence).
- **`[a]{n}`**: Matches exactly `n` occurrences of `a`.
  Example: `[a-z]{2}`
- **`[a]{n,k}`**: Matches at least `n` and at most `k` occurrences of `a`.
