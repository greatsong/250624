import streamlit as st

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "ISTJ": ["회계사", "행정 공무원", "법무 전문가"],
    "ISFJ": ["간호사", "초등교사", "사회복지사"],
    "INFJ": ["상담가", "작가", "심리학자"],
    "INTJ": ["전략 컨설턴트", "시스템 분석가", "연구과학자"],
    "ISTP": ["엔지니어", "파일럿", "정비사"],
    "ISFP": ["디자이너", "요리사", "플로리스트"],
    "INFP": ["작가", "예술가", "심리상담사"],
    "INTP": ["데이터 분석가", "개발자", "이론물리학자"],
    "ESTP": ["영업사원", "기업가", "경찰관"],
    "ESFP": ["연예인", "이벤트 플래너", "패션 스타일리스트"],
    "ENFP": ["마케터", "작가", "인플루언서"],
    "ENTP": ["창업가", "프로덕트 매니저", "변호사"],
    "ESTJ": ["관리자", "군 간부", "프로젝트 매니저"],
    "ESFJ": ["교사", "간호사", "호텔 매니저"],
    "ENFJ": ["상담가", "리더십 코치", "교육자"],
    "ENTJ": ["CEO", "전략 기획가", "조직 관리자"]
}

# 앱 제목
st.title("💼 MBTI 기반 직업 추천기")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택해주세요:", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"🧠 {selected_mbti} 유형을 위한 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
