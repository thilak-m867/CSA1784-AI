% Facts: parent relationships
parent(john, mary).
parent(john, david).
parent(susan, mary).
parent(susan, david).

parent(mary, anna).
parent(mary, tom).

parent(david, peter).

% Gender facts

male(john).
male(david).
male(tom).
male(peter).

female(susan).
female(mary).
female(anna).

%Rules

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

child(X, Y) :-
    parent(Y, X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).

siblings(X, Y):-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

brother(X, Y):-
    siblings(X, Y),
    male(X).

sister(X, Y) :-
    siblings(X, Y),
    female(X).



