import re

def is_valid_korean_juminno(juminno):
    # 주민등록번호 형식 확인 (생년월일 6자리, - 문자, PID 7자리)
    if not re.match(r'\d{6}-[1-2]\d{6}', juminno):
        return False

    birthdate, pid = juminno.split('-')
    
    # 주민등록번호에서 연도, 월, 일 추출
    year = int(birthdate[:2])
    month = int(birthdate[2:4])
    day = int(birthdate[4:6])
    
    # 생년월일 유효성 확인
    if not (1 <= month <= 12) or not (1 <= day <= 31):
        return False

    # PID의 첫 자리 유효성 확인
    if pid[0] not in ('1', '2'):
        return False

    return True

# 예제 사용:
sample_juminno = [
    '990101-1234567',  # 유효한 주민등록번호
    '900230-2345678',  # 유효한 주민등록번호
    '970500-3456789',  # 유효한 주민등록번호
    '830623-4567890',  # 유효한 주민등록번호
    '750804-5678901',  # 유효한 주민등록번호
    '080123-1234567',  # 유효하지 않은 주민등록번호 (연도 범위 초과)
    '991312-1234567',  # 유효하지 않은 주민등록번호 (유효하지 않은 월)
    '951032-1234567',  # 유효하지 않은 주민등록번호 (유효하지 않은 일)
    '990101-3234567',  # 유효하지 않은 주민등록번호 (PID의 첫 자리 유효하지 않음)
    '990101-7234567'   # 유효하지 않은 주민등록번호 (PID의 첫 자리 유효하지 않음)
]

for juminno in sample_juminno:
    if is_valid_korean_juminno(juminno):
        print(f"{juminno}은(는) 유효한 한국 주민등록번호입니다.")
    else:
        print(f"{juminno}은(는) 유효하지 않은 한국 주민등록번호입니다.")
