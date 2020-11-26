
[Delta Lab](https://links.deltalab.ai/website) | [Twitter](https://links.deltalab.ai/twitter) | [LinkedIn](https://links.deltalab.ai/linkedin)

---

# Calculator

- Omar Trejo
- February, 2016

## Problem

Given a valid string of math expressions, such as `3.1 + 4 * 5`, implement a
calculator. For the sake of simplicity, you can assume all operations will be
passed valid parameters. You do not need to concern yourself with error handling
for occurrences like non-mathematical symbol inputs.

Please do not use `eval()`.

### First Step

Please implement `Calc` to support double and mathematical operators such as +,
-, \*, and /. Mathematical operators will be delimited by a space. Please note:

- Input numbers are of the double type and can be negative.
- Operators \* and / has higher precedence than + and -.

For example,

~~~python
# Should return 23
calculator.calc("3 + 4 * 5")
# Should return 5.857142
calculator.calc("3 + 4 * 5 / 7")
~~~

### Second Step

Please update `calc` to support the use of parenthesis `()`, where contents
within the parenthesis are prioritized during computation.

~~~python
# Should return 5.0
calculator.calc("( 3 + 4 ) * 5 / 7")
~~~

### Third Step

Please implement `calc_with_vars`. Enable the method to accept a list of strings
representing assignment statements. The left-hand side should be the variable
and the right-hand side should be the mathematical expression that may contain
previously defined variables. Variables are in the form [a-z]+, and there will
be spaces around the equal sign `=`.

~~~python
# Should return the list, [3, 243].
calculator.calc_with_vars([
    "pi = 3",
    "pizza = 9 * 9 * pi"])
~~~

## Submission

Upon completion, please follow the instructions described in the website (where
you found the instructions to download the project) to submit your solution. You
can submit as many times as you prefer. Your last submission will be used for
evaluation as well as marking the end of your coding assessment.

Lastly, do not be concerned if you are running a little bit over time (0-10
minutes). We do not penalize moderately tardy submissions.

---

> "We are the people we have been waiting for."
