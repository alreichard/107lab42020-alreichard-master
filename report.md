Lab #: 4								First Name: Alex
Date: 10/21/20						    Last  Name: Reichard
The time you took: 5 hours

Approach: what was your approach to accomplish the listed tasks? How did you arrive at the solutions?
I followed the instructions for each function. On the sentiment analysis first I took every non stopword,
and put a N in front of the next word negation word to mark it. To determine the sentiment I tried a few approaches and
ended on taking the median sentiment value of every non 0 sentiment word, and said if it was great less than or between breaking
points for positive negative and neutral. The negation I tried handling by changing the positive word after it to negative and vice versa.
Just getting rid of all words that had negation worked better, however.

Explanation: provide evidence that the implemented approach works (it could be just in terms of passed test cases)
and explain why it would work in general. Explain how your implementation meets the constraints/conditions
(if any, e.g., time complexity) mentioned in the description of the problem. In the 550 test cases I got the results:
positive accuracy = 39%, neutral accuracy= 51% and negative accuracy = 44.4%. For the other 550 input files that I didnt
use to test I got positive accuracy= 48% neutral accuracy = 59.4% and negative accuracy = 33.33333%. From these numbers, I can tell that it
is over 33% correct. Also each function was checked to work.

Efficiency: Do you think your solution is optimal (i.e., its the best solution)? If not, list the ideas that you would
have tried if you had infinite time to make the code more efficient?
No it is not. I loop through similar processes in multiple functions that could be put together. Also, I changed the negation tactic, which could remove a
lot of code. I left the original in, however, incase I wanted to experiment with making negation more accurate.

Feedback/comments: provide any feedback or comments on the lab
This was a fun lab
