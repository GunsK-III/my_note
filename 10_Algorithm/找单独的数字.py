# https://www.marscode.cn/practice/17r1q2625r7jn4?problem_id=7414004855077912620
def solution(card):
    for i in card:
        times = card.count(i)
        if times == 1:
            return int(i)
    return 0


if __name__ == "__main__":

    print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)
    print(solution([0, 1, 0, 1, 2]) == 2)

