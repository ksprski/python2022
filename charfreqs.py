import sys

with open(sys.argv[1], 'r', encoding='utf8') as f:
        text = f.read().lower()
        
        chars = []
        freqs = []
        # find occurrences
        for ch in text:
                if ch in chars:
                        freqs[chars.index(ch)][0] += 1
                else:
                        chars += [ch]
                        freqs += [[1, 0]]
        # sort by occurrences
        for i in range(len(freqs)):
                freqs[i][1] = round(freqs[i][0] / len(text), 4)
                for j in range(i, len(freqs)):
                        if (freqs[i][0] < freqs[j][0]):
                                chars[i], chars[j] = chars[j], chars[i]
                                freqs[i], freqs[j] = freqs[j], freqs[i]
        # calc frequencies
        for i in range(len(freqs)):
                freqs[i][1] = round(freqs[i][0] / len(text), 4)
        # show table
        for i in range(len(freqs)):
                print(f'{chars[i]}\t{freqs[i][0]}\t{freqs[i][1]}')

                #python3 charfreqs.py "alice.txt"