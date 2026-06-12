% ====================================================================
% Aim: To write a Prolog program to identify fruits and their colors 
%      using backtracking.
% ====================================================================

% Step 1: Define fruit/2 facts pairing each fruit with its color.
% Format: fruit(FruitName, Color).
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(strawberry, red).
fruit(lemon, yellow).
fruit(orange, orange).
fruit(blueberry, blue).
fruit(cherry, red).

% Step 2: Define match_fruit_color/2 using the fruit/2 predicate.
% This rule leverages Prolog's built-in backtracking mechanism to match 
% or look up a fruit and its color.
match_fruit_color(Fruit, Color) :-
    fruit(Fruit, Color).

% Step 3: Use findall/3 to collect all fruits of a given color.
% Format: findall(Object, Condition, List)
get_fruits_by_color(Color, FruitList) :-
    findall(Fruit, fruit(Fruit, Color), FruitList).

% ====================================================================
% Step 4: Backtracking enumerates all fruit-color pairs automatically.
% ====================================================================
% To observe backtracking and test the database, try these queries:
%
% Query A: Enumerate all red fruits one by one using backtracking.
% (Press ';' after each result in the terminal to force backtracking)
% ?- match_fruit_color(Fruit, red).
% Output: 
% Fruit = apple ;
% Fruit = strawberry ;
% Fruit = cherry.
%
% Query B: Collect ALL red fruits into a single list at once using findall.
% ?- get_fruits_by_color(red, List).
% Output: List = [apple, strawberry, cherry].
%
% Query C: List every single fruit-color pair in the database.
% ?- match_fruit_color(Fruit, Color).
% (Pressing ';' will cycle through all 8 facts systematically)
% ====================================================================
