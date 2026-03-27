-- Finding the biggest single number in a list of numbers

Select Max(num) as num
From(
    Select num
    From MyNumbers
    Group By num
    Having Count(num) = 1
) as single_numbers;