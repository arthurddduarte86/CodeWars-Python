<<<<<<< HEAD
#Complete the solution so that it reverses all of the words
# within the string passed in.

#Example(Input --> Output):

#"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
#
#
def reverse_words(s):
    s = s.split(" ")
    return " ".join(s[len(s)-1::-1])
#
#
#
def reverse_words(s):
    s = s.split(" ")
=======
#Complete the solution so that it reverses all of the words
# within the string passed in.

#Example(Input --> Output):

#"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
#
#
def reverse_words(s):
    s = s.split(" ")
    return " ".join(s[len(s)-1::-1])
#
#
#
def reverse_words(s):
    s = s.split(" ")
>>>>>>> refs/remotes/origin/main
    return " ".join(s[::-1])