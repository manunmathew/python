# Regular Expression
Regular Expression or RegEx is a special sequence of characters that are used to search for a pattern in string

module re is used for regular expression in python

fullmatch(): it returns object if match is found
search(): it returns match object anywhere in the string
findall():it returns list that contains all match
split(): it returns a string has been split
sub(): it is used to replace the matches

a regular expression is created using mix of characters special sequences and sets

## characters:
[] : it represents a set of characters and numbers
\ : it represents special sequence #\s,\d,\w
^ : it represents patterns present at the beginning of a
string

* :it represents 0 or more occurance
[0-9]*

+ : it represents 1 or more occurance

[0-9]+
{} : specified number of occurance of pattern
#limit

| : it represents this or that character is
present



## rules  of regex :

x='[abc]'  : either a ,b, or c

x='[^abc]' : except abc

x='[a-z]' :  lower case a to z

x='[A-Z]' : upper case A-Z

x='[a-zA-z]' : both lower case and uppercase

x='[0-9]' : it checks the digit

x='[a-zA-Z0-9]' lower cases , upper cases or digit



## special sequence :
x='\s' : check space
x='\d' :check digit
x='\D' : it returns string except number
x='\w' :it returns a string contains a word



## quantifiers :
x='[a-z]+' :1 or more
x='[a-z]*' :0 or more
x='[a]?' a included or not included
x='[a]{n}' :  #n->number #[a-z]{2}
x='[a]{n,k}' : n->minimum number k->maximum number
