% ====================================================================
% Aim: To write a Prolog program to maintain and query a database of 
%      planets and their properties.
% ====================================================================

% Step 1: Define planet/5 facts with name, type, size, temperature, and position.
% Format: planet(Name, Type, SizeCategory, AvgTempCelsius, PositionFromSun).
planet(mercury, terrestrial, small, 167, 1).
planet(venus, terrestrial, medium, 464, 2).
planet(earth, terrestrial, medium, 15, 3).
planet(mars, terrestrial, small, -65, 4).
planet(jupiter, gas_giant, large, -110, 5).
planet(saturn, gas_giant, large, -140, 6).
planet(uranus, ice_giant, medium, -195, 7).
planet(neptune, ice_giant, medium, -200, 8).

% Step 2: Define planet_properties/5 to look up a planet by name.
% This rule takes a PlanetName and binds the remaining 4 variables to its properties.
planet_properties(Name, Type, Size, Temperature, Position) :-
    planet(Name, Type, Size, Temperature, Position).

% ====================================================================
% Step 3: Query for specific properties or categories of planets.
% ====================================================================
% To test this database, run the following sample queries in your interpreter:
%
% Query A: Look up all properties of a specific planet (e.g., Earth)
% ?- planet_properties(earth, Type, Size, Temp, Pos).
% Output: Type = terrestrial, Size = medium, Temp = 15, Pos = 3.
%
% Query B: Find all planets belonging to a specific category (e.g., gas_giant)
% ?- planet(Name, gas_giant, _, _, _).
% Output: 
% Name = jupiter ;
% Name = saturn.
%
% Query C: Find planets that are close to the Sun (Position less than 4)
% ?- planet(Name, _, _, _, Position), Position < 4.
% Output:
% Name = mercury, Position = 1 ;
% Name = venus, Position = 2 ;
% Name = earth, Position = 3.
% ====================================================================
