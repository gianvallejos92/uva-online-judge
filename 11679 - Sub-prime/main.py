import sys

def read_line():
    line = sys.stdin.readline()
    return list(map(int, line.rstrip().split()))

def evaluate_positives(banks):
    for bank in banks:
        if int(bank) < 0:
           return 'N'
    return 'S'

if __name__ == '__main__':
    for line in sys.stdin:
        B, N = line.split()[:2]
        if B == '0' and N == '0':
            break

        banks = read_line()

        for debentures in range(int(N)):
            d, c, v = read_line()[:3]
            banks[d-1] += v * -1
            banks[c-1] += v

        
        print(evaluate_positives(banks))

    exit (0)
