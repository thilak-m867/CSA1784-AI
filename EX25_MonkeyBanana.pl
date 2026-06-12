% --- States ---% --- States ---
% Fixed the typo here: changed 'has_not_earen' to 'has_not_eaten'
initial_state(state(at_door, on_floor, at_window, has_not_eaten)).
final_state(state(_, _, _, has_eaten)).

% --- Actions ---
action(state(at_window, on_floor, at_window, has_not_eaten), grasp,
       state(at_window, on_floor, at_window, has_eaten)).

action(state(at_door, on_floor, W, HB), walk_to_window,
       state(at_window, on_floor, at_window, HB)).

% --- Core Solver Interface ---
solve(Actions) :-
    initial_state(StartState),
    solve_state(StartState, Actions).

% --- Helper Solver ---
solve_state(CurrentState, []) :- 
    final_state(CurrentState).

solve_state(CurrentState, [Action|Rest]) :-
    action(CurrentState, Action, NextState),
    solve_state(NextState, Rest).
