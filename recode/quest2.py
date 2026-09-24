def passing_score(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed
print(passing_score([49, 50, 80, 65]))