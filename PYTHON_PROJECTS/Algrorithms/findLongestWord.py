# Function to print the longest
# word in given sentence
s = str(input('type a sentence: '))


def largestWord(s):
  
    # Sort the words in increasing
    # order of their lengths
    s = sorted(s, key = len)
  
    # Print last word
    print(s[-1])
  
  
# Driver Code
if __name__ == "__main__":
  
    # Given string
    
  
    # Split the string into words
    l = list(s.split(" "))
  
    largestWord(l)