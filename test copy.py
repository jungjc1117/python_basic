print('모듈 생성 테스트를 위한 테스트 모듈 파일입니다.')

def test_print() :
    print('test print ............')

def add(n1, n2) :
    return n1+n2

pi = 3.14

print(__name__)

if __name__ == '__main__' :
    print('__name__ 변수의 값이 __main__ 일 때만 실행')
    test_print ()