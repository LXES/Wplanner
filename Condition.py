#조건생성문\
#자료형은 8*2형태의 리스트 사용
answersheet = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
#하루치를 검증한 후 일주일치를 한번에 짜는것으로 해야할까?
#우선 하루하루를 만드는데 집중해보자.

#알고리즘은 데이터를 받아와서 실행하는 단계
def algorithm():
    print(answersheet)

#업로드는 필요한 데이터를 입력하고 저장하라고 시키는 단계.

def uploadYesterday(list):
    print(list)
    print("upload")

def setting():
    #지난날 근무 업로드 단계
    yesterDay1 = list(map(int, input().split()))
    yesterDay2 = list(map(int, input().split()))
    #여기서 각 길이가 8이 되지 않으면 터트리자.
    if len(yesterDay1) != 8 or len(yesterDay2) != 8:
        print("어제의 근무일지를 다시 입력하십시오")
        return
    yesterDay = [yesterDay1, yesterDay2]
    uploadYesterday(yesterDay)
    #지난날 근무 업로드 완료

    #당일 영외활동자 리스트 만들기
    notHere = list(map(int, input().split()))