import pandas as pd

xl_file = "score.xlsx"
df = pd.read_excel(xl_file)  # 엑셀 파일 -> data frame


def over20():
    result = df.loc[(df['midterm'] >= 20) & (df['final'] >= 20), ['sno', 'midterm', 'final']]
    print(result)


over20()
