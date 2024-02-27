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

# Brainstorming (part 2)

oh wow! this looks to be one of the hardest "part 2" so far!

there are few problems to solve.

1. figure out which side of the pipe loop is the inside  and which is the outside
2. follow the pipeline and identify points touching the pipeline that are inside the loop
3. "color" the gap inside the loop extending to points not touching the loop
4. include in the area to color also the points that are occupied by broken pieces

## inside/outside identification

once identified the loop you can count how many times you go left and how many you go right
e.g. every time you turn right increment a counter and every time you go left decrease the counter
if at the end of the loop the counter is positive you are followihg the loop in a clockwise direction
if at the end of the loop the coutner is negative you are following the loop in a counterclockwise direction

in the first case the inside is on your right, in the second it is on your left.

## exclusion of random pipes
we need to be able to identify pipe pieces that are not part of the pipeline and that can be accounted as part othe field.

two options come to mind.
keep a database (pyhon set) of the pieces part of the pipeline and then scan the map to remove the ones that are not part ofit

for each piece found in a field, follow the partial pipe it is part of to make sure it is not part of a loop and remove all of them,
a loop might be inside our loop so you could check that none of the pieces in that loop are not connected to our loop (the database solution overall looks to be more efficient)

## coloring algorithm

once you identify a location that is part of an inside field how do you make sure each point in that patch is "coloured" (counted as part of our intereste area)?

one option could be to start creating a database of that field and recursivelly explore in all 4 directions making sure not to come back to points that have already been discovered .

there might be a more efficient option: eg. going first left, then down and again right etc.. but the algorithm should take into account possibly complicated shapes of the patches.
