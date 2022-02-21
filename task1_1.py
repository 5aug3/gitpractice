num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list): #홀수 리스트 선언
    odd_num = []
    for i in num_list:
        if i % 2 == 1:
            odd_num.append(i) #홀수 리스트 요소 추가
        else: pass
    return  odd_num
     
print(get_odd_num(num_list)) #반환값 출력