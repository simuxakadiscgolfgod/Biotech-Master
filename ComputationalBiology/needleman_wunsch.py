#Needleman-Wunsch sequence alignment algorithm 
import numpy as np
import pandas as pd
#2 numpy matrices. one for the scores one for the "arrows".

m = 4 #match is 4
missm = -1 #missmatch is -1
gap = -2 #gap is -2

s2 = str(input("Enter the first sequence: ")).upper()
s1 = str(input("Enter the second sequence: ")).upper()

score_matrix = np.empty((len(s1)+1, len(s2)+1), dtype='i')
arrow_matrix = np.empty((len(s1)+1, len(s2)+1), dtype='object')

for i in range(len(s1)+1):
  score_matrix[i,0] = gap*i
  arrow_matrix[i,0] = "↑"

for i in range(len(s2)+1):
  score_matrix[0,i] = gap*i
  arrow_matrix[0,i] = "←"

arrow_matrix[0,0] = 0
cellvalues = []

for i in range(1, len(s1)+1):
  for j in range(1, len(s2)+1):
    if s1[i-1] == s2[j-1]:
      cellvalues.append(score_matrix[i-1,j-1] + m)
    else:
      cellvalues.append(score_matrix[i-1,j-1] + missm)

    cellvalues.append(score_matrix[i-1,j] + gap)
    cellvalues.append(score_matrix[i,j-1] + gap)

    score_matrix[i,j] = max(cellvalues)

    arrow_matrix[i,j] = cellvalues.index(max(cellvalues))

    if arrow_matrix[i,j] == 0:
      arrow_matrix[i,j] = "↖"
    elif arrow_matrix[i,j] == 1:
      arrow_matrix[i,j] = "↑"
    else:
      arrow_matrix[i,j] = "←"

    cellvalues = []

s1_names = [_ for _ in "-" + s1]
s2_names = [_ for _ in "-" + s2]

df_score = pd.DataFrame(score_matrix, index=s1_names, columns=s2_names)
df_arrow = pd.DataFrame(arrow_matrix, index=s1_names, columns=s2_names)

print("Score matrix \n", df_score, "\n")
print("Arrow matrix \n", df_arrow, "\n")

#get the alignment
topseq = ""
botseq = ""

i = len(s1)
j = len(s2)

while arrow_matrix[i,j] != 0:
  if arrow_matrix[i,j] == "↖":
    botseq = s1[i-1] + botseq
    topseq = s2[j-1] + topseq
    i -= 1
    j -= 1
  elif arrow_matrix[i,j] == "↑":
    botseq = s1[i-1] + botseq
    topseq = "-" + topseq
    i -= 1
  else:
    botseq = "-" + botseq
    topseq = s2[j-1] + topseq
    j -= 1

print("\nOptimal alignment")
print(topseq)
print(botseq)
