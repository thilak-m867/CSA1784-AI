% Facts: birds that can fly
can_fly(sparrow).
can_fly(eagle).
can_fly(parrot).
can_fly(pigeon).

% Facts: birds that cannot fly
cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

% Rule: A bird can fly if it is listed in can_fly/1
flies(Bird) :-
    can_fly(Bird).

% Rule: A bird cannot fly if it is listed in cannot_fly/1
does_not_fly(Bird) :-
    cannot_fly(Bird).
