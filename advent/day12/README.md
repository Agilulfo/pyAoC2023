# brainstorming

each damaged "condition record" is accompanied
by an additional verification string that enumerate the lenght of sequences of broken springs

e.g.
the record:
`.##...###....#`

would have the following verification string:
`2,3,1`

## bruteforcing solution

e.g.
considering this input

```
?????????????????
2,3,1
```

if you would only know the lenght of the condition record: 17
you could assume that the shortest possible reconstruction would be:
```
##.###.#
2 ^ 3 ^1
```
where each arrow indicate the mimimum required space between broken sequences.

the sequence above is long 8.
this means that there are other (17 - 8 = 9) `.` that can be spread and in between the different sequences to obtain all the possible 17 elements sequences that cotain subsequences of 2, 3 and 1 broken springs.



```
+##.+###.+#+
A   B    C D
```
the total numeber of sequence is equal to the number of ways you can group 9 dots in four groups (A,B,C and D potentially empty)

```
A B C D

9 0 0 0
8 1 0 0
8 0 1 0
8 0 0 1
7 2 0 0
7 0 2 0
7 0 0 2
7 1 1 0
7 0 1 1
7 1 0 1
.... etc
```

I don't remember much about combinatronics math, however it might be possible to use one of the formulas to calculate how many such combinations are possible.
Either way I have a feeling you will have to deal with a lot of combinations.

if your condition record still contains some valuable information. you would have then to produce all the possible sequences and count how many of them are compatible with your partial information.

writing an algorithm that uses this bruteforce approach that generate all the possible combinations is possible but it might not be practically usable to be used with arbitrary inputs.

### reconstructable records

in some cases the verification string might be sufficient to recover the missing parts, for instance if  for the damaged record:
`.#??????#.???#`
we would have the verification string

`2,3,1`
using some of the non damaged information we can recompose the string:

```
.#????#?#????#
 ^    ^ ^    ^
 A     B     C
```

the position marked as A need to be the beginning of the first sequence made of 2 broken springs

the position C must be the position of the last sequence made of 1 broken spring

given the points above the only left sequence of 3 broken spring must start and end in the points marked with the letter B.

`.##???###????#`

the remaining "?" (spring of unknown condition) can be now replaced with "." (spring in working order)

`.##...###....#`

### unreconstructable records
in other cases a damaged condition record cannot be fully reconstructed

`??#??`

with a verification string as:

`2`

can be reconstructed as `.##..` or as `..##.`

### composed records

it is possible to calculate the possible solutions by breaking the records in sub parts,
find out in how many way each part can be reconstructed.

the possible combination of the whole sequence can be calculated as multiplication of the combination of each part

given the verification string of `3,3,4`
we can split the record along the `^` points  in A,B and C parts:
```
??#?????#??????#???
  A  ^  B  ^   C
```
`A` can be reconstructed in 3 ways:
`###..`
`.###.`
`..###`

same can be done for `B`

`C` can be reconstructed in 4 ways:
`####...`
`.####..`
`..####.`
`...####`

the total number of ways the original sequence can be reconstructed is
`3*3*4 = 36`

### multiple splitting options

in some cases simply splitting the sequence in sub sequences is not possible
e.g.

in this case: `????#?????#?????` with verification sequence: `4,4`
you cannot split in a given point

the two locations marked below are related to the two verification sequences
```
????#?????#?????
    ^     ^
   (4)   (4)
```

however you cannto split in two substring and then multiply the amount of options you have for each string because some combinations might overalap as showne below

```
???.####.?#?????
????#?.####.????
```

in such cases you could split the sequence in multiple  points

```
????#?????#?????
      ^^^
      ABC
```

split in `A` getting `????#?` and `???#?????`
getting `2*4=8` reconstructions

split in `B` getting `????#??` and `??#?????`
getting `3*3=9` reconstructions

split in `C` getting `????#???` and `?#?????`
getting `4*2=8` reconstructions

the total combinations are given by the sum of all combinations for each splitting points
`8+9+8=25`
