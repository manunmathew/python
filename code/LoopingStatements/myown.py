if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    maxscore = max(scores)
    scores_without_max = []
    for score in scores:
        if score != maxscore:
            scores_without_max.append(score)
    runner_up = max(scores_without_max)
    print("Runner up is", runner_up)

