#이메일주소체크.py

import re

# 수정된 정규식 패턴 (이메일 주소 검사)
# r (raw string notation)

# 이메일 주소를 검증하기 위한 정규식 패턴
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[a-zA-Z]*$'
# [a-zA-Z0-9._%+-]+: @ 앞의 로컬 파트에 해당하는 부분. 영문 대/소문자, 숫자, 특수문자 중 하나 이상의 문자가 올 수 있습니다.
# @: 이메일 주소의 중간에는 반드시 "@" 기호가 와야 합니다.
# [a-zA-Z0-9.-]+: @ 뒤의 도메인 파트에 해당하는 부분. 영문 대/소문자, 숫자, 하이픈, 마침표 중 하나 이상의 문자가 올 수 있습니다.
# \.: 도메인 파트와 최상위 도메인을 구분하는 마침표입니다.
# [a-zA-Z]{2,}[a-zA-Z]*$: 최상위 도메인 부분. 최소 2개 이상의 영문 대/소문자로 시작하며, 그 뒤에 영문 대/소문자가 0개 이상 올 수 있습니다.

# 10개의 샘플 이메일 주소
sample_emails = [
    'john.doe@example.com',
    'jane.doe12345@gmail.com',
    'user@subdomain.example.co.uk',
    'user.name@example.org',
    'alice@example',
    'invalid-email',
    'user@.com',
    '@example.com',
    'user@example..com',
    'user@.example.co.uk',
]

# 각 이메일 주소를 패턴과 비교
for email in sample_emails:
    if re.search(email_pattern, email):
        print(f'{email} 는 유효한 이메일 주소입니다.')
    else:
        print(f'{email} 는 유효하지 않은 이메일 주소입니다.')


