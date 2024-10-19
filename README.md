## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
### 2.1 what refactoring signs (code smells) suggest this refactoring?
In the original design, the Movie class was responsible for providing the rental price and rental points, even though these values were only used by the Rental class. This led to the following issues:
|**Code Smells**|**Explaination**|
| - | - |
| **Middleman** | The Movie class was acting as a middleman by forwarding calls from Rental to the PriceStrategy, violating the Remove Middleman refactoring principle. |
### 2.2 what design principle suggests this refactoring? Why?
Single Responsibility Principle (SRP)
“A class should have only one reason to change”.

By moving price-related logic such as the price code and methods to calculate price and rental points to the Rental class, the Movie class is only responsible for handling movie information, while the Rental class handles rental logic. 

### 5.2 where price_code_for_movie (price_code in my version) should be implemented? Why?
|**Reasons**|**Explaination**|
| - | - |
|**High Cohesion**| Price calculation is part of renting, so putting it in Rental makes the code more cohesive and logical.|
|**Single Responsibility Principle (SRP)**| The Rental class is responsible for calculating the price, so it makes sense for it to be the one that determines the price code. This keeps the Movie class focused on only movie details like title and genre. |
|**Low Coupling**| Keeping pricing logic in Rental avoids making Movie or other classes depend on pricing rules, reducing unnecessary connections between classes.|
