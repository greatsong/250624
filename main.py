import streamlit as st
import pandas as pd

st.title("2025년 5월 기준 연령별 인구 현황")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("202505_202505_연령별인구현황_월간.csv", encoding="euc-kr")
    df['행정구역'] = df['행정구역'].str.extract(r'([\uAC00-\uD7A3]+)')  # 한글 추출
    return df

df = load_data()

# 전처리
total_col = '2025년05월_계_총인구수'
age_columns = [col for col in df.columns if col.startswith('2025년05월_계_') and '세' in col]

df[total_col] = df[total_col].astype(str).str.replace(',', '', regex=False).astype(int)
df[age_columns] = df[age_columns].astype(str).apply(lambda x: x.str.replace(',', '', regex=False).astype(int))

top5 = df.nlargest(5, total_col).copy()
age_labels = [col.replace('2025년05월_계_', '') for col in age_columns]
top5.columns = list(top5.columns[:3]) + age_labels

# 연령별 인구 테이블 변환
df_chart = top5.set_index('행정구역')[age_labels].T
df_chart.index.name = '연령'
df_chart = df_chart.reset_index()

# 시각화
st.subheader("상위 5개 행정구역의 연령별 인구 분포")
st.line_chart(df_chart.set_index("연령"))

# 원본 데이터 표시
st.subheader("원본 데이터 (상위 5개 지역)")
st.dataframe(top5)
