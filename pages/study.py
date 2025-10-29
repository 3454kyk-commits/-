# 🌙✨ It-Girl Horoscope & Saju Today ✨🌙
import streamlit as st
import datetime
import random

# ----------------- 🎀 기본 세팅 🎀 -----------------
st.set_page_config(
    page_title="✨오늘의 별자리 & 사주 운세✨",
    page_icon="🌙",
    layout="centered"
)

st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #fff8f8 0%, #ffe8f0 100%);
    color: #2b2b2b;
    font-family: 'Pretendard', sans-serif;
}
h1, h2, h3 {
    text-align: center;
    font-family: 'Cafe24 Ssurround', cursive;
}
.big-emoji {
    font-size: 80px;
    text-align: center;
}
.center {
    text-align: center;
}
a {
    text-decoration: none;
    color: #ff4b8a;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ----------------- 🌸 헤더 -----------------
st.markdown('<div class="big-emoji">🌞🌙🌷</div>', unsafe_allow_html=True)
st.title("✨오늘의 운세 - 별자리 & 사주✨")
st.subheader("☕️ 오늘의 우주가 내게 속삭이는 메시지 💫")

# ----------------- 🌈 입력 -----------------
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("💖 이름을 알려줘:", "")
with col2:
    birthday = st.date_input("🎂 생일을 선택해줘:", datetime.date(2000, 1, 1))

# ----------------- 🌟 별자리 계산 -----------------
zodiac_signs = {
    (120, 218): "♒️ 물병자리",
    (219, 320): "♓️ 물고기자리",
    (321, 419): "♈️ 양자리",
    (420, 520): "♉️ 황소자리",
    (521, 620): "♊️ 쌍둥이자리",
    (621, 722): "♋️ 게자리",
    (723, 822): "♌️ 사자자리",
    (823, 922): "♍️ 처녀자리",
    (923, 1022): "♎️ 천칭자리",
    (1023, 1121): "♏️ 전갈자리",
    (1122, 1221): "♐️ 사수자리",
    (1222, 119): "♑️ 염소자리"
}

def get_zodiac(month, day):
    md = month * 100 + day
    for (start, end), sign in zodiac_signs.items():
        if start <= md <= end or (start > end and (md >= start or md <= end)):
            return sign
    return "🌌 알 수 없음"

# ----------------- 🔮 운세 메시지 -----------------
love = ["💘 사랑이 피어나는 하루예요", "💞 달콤한 눈빛 교환이 있을지도 몰라요", "💋 사랑의 기운이 당신을 감싸요"]
work = ["💼 새로운 아이디어가 샘솟아요", "🌟 집중력이 최고예요", "📈 당신의 노력이 드러나는 날이에요"]
fortune = ["🍀 작은 행운이 속삭여요", "🌈 우연한 기쁨이 찾아올 거예요", "🦋 좋은 소식이 멀지 않았어요"]
mood = ["☕️ 차분하고 안정적인 하루", "🌷 마음이 따뜻해지는 순간이 많아요", "🎀 스스로에게 부드럽게 대해요"]

# ----------------- 🎧 추천 음악 목록 -----------------
music_recs = [
    ("🌼 IU - Love wins all", "https://www.youtube.com/watch?v=oxKCPjcvbys"),
    ("🌙 NewJeans - Super Shy", "https://www.youtube.com/watch?v=ArmDp-zijuc"),
    ("🍓 TAEYEON - Weekend", "https://www.youtube.com/watch?v=QUHy3VbK1lM"),
    ("🌊 Crush - 나빠 (NAPPA)", "https://www.youtube.com/watch?v=QYNwbZHmh8g"),
    ("🌹 LUCY - Flowering", "https://www.youtube.com/watch?v=dvwK2_5Wq0A"),
    ("☁️ DPR LIVE - Jasmine", "https://www.youtube.com/watch?v=6oT2n1i3qWw"),
    ("✨ Red Velvet - Feel My Rhythm", "https://www.youtube.com/watch?v=R9At2ICm4LQ"),
    ("💫 BIBI - 나쁜년 (BIBI Vengeance)", "https://www.youtube.com/watch?v=JZoFqIxlbk0")
]

# ----------------- 🌷 운세 생성 -----------------
if name:
    zodiac = get_zodiac(birthday.month, birthday.day)
    today_seed = int(birthday.strftime("%m%d")) + datetime.date.today().toordinal()
    random.seed(today_seed)

    st.markdown("---")
    st.markdown(f"### 🌙 {name}님의 오늘의 운세 🌙")
    st.markdown(f"**별자리:** {zodiac}")
    st.markdown("---")

    st.markdown(f"💘 **사랑운:** {random.choice(love)}")
    st.markdown(f"💼 **일/공부운:** {random.choice(work)}")
    st.markdown(f"🍀 **행운운:** {random.choice(fortune)}")
    st.markdown(f"🕯 **기분:** {random.choice(mood)}")

    st.markdown("---")
    st.markdown("🌸 **오늘의 한 줄 메시지** 🌸")
    st.markdown(f"✨ *'{random.choice(['우주는 오늘도 당신을 응원해요 🌌', '자신을 믿는 게 최고의 부적이에요 💖', '당신의 페이스로 천천히 가요 ☕️'])}'*")

    st.markdown("---")
    music = random.choice(music_recs)
    st.markdown(f"🎧 **오늘의 추천 음악:** [{music[0]}]({music[1]})")

    st.markdown("🪞 _별처럼 반짝이는 하루 보내요._")

# ----------------- 🌷 푸터 -----------------
st.markdown("""
<div class="center">✨ made with love by 🌙 it-girl cosmic vibes ✨</div>
""", unsafe_allow_html=True)
