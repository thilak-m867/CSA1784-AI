% ====================================================================
% Aim: To write a Prolog program that recommends a diet based on 
%      a patient's disease.
% ====================================================================

% Step 1: Define food/4 facts with food name, type, taste, and nutritional property.
% Format: food(FoodName, FoodType, Taste, MainNutrientProperty)
%
food(spinach, vegetable, bitter, high_iron).
food(salmon, fish, savory, omega_3).
food(oatmeal, grain, bland, high_fiber).
food(apple, fruit, sweet, vitamins).
food(yogurt, dairy, sour, probiotics).
food(chicken_breast, meat, savory, lean_protein).
food(almonds, nut, nutty, healthy_fats).

% Step 2: Define diet/2 facts linking diseases to lists of recommended foods.
% Format: diet(DiseaseName, ListOfRecommendedFoods).
diet(diabetes, [oatmeal, spinach, almonds, chicken_breast]).
diet(hypertension, [spinach, apple, yogurt, salmon]).
diet(anemia, [spinach, chicken_breast, almonds]).
diet(high_cholesterol, [oatmeal, salmon, almonds, apple]).

% Step 3: Define suggest_diet/2 to query the diet for a given disease.
% This rule takes a Disease name and retrieves its corresponding list of foods.
suggest_diet(Disease, FoodList) :-
    diet(Disease, FoodList).

% ====================================================================
% How to execute queries in your Prolog terminal:
% ====================================================================
%
% Query A: Get the recommended diet list for Diabetes
% ?- suggest_diet(diabetes, Diet).
% Output: Diet = [oatmeal, spinach, almonds, chicken_breast].
%
% Query B: Find out which disease recommends a diet containing a specific list
% ?- suggest_diet(Disease, [spinach, apple, yogurt, salmon]).
% Output: Disease = hypertension.
%
% Query C: Check if a specific food list is recommended for Anemia
% ?- suggest_diet(anemia, [spinach, chicken_breast, almonds]).
% Output: true.
% ====================================================================
