def below_zero(ops: list[int]) -> bool:
    balance = 0
    for op in ops:
        balance += op
        if balance < 0:
            return True
    return False


'''
TOKEN USAGE

Input: 55
Output: 796 
Total: 851
_________________

FULL RESPONSE

('Here is the Python function:\n\n```python\ndef below_zero(ops: list[int]) -> 
bool:\n    balance = 0\n    for op in ops:\n        balance += op\n        
ifbalance < 0:\n            return True\n    return False\n```\n\n### Examples:
\n```python\nprint(below_zero([1, 2, 3]))        # Output: False (balance: 1, 
3, 6)\nprint(below_zero([1, 2, -4, 5]))    # Output: True  (balance: 1, 3, -1 
-> drops below 0)\nprint(below_zero([5, -5, 2]))       # Output: False (
balance:5, 0, 2 -> reaches 0, but not below)\n```', Usage(input=55, output=530
, details={'candidatesTokenCount': 182, 'promptTokensDetails': [{'modality': 
'TEXT', 'tokenCount': 55}], 'thoughtsTokenCount': 348, 'serviceTier': 
'standard'}))

'''
