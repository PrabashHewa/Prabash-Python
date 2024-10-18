"""
The code reads scores from a file and processes these scores by summing them for 
each contestant, and then prints the scores in alphabetical order. 
Name : Prabash 
      
"""


def read_scores(filename):
    '''Read the scores from the file and sum them up for each contestant.'''
    scores = {}
    try:
        file = open(filename, 'r')
    except:
        print("There was an error in reading the file.")
        return None

    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            print("There was an erroneous line in the file:")
            print(line.strip())
            file.close()
            return None
        name, score_str = parts
        try:
            score = int(score_str)
        except ValueError:
            print("There was an erroneous score in the file:")
            print(score_str)
            file.close()
            return None
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score

    file.close()
    return scores

def print_scores(scores):
    '''Print the scores of all contestants in alphabetical order.'''
    sorted_names = sorted(scores.keys())
    for name in sorted_names:
        print(f"{name} {scores[name]}")

def main():
    '''Function prompts the user for the filename, reads the scores, and prints them out.'''
    filename = input("Enter the name of the score file: ")
    scores = read_scores(filename)
    if scores is not None:
        print("Contestant score:")
        print_scores(scores)

if __name__ == "__main__":
    main()
