import Condition
import Whole_investigation
# 메인메소드 돌릴곳
# 애자일 방법론을 따르기로 결정
# 이번엔 객체지향을 온전히 따르기로 결정
#
# 프로그램 설계
# 1. 전수검색 후 조건에 맞추어 삭제
#     -> 이때 데이터 저장과 저장형태, 속도에 대한 걸림돌 발생/
#     -> 다만 가장 쉽게 개발가능
#
# 2. 조건에 맞추어서 숫자를 넣기
#     -> 조건에 대한 자세한 이해와 다양한 경험필요
#     -> 다만 가장 쉽게 자료형 설정가능
print("a")


#알고리즘 선택하기
wayToUse = 0

#조건생성
#         wayToUse = 0
# 전수조사
#         wayToUse = 1



#실행부

#만약 조건생성일경우
if wayToUse == 0:
    #필요한 정보(이전날 근무, 영외활동자 리스트) 세팅
    Condition.setting()
    #알고리즘 실행
    Condition.algorithm()

