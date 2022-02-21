score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
    #TODO
    sum = 0
    avg = 0
    for i in range(5):
        for j in range(2):
            sum += score[i][j]
            avg = sum / 2
        print(f"{i+1}번, 평균 : {avg}")

get_avg(score)
