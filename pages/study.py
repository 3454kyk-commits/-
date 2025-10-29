# 🌙✨ 오늘의 운세 ✨🌙
import streamlit as st
import datetime
import random
from lunardate import LunarDate


st.set_page_config(page_title="✨오늘의 사주 운세✨", page_icon="🌙", layout="centered")

st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #fff8f8 0%, #ffe8f0 100%);
    color: #2b2b2b;
    font-family: 'Pretendard', sans-serif;
}
h1, h2, h3 {
    text-align: center;
}
.big-emoji {
    font-size: 80px;
    text-align: center;
}
.center { text-align: center; }
.rank-box {
    background-color: #fff0f5;
    border-radius: 12px;
    padding: 10px;
    margin: 5px 0;
    box-shadow: 0 2px 6px rgba(255, 128, 171, 0.3);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-emoji">🌞🌙🌷</div>', unsafe_allow_html=True)
st.title("✨오늘의 사주 운세✨")
st.subheader("🌸 만세력 기반으로 보는 나의 하루 🔮")

# ----------------- 🔢 입력 -----------------
col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("💖 이름:", "")
with col2:
    birth_date = st.date_input("🎂 생일:", datetime.date(2000, 1, 1))
with col3:
    birth_hour = st.selectbox("🕐 태어난 시간:", 
        ["자(23~1시)", "축(1~3시)", "인(3~5시)", "묘(5~7시)", 
         "진(7~9시)", "사(9~11시)", "오(11~13시)", 
         "미(13~15시)", "신(15~17시)", "유(17~19시)", "술(19~21시)", "해(21~23시)"])

# ----------------- 🪄 천간·지지 데이터 -----------------
heavenly_stems = ["갑", "을", "병", "정", "무", "기", "경", "신", "임", "계"]
earthly_branches = ["자", "축", "인", "묘", "진", "사", "오", "미", "신", "유", "술", "해"]

five_elements = {
    "갑": "목", "을": "목",
    "병": "화", "정": "화",
    "무": "토", "기": "토",
    "경": "금", "신": "금",
    "임": "수", "계": "수"
}

colors = {
    "목": "💚 초록 (성장과 시작의 기운)",
    "화": "❤️ 빨강 (열정과 추진력의 기운)",
    "토": "💛 노랑 (안정과 중심의 기운)",
    "금": "🤍 하양 (정리와 판단의 기운)",
    "수": "💙 파랑 (지혜와 흐름의 기운)"
}

# ----------------- 🔮 만세력 계산 -----------------
def get_four_pillars(date):
    # 간단한 계산 방식 (정확한 천간/지지는 천문력 기반이지만, 여긴 구조 예시)
    base_date = datetime.date(1900, 1, 1)
    diff_days = (date - base_date).days
    year_stem = heavenly_stems[(date.year - 4) % 10]
    year_branch = earthly_branches[(date.year - 4) % 12]
    month_stem = heavenly_stems[(date.month + date.year) % 10]
    month_branch = earthly_branches[(date.month + 2) % 12]
    day_stem = heavenly_stems[diff_days % 10]
    day_branch = earthly_branches[diff_days % 12]
    return (year_stem, year_branch, month_stem, month_branch, day_stem, day_branch)

# ----------------- 🪞 운세 결과 -----------------
if name:
    year_s, year_b, month_s, month_b, day_s, day_b = get_four_pillars(birth_date)
    element = five_elements[day_s]
    color = colors[element]

    today = datetime.date.today()
    today_s, today_b, _, _, _, _ = get_four_pillars(today)
    today_element = five_elements[today_s]

    st.markdown("---")
    st.markdown(f"### 🌙 {name}님의 오늘의 사주 운세 🌙")
    st.markdown(f"**생년월일:** {birth_date.strftime('%Y-%m-%d')} {birth_hour}")
    st.markdown(f"**오늘:** {today.strftime('%Y-%m-%d')}")
    st.markdown(f"**당신의 일주(주된 기운):** {day_s}{day_b} ({element})")
    st.markdown(f"**오늘의 기운:** {today_s}{today_b} ({today_element})")

    # 궁합 판단 (같은 오행이면 좋음)
    if element == today_element:
        result = "🌈 오늘은 우주의 흐름이 당신 편이에요! 모든 게 자연스럽게 흘러가요."
    else:
        result = random.choice([
            "🍀 새로운 도전이 좋은 변화를 불러올 거예요.",
            "🌷 주변과 조화를 이루면 운이 들어와요.",
            "🕯 잠시 멈춰 마음의 중심을 잡아보세요."
        ])

    st.markdown("---")
    st.markdown(f"💫 **오늘의 메시지:** {result}")
    st.markdown(f"🎨 **오늘의 기운 색상:** {color}")
    st.markdown(f"🪞 **오늘의 명언:** {random.choice(['“운명은 용기 있는 자의 편이다.” – 베르길리우스', '“오늘의 기분이 내일의 운을 만든다.”', '“지금의 나를 믿는 것이 최고의 행운이다.”'])}")
    st.markdown(f"🌸 **행운 행동:** {random.choice(['따뜻한 차 마시기 ☕️', '감사한 일 세 가지 적기 ✍️', '좋아하는 향수 뿌리기 💐'])}")
    st.markdown(f"🎧 **추천 음악:** [{random.choice(['IU - Palette', '태연 - Fine', 'LUCY - Flowering', 'BIBI - 밤양갱'])}](https://www.youtube.com)")

    st.markdown("---")
    st.markdown("🪴 _별처럼 반짝이는 하루 보내요._")

# ----------------- 🌷 푸터 -----------------
st.markdown("""
<div class="center">✨ made with love by 🌙 it-girl cosmic vibes ✨</div>
""", unsafe_allow_html=True)


