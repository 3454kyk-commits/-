import streamlit as st
import time
import base64

# 🌸 페이지 기본 설정
st.set_page_config(page_title="BloomFocus 🌱", page_icon="🌼", layout="centered")

# 🎵 로파이 사운드 임베드 (YouTube or mp3 링크 가능)
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    md = f"""
        <audio controls autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

# 🌿 헤더
st.markdown("""
<h1 style='text-align:center; color:#6B8E23;'>🌷 BloomFocus 🌷</h1>
<p style='text-align:center; color:#808080;'>
공부할수록 나의 식물이 자라나요 🌱<br>힐링과 집중을 동시에 💫
</p>
""", unsafe_allow_html=True)

# 🌼 식물 선택
plant = st.selectbox(
    "키우고 싶은 식물을 선택하세요 🌿",
    ["🌱 새싹", "🌵 선인장", "🌼 해바라기", "🌸 벚꽃나무", "🌾 라벤더"]
)

# ⏳ 포모도로 설정
st.markdown("### 🍅 포모도로 모드 설정")
focus_time = st.slider("집중 시간 (분)", 5, 60, 25)
break_time = st.slider("휴식 시간 (분)", 1, 15, 5)
cycles = st.number_input("반복 횟수 🔁", 1, 8, 2)

start = st.button("🌿 집중 시작하기")

# 🎵 사운드 파일 경로
# 👉 mp3 파일 이름을 바꿔서 로컬에 두면 됨. (예: 'lofi.mp3')
sound_file = "lofi.mp3"

if start:
    st.write(f"🎧 로파이 사운드 재생 중... 집중 모드로 들어갑니다 🌙")
    autoplay_audio(sound_file)

    progress_bar = st.progress(0)
    stage_text = st.empty()
    status_text = st.empty()

    total_cycles = cycles
    for cycle in range(total_cycles):
        st.markdown(f"## 🌸 {cycle+1}번째 사이클 시작 🌸")
        
        # 🌿 공부 시간
        for sec in range(focus_time * 60):
            progress = (sec + 1) / (focus_time * 60)
            progress_bar.progress(progress)
            if progress < 0.33:
                stage_text.markdown("<h2 style='text-align:center;'>🌱 새싹이 자라나요...</h2>", unsafe_allow_html=True)
            elif progress < 0.66:
                stage_text.markdown("<h2 style='text-align:center;'>🌿 줄기가 자라나요...</h2>", unsafe_allow_html=True)
            else:
                stage_text.markdown("<h2 style='text-align:center;'>🌳 꽃이 피어나요!</h2>", unsafe_allow_html=True)
            status_text.text(f"집중 중... {int(progress*100)}% 완료 ⏳")
            time.sleep(1)
        
        st.success(f"🎉 {plant}가 한 단계 성장했어요! 잠시 휴식해요 🍵")

        # ☕ 휴식 시간
        for sec in range(break_time * 60):
            progress = (sec + 1) / (break_time * 60)
            progress_bar.progress(progress)
            stage_text.markdown("<h2 style='text-align:center;'>🍵 휴식 중... 🌿</h2>", unsafe_allow_html=True)
            status_text.text(f"휴식 {int(progress*100)}% 진행 중 💤")
            time.sleep(1)

    st.balloons()
    st.success(f"🌺 축하해요! {plant}가 완전히 성장했어요 💪✨")

# 🌈 푸터
st.markdown("""
<hr>
<p style='text-align:center; color:#A9A9A9;'>
🌿 created with ❤️ by 니야 | keep blooming, keep growing 🌸
</p>
""", unsafe_allow_html=True)
