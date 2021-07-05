import sys
 
# Saving the reference of the standard output
original_stdout = sys.stdout    
 
with open('demo.txt', 'w') as f:
    sys.stdout = f 
    print('Hello, Python!')
    print('This message will be written to a file.')
    # Reset the standard output
    sys.stdout = original_stdout 
 
print('This message will be written to the screen.')
