# 🌙✨ It-Girl Cosmic Fortune ✨🌙
import streamlit as st
import datetime
import random

# ----------------- 🎀 기본 세팅 🎀 -----------------
st.set_page_config(
    page_title="✨오늘의 별자리 운세✨",
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
.rank-box {
    background-color: #fff0f5;
    border-radius: 12px;
    padding: 12px;
    margin: 6px 0;
    box-shadow: 0 2px 6px rgba(255, 128, 171, 0.3);
}
</style>
""", unsafe_allow_html=True)

# ----------------- 🌸 헤더 -----------------
st.markdown('<div class="big-emoji">🌞🌙🌷</div>', unsafe_allow_html=True)
st.title("✨오늘의 잇걸 운세✨")
st.subheader("💖 별자리 · 사주 · 명언 · 행운의 행동 💫")

# ----------------- 🌈 입력 -----------------
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("💋 이름을 알려줘:", "")
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

# ----------------- 🔮 운세 데이터 -----------------
love = ["💘 사랑이 피어나는 하루예요", "💞 새로운 인연이 다가올지도 몰라요", "💋 따뜻한 대화가 행운을 불러요"]
work = ["💼 집중력이 최고예요", "🌟 당신의 아이디어가 주목받아요", "📈 꾸준함이 큰 결과를 가져와요"]
fortune = ["🍀 작은 행운이 속삭여요", "🌈 좋은 기운이 당신 곁에 있어요", "🦋 예상 못한 기쁨이 찾아와요"]
mood = ["☕️ 따뜻하고 안정적인 하루", "🌷 자신에게 부드럽게 대해요", "🎀 감정의 균형이 조화를 이루어요"]

quotes = [
    "💬 *“오늘의 당신은 어제보다 더 빛나요.”* – 익명",
    "🌙 *“행운은 준비된 마음에 온다.”* – 루이 파스퇴르",
    "🌸 *“자신을 사랑하는 것이 모든 행복의 시작이다.”* – 루시 메이",
    "🪞 *“완벽하지 않아도 괜찮아, 이미 충분히 아름다워.”*",
    "🌷 *“하루를 바꾸면 인생이 달라진다.”* – 로빈 샤르마"
]

lucky_actions = [
    "🍓 딸기우유 마시기",
    "💌 좋아하는 사람에게 안부 인사하기",
    "🕯 향초 켜놓고 10분 명상하기",
    "📖 책 한 장만이라도 읽기",
    "🌿 산책하면서 하늘 보기",
    "🎧 노래 한 곡 전부 들으면서 휴대폰 내려놓기",
    "☕️ 오늘 하루 감사한 일 3가지 떠올리기"
]

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

# ----------------- 🪞 운세 생성 -----------------
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
    st.markdown(f"🪞 **오늘의 명언**\n{random.choice(quotes)}")
    st.markdown(f"🎧 **오늘의 추천 음악:** [{random.choice(music_recs)[0]}]({random.choice(music_recs)[1]})")
    st.markdown(f"🌸 **오늘의 행운 행동:** {random.choice(lucky_actions)}")

    st.markdown("---")

    # ----------------- 🌟 별자리 운세 랭킹 -----------------
    st.markdown("## 🌟 오늘의 별자리 TOP 3 🌟")
    all_zodiacs = list(zodiac_signs.values())
    random.shuffle(all_zodiacs)
    ranks = all_zodiacs[:3]
    for i, sign in enumerate(ranks, 1):
        st.markdown(f"""
        <div class='rank-box'>
            <h4>{i}위 ✨ {sign}</h4>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("🪴 _별처럼 반짝이는 하루 보내요._")

# ----------------- 🌷 푸터 -----------------
st.markdown("""
<div class="center">✨ made with love by 🌙 it-girl cosmic vibes ✨</div>
""", unsafe_allow_html=True)
