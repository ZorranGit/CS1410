import os

def fileToList(filename):
    em_list = []
    if os.path.exists(filename):
        file = open(filename, "r")
        lines = file.readlines()
        lines = [x.strip() for x in lines]
        file.close()
        return lines
    else:
        return em_list
    
def returnFirstString(strings):
    em_string = ""
    if not strings:
        return em_string
    else:
        return strings[0]

def strandsAreNotEmpty(strand1,strand2):
    if strand1 and strand2:
        return True

def strandsAreEqualLengths(strand1, strand2):
    if len(strand1) == len(strand2):
        return True

def candidateOverlapsTarget(target,candidate,overlap):
    candboi=candidate[:overlap]
    if target[overlap*-1:] == candboi:
        return True
    else:
        return False

def findLargestOverlap(target, candidate):
    if not target and not candidate:
        return -1
    if len(target) != len(candidate):
        return -1
    length = len(target)
    overlap = 0
    for x in range(length):
        if target[length - x - 1: length] == candidate[0: x + 1]:
            overlap = x + 1
    if not overlap:
        return (0)
    else:
        return overlap

def findBestCandidate(target, string):
    overlap = []
    for x in range(len(string)):
        overlap.append(findLargestOverlap(target, string[x]))
    best_cand_length = max(overlap)
    best_cand = overlap.index(best_cand_length)
    if overlap[best_cand] == 0:
        return ('', 0)
    return (string[best_cand], overlap[best_cand])

def joinTwoStrands(target, candidate, overlap):
    string=''
    lenboi=len(target)
    new_target=target[0: lenboi - overlap]
    new_candidate=candidate[0: lenboi]
    string=new_target+new_candidate
    return string

def main ():
    target_file = input('Target strand file name: ')
    candidate_file = input('Candidate strands file name: ')
    target_file_list = fileToList(target_file)
    candidate_file_list = fileToList(candidate_file)
    target=returnFirstString(target_file_list)
    overlap=findBestCandidate(target, candidate_file_list)
    finished = joinTwoStrands(target,overlap[0], overlap[1])
    print(finished)

if __name__ == '__main__':
    main()
    
