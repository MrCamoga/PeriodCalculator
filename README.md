# PeriodCalculator
Program to find the period of a sequence.

This is a python implementation of the algorithm used to find the period of a highway in the Langton's Ant program.

The sequence is given term by term and thus this algorithm is able to find the period of a huge sequence using constant memory (storing the first N terms of the sequence).

To make this possible, we are assuming that if the first N terms (for a large integer N) repeat at some point in the sequence, then we've found the period.
