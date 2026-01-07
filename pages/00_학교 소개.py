import streamlit as st

st.set_page_config(
    page_title="학교 소개 | 우리학교",
    page_icon="🏫",
    layout="centered"
)

st.title("🏫 우리학교 소개")
st.write("우리학교에 오신 것을 환영합니다!")

st.divider()

# 학교 개요
st.header("📌 학교 개요")
st.write("""
우리학교는 학생 중심의 교육을 바탕으로
미래 사회를 이끌어 갈 창의적인 인재를
양성하는 것을 목표로 하고 있습니다.
""")

st.divider()

# 교육 이념
st.header("🎯 교육 이념")
st.write("""
- 학생 중심 교육
- 창의적 사고 능력 함양
- 올바른 인성과 책임감 있는 시민 양성
""")

st.divider()

# 입학 전형 소개  ✅ 문제 나던 부분 완전 수정
st.header("🎓 입학 전형")
st.write("""
우리학교의 입학 전형은
학생부 중심 전형으로 진행됩니다.

학교생활기록부와 면접을 통해
학생의 잠재력과 성장 가능성을
종합적으로 평가하여 선발합니다.
""")

st.divider()

# 학교 시설
st.header("🏢 학교 시설")
st.write("""
- 최신식 교실
- 과학 실험실
- 컴퓨터실
- 도서관
- 체육관
""")

st.divider()

st.info("📞 궁금한 사항은 [문의] 페이지를 이용해주세요.")

