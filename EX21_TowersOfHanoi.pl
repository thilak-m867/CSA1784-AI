move(1, Source, Target, _):-
    write('Move top disk from '), write(Source),
    write(' to '), write(Target), n1.

move(N, Source,Targer, Aux):-
    N>1,
    N1 is N-1,
    move(1, Source, Target, Aux),
    move(N1, Aux, Targer, Source).

% ====================================================================
% Aim: To write a Prolog program to solve the Towers of Hanoi 
%      problem recursively.
% ====================================================================

% Step 1: Base case – if N=1, move disk from Source to Target directly.
hanoi(1, Source, Target, _, Path) :-
    write('Move disk 1 from '), write(Source), write(' to '), write(Target), nl.

% Steps 2-4: Recursive case for N disks
hanoi(N, Source, Target, Auxiliary, Path) :-
    N > 1,
    M is N - 1,
    % Step 2: Move N-1 disks from Source to Auxiliary using Target.
    hanoi(M, Source, Auxiliary, Target, Path),
    
    % Step 3: Move the largest disk from Source to Target.
    write('Move disk '), write(N), write(' from '), write(Source), write(' to '), write(Target), nl,
    
    % Step 4: Move N-1 disks from Auxiliary to Target using Source.
    hanoi(M, Auxiliary, Target, Source, Path).

% ====================================================================
% How to execute this program:
% ====================================================================
% To solve the puzzle for 3 disks moving from peg 'A' to peg 'C' 
% using peg 'B' as the auxiliary tracker, run this query:
%
% ?- hanoi(3, 'A', 'C', 'B', _).
%
% Expected Terminal Output:
% Move disk 1 from A to C
% Move disk 2 from A to B
% Move disk 1 from C to B
% Move disk 3 from A to C
% Move disk 1 from B to A
% Move disk 2 from B to C
% Move disk 1 from A to C
% ====================================================================
