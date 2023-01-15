import pandas as pd

xl_file = "score.xlsx"


def excelToDf(xl_file):
    df = pd.read_excel(xl_file)  # 엑셀 파일 -> data frame

    return df


def over20():
    df = excelToDf(xl_file)
    result = df.loc[(df['midterm'] >= 20) & (df['final'] >= 20), ['sno', 'midterm', 'final']]
    print(result)


if __name__ == '__main__':
    over20()
