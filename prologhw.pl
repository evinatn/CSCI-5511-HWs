% Kinship Domain
parent(charles, william).
parent(charles, harry).
parent(elizabeth, charles).
parent(george, elizabeth).
parent(george, margaret).
parent(elizabeth, anne).
parent(elizabeth, andrew).
parent(elizabeth, edward).
parent(anne, peter).
parent(anne, zara).
parent(andrew, beatrice).
parent(andrew, eugenie).
parent(edward, louise).
parent(edward, james).


child(X,Y) :- parent(Y,X).

sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \= Y.

cousin(X,Y) :- parent(A,X), parent(B,Y), sibling(A,B).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).


% Maze Solving
connected(1,2).
connected(3,4).
connected(5,6).
connected(7,8).
connected(9,10).
connected(11,13).
connected(13,14).
connected(15,16).
connected(17,18).
connected(19,20).
connected(4,1).
connected(6,3).
connected(4,7).
connected(6,12).
connected(14,9).
connected(12,15).
connected(16,11).
connected(14,17).
connected(16,19).

path(X,Y) :- connected(X,Y).
path(X,Y) :- connected(X,Z), path(Z,Y).

path_length(X,Y,1) :- connected(X,Y).
path_length(X,Y,N) :- connected(X,Z), path_length(Z,Y,M), N is M+1.
