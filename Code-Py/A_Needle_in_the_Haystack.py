'''
Can you find the agulha in the palheiro?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
'''

# minha solução

def find_needle(haystack): return ("found the needle at position %i" % haystack.index("needle"))