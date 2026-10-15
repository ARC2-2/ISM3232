# debug_log.md
# Author: Aaron Contente

## Bug 1
Error type: Key error
File + line: week8_buggy line 12
What the error means: get_total cant find 'amount'?
What I told the duck: get_total adds all the amounts listed in records and adds them to total
What I tried: ran code after adding print(f'DEBUG: rec = {rec}')
How I fixed it: Fixed spelling in 'amount'

## Bug 2
Error type: Type error
File + line: week8_buggy line 16
What the error means: It cant print is_over_limit because 1000 is a string. Python cant compare numbers to strings using > sign
How I fixed it: deleted the '' so 1000 is an int

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes / No

## AI Literacy Reflection
Did I use AI? Yes
If yes -- exact prompt I used: When I finished I uploaded a screenshot of my work and the assignment to gemini and asked it to "check my work"
What AI explained: For bug 1 I put that the error was on line 4 because that was where the bug was. AI explained that the error occurs on line 12 because thats when the code attempts to look up a key (amount) that does not exist in line 4
What I changed myself: Changed the line from 4 to 12
Can I explain every fixed line? Yes

## What I learned
I learned how to distinguish between where an error is triggered versus where its underlying cause was written. I realized that while the typo was in the dictionary on line 4, the KeyError occurred when it actually tries and fails to retrieve that key.