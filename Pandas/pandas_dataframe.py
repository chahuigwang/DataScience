import pandas as pd

# 데이터 프레임 생성
df = pd.DataFrame([['차희광', '남', 25], ['김여자', '여', 20]],
                  index=[1, 2],
                  columns=['이름', '성별', '나이'])
print(df)

# 행, 열 바꾸기
# df = df.transpose()
# print(df)

# 인덱싱
print(df.iloc[0])  # 0번째 행 인덱싱
print(df.loc[1])  # '1' 행 인덱싱
