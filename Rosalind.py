import math
import switch
import numpy as np

#
# def f(a, b):
#     return ((a**2) + (b**2))
#
#
# print(f(3, 5))
# print(f(815, 907))
#
# s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"
# def f2(s, a, b, c, d):
#     return s[a:(b+1)] + " " + s[c:(d+1)]
#
# print(f2(s, 22, 27, 97, 102))
#
# s2 = "yrR7BkBpKFhww78Xwn8KFmspoV5exTG42t7cKAenN9YaySChrysopeleaC9kyyEqjdXPBbhySE80N46jY7BNBP9Bf5E284SLrVILwRFLXanMwFr654aSIb01tMaxnjaponensis6BmlJ5RPG9HAw9sWiOZpqBZPMb7QBR9ZJcVmZj43bWM1579IDlqK"
# print(f2(s2, 46, 56, 125, 134))
#
#
# def f3(a, b):
#     total = 0
#     for i in range(a, b + 1):
#         if (i % 2) == 1:
#             total += i
#         else:
#             continue
#     return total
#
# print(f3(100, 200))
# print(f3(4440, 8864))
#
# s3 = "We tried list and we tried dicts also we tried Zen"
# s4 = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
# def f4(s):
#     d = dict()
#     for word in s.split(" "):
#         if word in d.keys():
#             d[word] += 1
#         else:
#             d[word] = 1
#     return d
#
# dic = f4(s4)
# for key, value in dic.items():
#     print(key, value)
import switch

# # working with files
# # return a file containing all even-numbered lines from the original file
# # rosalind_ini5.txt
# fh = open("rosalind_ini5.txt", "r+")
# l = []
# for line in fh:
#     l.append(line.strip())
#
# # print(l)
#
# # f.write('Any data you want to write into file')
# result = []
# # element is a list
# i = 1
# for element in l:
#     if (i % 2) == 0:
#         result.append(element)
#     i += 1
#
# # print(result)
#
# f = open("output.txt", "w")
#
# for line in result:
#     s = str(line)
#     f.write(s + "\n")
#
# f.close()
# fh.close()

### Bioinformatics StrongHold

# 1. Counting DNA Nucleotides - Solved

# s = "AGGTAATCTTTATAGCGACGCCTACTGCACGTAATAGCAGACAGCTTTAGCTTTAAGAATACGAACCGAGGTCGAGGGCGACGGATAAGATTTCTTGACACGAAGGAAAAGAACCCCTGTAATCCAGTGTCGAGCCTCCGATGCCGGACATCGCTAGTGAGTAAATATTAGCAAAGCAGCGAGATAAACGTAACGGTGGTTTAACCCCAGTAACGCCGCTACCACCCAATCACGTCAGGCTTGGCCATTTGCTCTCCGATACGCGCGTGCAGCGTTCCAGCAACCTCCATACGTTTTCCGTATAGGAATATATAGTGCCATGGTAACCACACGCTACATTCTAGGGCAGAACGCTGCCACTACAAGAACGATAAGTGGAGACAAGTTGGGGTACCGCTTGACGACGATTACTAGGATGCAGGGTCCTTAGCATTAGCCACGGCCTACTGACATCTCATATCCCTTACGGGCTCCATTTATGGTTTGGCCGGGACCTATAGTCCAACATTTCAGGCCGTCAGAGGCCAGTCGATACTTTAGTCATCTACAAGGACCATGACGATGGTCAAACTATACGTAGCGTAAGATTGCACGCCACGTGCCGCGAGAGATAATGAGTTAACCCCCGCAAGGCATGTAACGCTTCTCACCCAATCGTCCAAGTGTTCGGCGTTCAATGACGTGTCTGCGCTATATTTTTTTGCGGCCCATACGAGAAGATTACTAGTATGTATAAGCATCAGTCGCTCTCGAGGTACAGCTCACGATAGAGGCCTGCAGAACGCAACCCGCACAAGTTTTTAGAACCACGTATTCGCACGGTTAGGGACGCGTCTATAGTATGCGCA"
#
# numA = 0
# numG = 0
# numC = 0
# numT = 0
#
# for c in s:
#     match c:
#         case "A":
#             numA += 1
#         case "G":
#             numG += 1
#         case "C":
#             numC += 1
#         case "T":
#             numT += 1
#         case _:
#             print("Nah...")
#
# print(numA, numC, numG, numT)

# 2. Transcribing DNA into RNA - Solved

# s = "GGGGGAAGTCTGTGGTATTTCAGCTTATGCGGGGTAAGGGGTACCGTGACGATCCCCAAGGCCGGCTCATACTAATGACTGCCGGGTAGGTAATTCATTACGCAATGCGGGGTACATATGCTCGTCGAATCTCGGACTGGTGTCTAGGAAGGGCGATGCTCCTTCGCTCGTCTACGTTTATACCTGCTTTATCAGGCGAGAACTGCTCGACGACCCGCACCGGGTCCCACGGGCACATGGCTTCGCATGTCGTATTTTTCTTGGTTGAGACAATCCTTGGAGTACTTTGCCGGATGGCCGAAGCGAAACCATGTGTTCCGATACGCAGGGACGTTAGCCCCACCCCCCTATTTAATGATTAAATAGAATAACGCTGTATTTAGCCGGCATAAAATCTACAGCCTTTACGCGTCCCGCTGTAACGGTATACGACGGTTGCCGCGTGAGGCTAGCACATAGCTTAGTTGAATAACGTCCTCTCATAGAAGACTGGGAAACCGCCTAAATACTGTCTAGCTGCCTAGCCGCTCCCGTTTGGAAAATAGTTCGCTACAGCGCAGCGGTGGCCCACGCCACGGGGGGAATGCAAAGGCAAGATACTACTATCCGACCTTCGCACCTGGGGATGCGGGGATGGCACAAACCAATACGTCCCCTTGTCATGATGTCCCATAAGCCCCCGCCCATTACATTTGAAAGCAGAGACTGATAGTTAAAGCCTCTAATGTGGGTAATTGTATCTGTACTGAACGTAAATGCGAATGCCGCGCGTGACATCCTTTTGGAGGATCGCTCACGGGGCATTCCAACCTCGATCGTATGACATGTACTCCGGGACTAAAGGCCCTAAAATGATATAACCGATGTGACTGATAGGTGAACAGCGTAGGATCATGCCTGTGTGCGACAAACAATTG"
# s1 = s.replace("T","U")
# print(s1)

