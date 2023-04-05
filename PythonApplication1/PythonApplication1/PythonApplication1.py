#변수 정의
archive_credit, submit_credit = 0, 0
archive_gpa, submit_gpa = 0, 0
gpa_sum = 0.0

#학점 변환 함수
def credit(gpa):
    global gpa_sum
    match gpa:
        case 'A+':
            gpa_sum = 4.5
        case 'A':
            gpa_sum = 4.0
        case 'B+':
            gpa_sum = 3.5
        case 'B':
            gpa_sum = 3.0
        case 'C+':
            gpa_sum = 2.5
        case 'C':
            gpa_sum = 2.0
        case 'D+':
            gpa_sum = 1.5
        case 'D':
            gpa_sum = 1.0
        case 'F':
            gpa_sum = 0.0
            
            

#입력
while True:
    print('작업을 선택하세요.')
    print('1. 입력')
    print('2. 계산')
    
    user_value = input()
    value = int(user_value)
    if value == 1:
        score = input('학점을 입력하세요.')
        hak_jum = int(score)
        gpa = input('평점을 입력하세요.')
        credit(gpa)
        print(gpa_sum)
        archive_credit += hak_jum
        archive_gpa += gpa_sum * hak_jum
        
        if gpa_sum != 0.0:
           
            submit_credit += hak_jum
            submit_gpa += gpa_sum*hak_jum
            
        print('입력되었습니다.\n')

    if value == 2:
        submitation_1 = submit_gpa/submit_credit
        submitation_2 = archive_gpa/archive_credit
        print('제출용 : '+ str(submit_credit)+ '(gpa :' + str(round(submitation_1, 2)) + ')')
        print('열람용 : '+ str(archive_credit)+ '(gpa :' + str(round(submitation_2, 2)) + ')')
        break

        


