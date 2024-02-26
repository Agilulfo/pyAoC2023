# brainstorming (PART 1)

Keep the map as a list of string

find Start ("S")

considering S as a piece of  the pipeline the most distant piece from S is distant from S:
`<total_number_of_pieces_in_pipeline> / 2`

e.g. given the pipe
```
S7
LJ
```

`most distant = 4 / 2`

```
01
12
```

many possibilities to calculate distance.

the problem looks to be one of the problem that would benefit from parallelization.
however keeping things relativelly simple you could simply jump from start and keep a count of how many steps you take till you reach againt the start.

## functionalities needed

for sure a function that given a point and a direction (u,d,l,r) up, down, left, right returns the item adjacent piece in the specified direction


## strategy

starting from start retrieve visit all the adjacent nodes till you find a next pipe that has one of the ending towards you

```
.....
..L..
.JS-.
..|..
.....

```

in the example above we should not consider L and J because are not valid pipes that can be connected to S

"-" or "|" in this case could be good candidate

arbitrarelly pick one e.g. "-"
and move to the other end of that piece (excluding the direction from where you are coming from)

repeat till you get again in S

count the jumps you do and divide by 2

### assumptions

I'm assuming that there no cases where dead ends start from S
```
.....
..|..
.-S-.
..|..
.....

```
in such cases you will have to visit each direction to ensure it is not a deadend
