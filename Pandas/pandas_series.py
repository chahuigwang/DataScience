import pandas as pd

# 딕셔너리로 시리즈 생성
dict_data = {'이름': '차희광', '성별': '남', '나이': 25}
dict_series = pd.Series(dict_data)
# print(dict_series)

# 리스트로 시리즈 생성
list_data = ['차희광', '남', 25]
list_series = pd.Series(list_data, index=['이름', '성별', '나이'])
print(list_series)

# 인덱싱
print(list_series[0])  # 0번째 행 인덱싱
print(list_series['이름'])  # '이름' 행 인덱싱
print(list_series[[0, 1]])
print(list_series[['이름', '성별']])
