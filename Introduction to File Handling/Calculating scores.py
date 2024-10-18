"""
Name : Prabash 
      
"""

def read_scores(filename):
    '''ead the scores from the file and sum them up for each contestant'''
    scores = {}
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split()
            if name in scores:
                scores[name] += int(score)
            else:
                scores[name] = int(score)
    return scores

def print_scores(scores):
    ''' print the scores of all contestants in alphabetical order'''
    sorted_names = sorted(scores.keys())
    for name in sorted_names:
        print(f"{name} {scores[name]}")

def main():
    '''function prompts the user for the filename, reads the scores, and prints them out.
'''
    filename = input("Enter the name of the score file: ")
    scores = read_scores(filename)
    print("Contestant score:")
    print_scores(scores)

if __name__ == "__main__":
    main()





