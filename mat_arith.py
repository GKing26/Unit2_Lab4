# There is no need to import SAMPLE_MATRICES
# YOUR CODE AND HEADING HERE

# Griffin King
# Unit 2 Lab 4
# Making a program that can add and multiply matrix thingies

def mat_sum(m1, m2):
  if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    return [[m1[a][b]+m2[a][b] for b in range(len(m2[0]))] for a in range(len(m1))]
  return "No Solution"

def mat_mul(m1, m2):
  if len(m1[0]) == len(m2):
    m1_2 = [[' ' for b in range(len(m2[a]))] for a in range(len(m1))]
    for a in range(len(m1)):
      for b in range(len(m1[a])):
        for c in range(len(m2[b])):
          if m1_2[a][c] == ' ':
            m1_2[a][c] = m1[a][b]*m2[b][c]
          else:
            m1_2[a][c] += m1[a][b]*m2[b][c]
    print(m1_2)
    return m1_2
  return "No Solution"

# [0,1]
# [1,0]
# [2,0]

#[0,1,2,3]
#[1,0,0,0]


