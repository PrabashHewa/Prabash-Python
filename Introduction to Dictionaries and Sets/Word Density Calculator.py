"""
Name : Prabash 
      
"""

def main():
   
    print("Enter rows of text for word counting. Empty row to quit.")
    
    word_count = {}
    
    while True:
        text = input().strip()
        if not text:
            break
        
        words = text.split()
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    print_word_count(word_count)

def print_word_count(word_count):
    '''This fuction is printing number of words in the given sentence'''
    for word in sorted(word_count.keys()):
        print(f"{word} : {word_count[word]} times")

if __name__ == "__main__":
    main()



