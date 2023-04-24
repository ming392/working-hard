#임의의 id 생성
import random

id_code = {}                                           
taken_course_list = []             
submit_grade = {}
archive_grade = {}
#과목코드 생성 함수
def get_course_id(id_code,course_name):
    if course_name not in id_code:
        new_id = random.randrange(10000, 99999)                   
        id_code[course_name] = new_id
        id_code[new_id] = course_name
        return id_code, new_id
    else:
        return id_code, id_code[course_name]
#입력 함수
def user_input(id_code):
    course_name = input('과목명을 입력하세요.\n')    
    id_code, course_id = get_course_id(id_code, course_name)
    credit = input('학점을 입력하세요\n')             
    gpa = input('평점을 입력하세요\n')                 
    return (course_id, int(credit), gpa)

#계산 함수
def calculate():
    for course in submit_grade:
        submit_gpa_sum += submit_grade[course][0]*submit_grade[course][1]
        submit_credit_sum += submit_grade[course][0]
    submit_gpa_sum /= submit_credit_sum

    for course in archive_grade:
        archive_gpa_sum += archive_grade[course][0]*archive_grade[course][1]
        archive_credit_sum += archive_grade[course][0]
    archive_gpa_sum /= archive_credit_sum
    return submit_credit_sum, submit_gpa_sum, archive_credit_sum, archive_gpa_sum

#평점 - 점수 변환 함수
def gpa_score(input_gpa):
    match input_gpa:
        case 'A+':
            return 4.5
        case 'A':
            return 4
        case 'B+':
            return 3.5
        case 'B':
            return 3
        case 'C+':
            return 2.5
        case 'C':
            return 2
        case 'D+':
            return 1.5
        case 'D':
            return 1
        case 'F':
            return 0

#초기 화면
while True:
    print('작업을 선택하세요.')
    print('1. 입력')
    print('2. 출력')
    print('3. 계산')

    user_value = input()
    
    if user_value == 1:                                                 #입력을 선택한 경우엔 과목명, 학점, 평점을 순서대로 입력받아야 함 그리고 이를 튜플로 저장
        input_course_id, input_credit, input_gpa = user_input(id_code)
        input_score = gpa_score(input_gpa)                                  #재수강 고려해서 이미 있는 거라면 더 높은 평점이 기록되도록 저장
        if input_course_id in archive_grade:
            if input_score > archive_grade[input_course_id][1]:
                archive_grade[input_course_id] = (input_credit, input_score)
        else:
            archive_grade[input_course_id] = (input_credit, input_score)

        if input_score > 0:
            if input_course_id in submit_grade:
                if input_score > submit_grade[input_course_id][1]:
                    submit_grade[input_course_id] = (input_credit, input_score)
                else:
                    submit_grade[input_course_id] = (input_credit, input_score)

        taken_course_list.append((input_course_id, input_credit, input_gpa))
        print("입력되었습니다.")
            
    elif user_value == 2:                                                 
       for output_course in taken_course_list:
            print('[' + str(id_code[output_course[0]]) + ']' + str(output_course[1] + '학점 : ' + str(output_course[2])))

    elif user_value == 3:                                                 
        submit_gpa_sum, archive_gpa_sum = 0.0, 0.0
        submit_credit_sum, archive_credit_sum = 0, 0
        submit_credit_sum, submit_gpa_sum, archive_credit_sum, archive_gpa_sum = calculate()
        print('제출용 : ' + str(submit_credit_sum) + '학점(gpa : ' + str(submit_gpa_sum) + ')')
        print('열람용 : ' + str(archive_credit_sum) + '학점(gpa : ' + str(archive_gpa_sum) + ')')
        break
    else:
        continue
    print('프로그램을 종료합니다.')


