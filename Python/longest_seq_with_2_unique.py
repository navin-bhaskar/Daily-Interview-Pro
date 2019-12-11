"""                 Shree Krishnaya Namaha              """


def findSequence(seq):
    start_seq = 0
    end_seq = 2
    max_len = float("-inf")

    first_uniq = seq[0]
    second_uniq = seq[1]
    for idx in range(2, len(seq)):
        if seq[idx] not in (first_uniq, second_uniq):
            first_uniq, second_uniq = seq[idx-1], seq[idx]
            start_seq = idx - 1
        
        end_seq += 1

        #print (seq[start_seq:end_seq])
        max_len = max(max_len, end_seq-start_seq)


    return 0 if max_len == float("-inf") else max_len

print findSequence([1, 3, 5, 3, 1, 3, 1, 5])