# 3. The Secondary and Tertiary Structures of DNA - Solved
# reverse symbol of s, then take the complement

# s = "GCAGTACTAGAGAACGATGTGCGAGAAGTCTTAAATTCGTGAGGCCGTGTCCAGCTACGTTTTGATGGCTACCTCCAGGCCGGTGGTCAATGTTTAGTCTCGCCTTTCAGGCCTGACAACAAACCATAGAAGATGTTTCAAAAGGCAGCCCTAGGATACGCTCGAACGTGCCGATTTATATCAAATGTACGTATATTCACAAATTTTAAAAAGTCTCAGCGACATGTTTGGGTTAAATATCGTGGTATTTCTGTATAAGGAGTGTCGATGACTAAACAGTCATACCGCTTAAGGTGTCCTTTTCCCCCTGACGATATGCTGGCTACTCCTGGCAGTAAGAGACTTGAATTCAGCGTAAAAGATTTTCCCAGTGGGTTATGGTGACCTCCCACCTGAACTTTATGCCCGCTTACGCCTTAATTAAGGACGTGCTCGACATATAGATCTGTCTCGAATGAGCCAGAGTGTACATCACAGTAGCTGCCCTCGGATGGTCATCACCACAGCTATCATTGCACGATGGCGGTATAGCCAGATTCCGCGCCGAGTCTCAGTGGGTGCCTTCGAAGTCTCCGGGCCCGACTTATAGACAGGGTCAGATGTAAAAGGGTGAATAAACATGGATAAATCGGGGACATAAAATAAGACCAGTTAATAATTGTTTCCAGCGCATCCCCCGCGATCAGTTCGTGGGCTCAAATTTGCACGGCCATGACTCCGAAGTACGCATAGGACCTCTCTAGAGGACTTTTCCAATCCGAGTAGAGTCTTGTTTCGTAGGAATCTCCCATTTGGTATTACCGACTGGGAGTCGCTTCGGAGTTCATGGATGAAGTTTGGCCCTGGAAAGCGTGGAGTTGATAGGCACTGGAGCTATCGGTCCCTTAGCCTCGGCGCCTAGTTAACTACTCCATTTGAAATTAGTTCTATGGAAGAACGTGCTACCCTC"
# s_reverse = s[::-1]
# print(s_reverse)
# result = ""
# for c in s_reverse:
#     if c == "A":
#         c = "T"
#     elif c == "T":
#         c = "A"
#     elif c == "G":
#         c = "C"
#     else:
#         c = "G"
#     result += c
# print(result)

# 4. Rabbits and Recurrence Relations / Recursion. Fibonacci - Solved
# def Fibo(n, k):
#     """
#     Positive integers n≤40 and k≤5.
#     n is the No of month
#     k is how many pairs of rabbits each pair can produce
#     The total number of rabbit pairs that will be present after n months
#     Every pair of reproduction-age rabbits produces a litter of k rabbit pairs
#
#     This problem can be solved by drawing out a tree of rabbit population
#     """
#     # base case
#     if (n <= 2):
#         return 1
#     else:
#         return k * Fibo(n - 2, k) + Fibo(n - 1, k)
#
# print(Fibo(5, 3)) # 19
# print(Fibo(30, 4))

# 5. Mortal Fibonacci Rabbits - Unsolved
# def mortal_Fibo(n, m = 1):
#     """
#     Trial: 6, 3 => 4
#     :param n: number of months. n <= 100
#     :param m: months a rabbit lives. m <= 20
#     each pair produces exactly 1 pair of rabbit
#     :return: total number of rabbits after n months
#
#     keep track of the ages of rabbits
#     """
#     ages = [1] + [0] * (m - 1)
#     for i in range(n - 1):
#         ages = [sum(ages[1:])] + ages[:-1]
#     return sum(ages)
#
# print(mortal_Fibo(96, 19))
# print(mortal_Fibo(6, 3))

# 6. Mendel's First Law
def mendel_first(k, m, n):
    """
    Three positive integers k, m, and n, representing a population containing k+m+n organisms:
    k individuals are homozygous dominant (AA, BB) for a factor
    m are heterozygous (Aa, Bb)
    n are homozygous recessive (aa, bb)
    :return: the probability that two randomly selected mating organisms will produce an individual
    possessing a dominant allele (and thus displaying the dominant phenotype).
    Assume that any two organisms can mate
    """
    # 1 - P(no dominant allele whatsoever). Latter = P1 no dominant allele * P2 no either
    total = k + m + n
    pn = n / total
    pm = m / total
    # combination of populations, two recessive population
    twoRecess = pn * (n - 1) / (total - 1)
    twoHetero = pm * (m - 1) / (total - 1)
    heteroRecess = pn * (m / (total - 1)) + pm * (n / (total - 1))

    recessProb = twoRecess + twoHetero * 1 /4 + heteroRecess * 1 / 2
    return (1 - recessProb)

print("{:.5f}".format(mendel_first(18, 21, 26)))




