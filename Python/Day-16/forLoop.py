scores = [10, 1, 4, 50, 45, 34]

for score in scores:
    print(score, end=" ")

squaredScores = [score**2 for score in scores]
print(*squaredScores)
