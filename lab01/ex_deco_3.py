AUTH = False
id = "chae"
pw = "1234"

def login():
    global AUTH

    if AUTH:
        AUTH = False
        print("로그아웃 되었습니다")
        return
    
    while id != input("ID 입력: "):
        print("없는 아이디입니다.")

    while pw != input("PW 입력: "):
        print("비밀번호가 틀렸습니다.")
      
    print("로그인 성공")
    AUTH = True

# 사용 승인 체크 데코레이터
def auth_required(func):
    
    def wrapper(*args, **kwargs):
        if AUTH == True:
            print("접근 승인")
            func(*args, **kwargs)
        else:
            print("접근 권한이 없습니다.")

    return wrapper  # 함수를 꼭 리턴해줘야 함


# 이 함수에 완성된 데코레이터를 적용해주세요.
@auth_required
def order_list():
    print("*********************")
    print("구매 리스트 출력")
    print("만두, 아이스크림, 콜라")
    print("*********************")

# 이 함수에 완성된 데코레이터를 적용해주세요.
@auth_required
def return_list():
    print("*********************")
    print("반품 리스트 출력")
    print("커피, 책")
    print("*********************")

# 이 함수에는 데코레이터를 적용하지 마세요.
def recommend_list():
    print("*********************")
    print("추천 목록 출력")
    print("참치, 라면, 피자")
    print("*********************")

while True:
    print("============================")
    if AUTH == False:
        print("[0] : 로그인")
    else:
        print("[0] : 로그아웃")
    print("[1] : 구매 리스트")
    print("[2] : 교환 반품 리스트")
    print("[3] : 오늘의 추천 상품")
    c = input("메뉴 선택: ")

    if c == "1":
        order_list()
    elif c == "2":
        return_list()
    elif c == "3":
        recommend_list()
    elif c == "0":
        login()
    else:
        break