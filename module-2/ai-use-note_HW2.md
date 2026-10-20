**Assignment:**

***Pt 1***


**Prediction, written before I asked for anything** (the page tells you what to predict):
I predicted for n = 2, x = 0l5 that we would get -0.125

**What I asked the agent for** (one line per request):I asked the agent to help me wrtie the loop. It got confused as to whether part 1 or 2 was meant to be done by hand and so didn't write any code for me at all though so I wrote the loop

**What I changed by hand:** the loop 

**One "why" I asked, and the answer in my own words:** Why would a recursive function that calls itself be so slow for n = 3501
ans: every value would get recomputed over and over

**What the agent got wrong, and how I found out** (if nothing, say what check you ran that would have caught it):
It thought that Pt 1 was the no AI policy and so didnt write a loop for me but it is actually the start of pt 2 that has no AI

**What I still do not understand:**
I dont understand taylor series well



***Pt 2***
**Prediction, written before I asked for anything** (the page tells you what to predict):
The grid for n = 4:
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16

The nested loop:
for i in range(1,5):
    row = []
    for j in range(1,5):
        row.append(i * j)
    print(row)

calc the width of the largest string (n*n)
yes this was correct

**What I asked the agent for** (one line per request):

look at my multitab.py doc and let me know if I should change anything to make it neater or match the output wanted for task 2 HW2

**What I changed by hand:** 
I wrote the loop by myself and claude would not make it neat for me so I also added code to calculate length of longest string and then allign the numbers nicely

**One "why" I asked, and the answer in my own words:** 
what does print(..., end='') do?
It adds a line after the ... (whatever you want to print)


**What the agent got wrong, and how I found out** (if nothing, say what check you ran that would have caught it):
The agent refused to write any actual code for me

**What I still do not understand:**
I hadn't seen this product table before so this is new for me



***EXTRA CREDIT***
Git is forked, here is the repo: https://github.com/rabbittibbar10/astr119-fall2026/tree/main/module-2