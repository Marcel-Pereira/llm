
> # Quick note
> The Gemini 3.8 Flash model was having a server error with high demand of requests, so I used Gemini 3.6 Flash (3.7 was also having high request). \
> Both versions of requests were done with the same model.

# Questions

## Which version's code is correct?

The final code for both versions are correct and do what was asked to do, and the logic in both is identical, with the only difference being a variable name, and a docstring explaining what the code does.

## Which version's code is cleaner / simpler / easier to read?

I belive that the step-by-step version is better to read, because it generated a docstring that explains what the function is doing, which the full prompt version didn't do. \
The variable naming in the step-by-step version is also better, but this is because of the way that the function was described in each version was different.

## Did the step-by-step run show any signs of the model guessing wrong or making assumptions before all the information was in?

This stepwise version assumed many characteristics of the code during the process. \
After the first prompt, the model didn't know the input type, so it assumed it was list[float] and a parameter name "operations". \
After prompt 2, it changed to list[int] and renamed the parameter to "transactions". \
It also imported a library called "accumulate" at some point, which was never intended.

# Token Usage

## Full Prompt

Input: 55 \
Output: 796 \
Total: 851

## Step-by-Step prompts

### Prompt 1

Input: 20    
Output: 1040  
Total: 1060

### Prompt 2 
input: 1073  
output: 769   
total: 1842

### Prompt 3
input: 1851  
output: 591   
total: 2442

### Prompt 4 
input: 2458  
output: 448   
total: 2906

### TOTAL    
input: 5402  
output: 2848  
total: 8250

## Reflection

As we can see, the full prompt version used much much less tokens than the step-by-step version. This is because the step-by-step version is always uploading the whole conversation as tokens in the context window, making the total number of tokens accumulate with each request. 

The total token usage for the full prompt version was 851, while the total usage for the step-by-step was 8250, approximately 10 times more.