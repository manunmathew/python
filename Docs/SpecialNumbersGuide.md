# Special Numbers in Mathematics

## 1. Harshad Numbers
A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.

**Examples:**
- **18:** The sum of its digits is 1 + 8 = 9, and 18 is divisible by 9.
- **21:** The sum of its digits is 2 + 1 = 3, and 21 is divisible by 3.

## 2. Deserium Numbers (Narcissistic Numbers)
Given a number “n”, find if it is Disarium or not. A number is called Disarium if sum of its digits powered with their respective positions is equal to the number itself.

**Examples:**

Input   : n = 135
Output  : Yes
1^1 + 3^2 + 5^3 = 135
Therefore, 135 is a Disarium number

Input   : n = 89
Output  : Yes
8^1+9^2 = 89
Therefore, 89 is a Disarium number

Input   : n = 80
Output  : No
8^1 + 0^2 = 8


## 3. Armstrong Numbers
An Armstrong number (named so after Michael F. Armstrong), also called a narcissistic number, a pluperfect digital invariant, or a plus perfect number, is a number that is equal to the sum of its own digits when they are raised to the power of the number of digits. As an example, the smallest Armstrong number is 153, which is equal to .

**Examples:**
- **153:** As explained above, 153 is both a Deserium and an Armstrong
number.
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
- **370:** Similarly, 370 is both a Deserium and an Armstrong number.
- **89:**
8^1 + 9^2 = 8 + 81 = 89
8^2 + 9^2 = 64 + 81 = 145
So, 89 is a number that is a Deserium number but not an Armstrong number.

## 4. Perfect Numbers
A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).

**Examples:**
- **6:** The proper divisors are 1, 2, and 3. \( 1 + 2 + 3 = 6 \).
- **28:** The proper divisors are 1, 2, 4, 7, and 14. \( 1 + 2 + 4 + 7 + 14 = 28 \).

## 5. Prime Numbers
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

**Examples:**
- 2, 3, 5, 7, 11, 13, 17, 19, 23, etc.

## 6. Fibonacci Numbers
Fibonacci numbers form a sequence where each number is the sum of the two preceding ones, usually starting with 0 and 1.

**Examples:**
- 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.

## 7. Triangular Numbers
A triangular number or triangle number is the number of dots in an equilateral triangle uniformly filled with dots. The \( n \)-th triangular number is the sum of the first \( n \) natural numbers.

**Examples:**
- The 1st triangular number is 1.
- The 3rd triangular number is \( 1 + 2 + 3 = 6 \).
- The 5th triangular number is \( 1 + 2 + 3 + 4 + 5 = 15 \).

## 8. Palindromic Numbers
A palindromic number is a number that remains the same when its digits are reversed.

**Examples:**
- 121, 131, 1221, 1331, etc.

## 9. Happy Numbers
A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit repeatedly. If this process results in an endless cycle of numbers which does not include 1, then the number is called an unhappy number (or sad number).

**Examples:**
- **19:** \( 1^2 + 9^2 = 82 \), \( 8^2 + 2^2 = 68 \), \( 6^2 + 8^2 = 100 \), \( 1^2 + 0^2 + 0^2 = 1 \) (Happy number).
- **4:** \( 4^2 = 16 \), \( 1^2 + 6^2 = 37 \), \( 3^2 + 7^2 = 58 \), \( 5^2 + 8^2 = 89 \), \( 8^2 + 9^2 = 145 \), \( 1^2 + 4^2 + 5^2 = 42 \), \( 4^2 + 2^2 = 20 \), \( 2^2 + 0^2 = 4 \) (Cycle, unhappy number).

## 10. Catalan Numbers
Catalan numbers form a sequence of natural numbers that have many applications in combinatorial mathematics. The \( n \)-th Catalan number can be expressed directly in terms of binomial coefficients.

**Examples:**
- \( C_0 = 1 \)
- \( C_1 = 1 \)
- \( C_2 = 2 \)
- \( C_3 = 5 \)
- \( C_4 = 14 \)

## 11. Kaprekar Numbers
A Kaprekar number is a number \( n \) such that if you square it and add the right-hand digits to the left-hand digits, the result is \( n \).

**Examples:**
- **45:** \( 45^2 = 2025 \), and \( 20 + 25 = 45 \).

## 12. Twin Prime Numbers
Twin primes are pairs of prime numbers that have a difference of 2.

**Examples:**
- (3, 5), (11, 13), (17, 19), etc.
