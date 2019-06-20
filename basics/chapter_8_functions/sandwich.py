# This code contains simple examples about working with modules in Python.
# Module functions

def make_sandwich(size, *items):
    '''Summarize the sandwich we are about to make.'''
    print('\nMaking a '+ str(size) + '-inch sandwich with the following items:')
    for item in items:
        print('- ' + item)
  