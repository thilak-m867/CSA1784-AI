dob(john, date(15, may, 1998)).
dob(alice, date(23, august, 2001)).
dob(bob, date(04, january, 1995)).
dob(mary, date(30, november, 2002)).

lookup(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).

