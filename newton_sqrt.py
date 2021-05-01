"""
You usually need a scientific calculator to determine the square root of a number. Isaac Newton devised a clever method
to easily approximate the square root without having to use a calculator that has the square root function.

His method consists of making an educated guess and then entering it into his simple equation. A calculator would be
handy for the arithmetic involved.

You repeatedly take your answer and enter it in his equation until the correct square root is obtained.

Suppose you wanted to find the square root of a positive number N. Newton's method involves making an educated guess of
a number A that, when squared, will be close to equaling N.

For example, if N = 121, you might guess A = 10, since A² = 100. That is a close guess, but you can do better than that.

The equation to use in this method is:

√ N ≈ ½(N/A + A)

where

N is a positive number of which you want to find the square root
√ is the square root sign
≈ means "approximately equal to..."
A is your educated guess
If N = 121 and you guess at A = 10, you can enter the values into the equation:

√ 121 ≈ ½(121/10 + 10) = ½(12.1 +10) = ½(22.1) = 11.05

That is pretty close to the correct answer of 11.

Newton's method allows you to repeat the estimation a number of times to approach an exact number, if necessary.

Suppose we made a guess of A = 5, which is not very close. Entering substituting 5 in the equation results in:

√ 121 ≈ ½(121/5 + 5) = ½(24.2 +5) = ½(29.2) = 14.6

Use 14.6 in another approximation:

√ 121 ≈ ½(121/14.6 + 14.6) = ½(8.29 +14.6) = ½(22.89) = 11.445

That is much closer. We can do one more iteration in this example:

√ 121 ≈ ½(121/11.445 + 11.445) = ½(10.57 +11.445) = ½(22.017) = 11.008

You can see that we are approaching the exact value of the square root. You can continue, if you want the answer to be
more accurate, but it should not be necessary.

With a better guess for A, you should be able to use this method with only one calculation.
"""

try:
    number = int(input("Find the square root of an integer: "))
    guess = float(input("Initial guess: "))
    tolerance = float(input("Tolerance: "))

    original_guess = guess
    count = 0
    previous = 0.0

    while abs(previous - guess) > tolerance:
        previous = guess
        quotient = number / guess
        guess = (quotient + guess) / 2
        count += 1

    print(f"Square root of {number} is {guess}")
    print(f"it took {count} reps to get to {tolerance:8.8f} starting with a guess of {original_guess}")

except ValueError as e:
    print(e)
    quit(1)