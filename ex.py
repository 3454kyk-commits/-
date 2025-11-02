# streamlit_youth_simulator.py
"""
청소년기 시뮬레이터 게임 (Streamlit Single-file)
설명:
- 성별 선택 후 진행
- 대화(메시지) 형태로 선택지를 보여주고, 선택에 따라 스탯(정신건강, 육체건강, 위험행동)이 변경
- 특정 위험 메시지(마약, 도박, 학교폭력 등)가 오고 Yes/No 선택으로 엔딩 분기
- 최종 화면에 상담센터 / 교육자료 안내(운영자는 실제 기관 문서를 연결할 수 있음)

실행:
$ pip install streamlit
$ streamlit run streamlit_youth_simulator.py

Github에 올리는 방법 요약 (로컬):
1. git init
2. git add streamlit_youth_simulator.py
3. git commit -m "Add youth simulator app"
4. Create repo on GitHub and push

이 파일은 교육/데모용이며 실제 상담·의료 대응을 대신하지 않습니다.
"""

import streamlit as st
import random
import json
from dataclasses import dataclass, asdict

# -------------------- Scenario data --------------------
# 각 시나리오는: id, text, choices: list of {text, effects:{stat:delta}, message_tags:[]}
# message_tags는 위험 메시지(예: 'drugs', 'gamble', 'bully')를 포함할 수 있음

SCENARIOS = [
    {
        "id": "start",
        "text": "새 학기가 시작되었어. 반에 적응해야 해. 친구가 먼저 말을 걸어왔어. '같이 점심 먹을래?'",
        "choices": [
            {"text": "응 고마워!", "effects": {"mental": +2, "physical": +1, "risk": 0}, "tags": []},
            {"text": "아니, 혼자 먹을래.", "effects": {"mental": -1, "physical": 0, "risk": 0}, "tags": []}
        ]
    },
    {
        "id": "study_pressure",
        "text": "시험 기간이 다가와. 공부를 더 해야 할까?"
        ,"choices":[
            {"text":"열심히 공부할래. 밤샘도 해볼까.", "effects": {"mental": -2, "physical": -2, "risk": 0}, "tags": []},
            {"text":"조금만 하고 쉴래.", "effects": {"mental": +1, "physical": +1, "risk": 0}, "tags": []}
        ]
    },
    {
        "id": "party_offer",
        "text": "친구에게서 파티 초대 메시지가 왔어. 여기서 뭔가를 권유받을 수 있어.",
        "choices":[
            {"text":"갈래, 재밌겠다.", "effects": {"mental": +1, "physical": -1, "risk": +1}, "tags": ["drugs"]},
            {"text":"가지 않을래.", "effects": {"mental": 0, "physical": 0, "risk": 0}, "tags": []}
        ]
    },
    {
        "id": "loan_message",
        "text": "모르는 번호로 '빠른 돈 벌이, 소액 대출 필요?' 라는 메시지가 왔어.",
        "choices":[
            {"text":"연결해볼래 (Yes)", "effects": {"mental": -2, "physical": 0, "risk": +2}, "tags":["gamble"]},
            {"text":"무시할래 (No)", "effects": {"mental": +0, "physical": 0, "risk": 0}, "tags": []}
        ]
    },
    {
        "id": "bully_event",
        "text": "같은 반 친구가 온라인에서 너를 놀리는 글을 올렸어.",
        "choices":[
            {"text":"맞대응 한다.", "effects": {"mental": -2, "physical": 0, "risk": +1}, "tags":["bully"]},
            {"text":"증거를 모아 상담선생님에게 말한다.", "effects": {"mental": +1, "physical": 0, "risk": -1}, "tags": []}
        ]
    }
]

# 추가 위험 메시지(랜덤으로 발송)
RISK_MESSAGES = [
    {"id":"msg_drug","text":"[친구] 야, 이거 해볼래? 엄청 재밌어. 네가 스트레스도 풀린다네. Yes/No","tag":"drugs"},
    {"id":"msg_gamble","text":"[채팅방] 소액 베팅으로 대박! 관심 있으면 'Yes'라고 해'","tag":"gamble"},
    {"id":"msg_bully","text":"[알수없는번호] 네 비밀 사진 유출할게. 돈 내, 안내면... Yes/No","tag":"extortion"}
]

# -------------------- Data classes --------------------
@dataclass
class Player:
    name: str = "플레이어"
    gender: str = "other"
    mental: int = 50
    physical: int = 50
    risk: int = 0
    choices_history: list = None
    messages_seen: int = 0

    def __post_init__(self):
        if self.choices_history is None:
            self.choices_history = []

# -------------------- Utility functions --------------------

def clamp(x, a=0, b=100):
    return max(a, min(b, x))


def apply_effects(player: Player, effects: dict):
    player.mental = clamp(player.mental + effects.get('mental', 0))
    player.physical = clamp(player.physical + effects.get('physical', 0))
    player.risk = max(0, player.risk + effects.get('risk', 0))


def random_risk_message():
    # 30% 확률로 위험 메시지 발생
    if random.random() < 0.3:
        return random.choice(RISK_MESSAGES)
    return None


# -------------------- Streamlit UI --------------------

st.set_page_config(page_title="청소년 시뮬레이터: 생명 존중", layout="centered")

if 'player' not in st.session_state:
    st.session_state.player = Player()
    st.session_state.step = 0
    st.session_state.ended = False
    st.session_state.end_reason = None

# --- 사이드바: 스탯 표시 ---
with st.sidebar:
    st.header("플레이어 스탯")
    p = st.session_state.player
    st.write(f"이름: {p.name}")
    st.write(f"성별: {p.gender}")
    st.progress(p.mental/100)
    st.caption("정신건강")
    st.progress(p.physical/100)
    st.caption("육체건강")
    st.write(f"위험 점수: {p.risk}")
    st.caption("위험 행동 가능성")

# --- 시작 화면 ---
if st.session_state.step == 0:
    st.title("청소년기 시뮬레이터 — 생명 존중")
    st.markdown("간단한 선택으로 청소년기의 여러 상황을 경험해보고, 선택이 어떤 결과를 낳는지 알아보세요.")
    name = st.text_input("이름을 입력하세요", value=st.session_state.player.name)
    gender = st.radio("성별 선택", options=["여자","남자","기타"], index=2)
    if st.button("게임 시작"):
        st.session_state.player.name = name
        st.session_state.player.gender = gender
        st.session_state.step = 1
        st.experimental_rerun()

# --- 메인 게임 루프 ---
if 1 <= st.session_state.step <= 10 and not st.session_state.ended:
    idx = (st.session_state.step - 1) % len(SCENARIOS)
    scenario = SCENARIOS[idx]
    st.subheader(f"상황 {st.session_state.step}:")
    st.write(scenario['text'])

    cols = st.columns(len(scenario['choices']))
    for i, choice in enumerate(scenario['choices']):
        if cols[i].button(choice['text']):
            apply_effects(st.session_state.player, choice['effects'])
            st.session_state.player.choices_history.append((scenario['id'], choice['text']))
            # 메시지 태그 대응: 위험 태그가 있으면 위험 카운트 증가
            for tag in choice.get('tags', []):
                if tag in ['drugs','gamble','bully','extortion']:
                    st.session_state.player.messages_seen += 1
            st.session_state.step += 1
            st.experimental_rerun()

    # 랜덤 위험 메시지 삽입
    if 'pending_message' not in st.session_state or st.session_state.pending_message is None:
        msg = random_risk_message()
        st.session_state.pending_message = msg

    if st.session_state.pending_message:
        st.markdown("---")
        st.warning("새로운 메시지가 도착했습니다:")
        st.info(st.session_state.pending_message['text'])
        if st.button("Yes", key=f"yes_{st.session_state.step}"):
            tag = st.session_state.pending_message['tag']
            # 위험 응답: 큰 위험도 증가, 정신건강 하락
            if tag == 'drugs':
                apply_effects(st.session_state.player, {'mental': -5, 'physical': -5, 'risk': +3})
            elif tag == 'gamble':
                apply_effects(st.session_state.player, {'mental': -3, 'risk': +3})
            elif tag == 'extortion':
                apply_effects(st.session_state.player, {'mental': -6, 'risk': +4})
            st.session_state.player.choices_history.append(('message_'+tag, 'Yes'))
            st.session_state.pending_message = None
            st.experimental_rerun()
        if st.button("No", key=f"no_{st.session_state.step}"):
            st.session_state.player.choices_history.append(('message', 'No'))
            st.session_state.pending_message = None
            st.experimental_rerun()


# --- 엔딩 조건 체크 ---
# 간단한 규칙: 정신건강 <= 15 -> 우울/자살 위험 엔딩
# risk >= 6 -> 마약/도박/위협 엔딩
# otherwise 긍정 엔딩

if not st.session_state.ended:
    p = st.session_state.player
    if p.mental <= 15:
        st.session_state.ended = True
        st.session_state.end_reason = 'depression'
    elif p.risk >= 6:
        st.session_state.ended = True
        st.session_state.end_reason = 'risk_path'
    elif st.session_state.step > 10:
        st.session_state.ended = True
        st.session_state.end_reason = 'neutral'

# --- 엔딩 페이지 ---
if st.session_state.ended:
    st.markdown("# 엔딩")
    reason = st.session_state.end_reason
    if reason == 'depression':
        st.error("결과: 우울증/자살 위험 엔딩")
        st.write("당신의 선택은 정신건강에 큰 손상을 주었습니다. 이런 상황에 놓였을 때는 즉시 도움을 요청해야 합니다.")
    elif reason == 'risk_path':
        st.warning("결과: 위험 행동(마약/도박/갈취) 엔딩")
        st.write("위험한 선택들이 쌓여 문제로 이어졌습니다. 주변의 안전한 성인이나 전문 기관에 도움을 받으세요.")
    else:
        st.success("결과: 회복/중립 엔딩")
        st.write("여러 선택 중 일부는 긍정적 영향을 주었습니다. 계속해서 자기돌봄을 해나가세요.")

    st.markdown("---")
    st.subheader("선택 기록")
    for i, ch in enumerate(st.session_state.player.choices_history[-20:]):
        st.write(f"{i+1}. 상황: {ch[0]} → 선택: {ch[1]}")

    st.markdown("---")
    st.subheader("도움 받을 수 있는 기관 및 자료(샘플)")
    st.write("• 24시간 자살예방 상담: 국번없이 1393 (한국, 예시)")
    st.write("• 청소년 상담전화: 1388 (한국, 예시)")
    st.write("• 지역 보건소 정신건강 복지센터 방문 권장")
    st.write("")

    st.subheader("관련 자료(운영자가 실제 문서로 교체하세요)")
    st.markdown("- 청소년 정신건강 및 자살 통계 보고서\n- 마약류 사용과 청소년 정신건강 연구자료\n- WHO: Suicide prevention 및 Adolescent mental health 팩트시트")

    st.info("이 게임은 도움을 권장하고, 심각한 증상이 있다면 전문기관을 꼭 이용하세요.")

    if st.button("다시하기"):
        st.session_state.player = Player()
        st.session_state.step = 0
        st.session_state.ended = False
        st.session_state.end_reason = None
        st.experimental_rerun()

# -------------------- 끝 --------------------

# 추가 개발 아이디어 (주석으로 남겨둠):
# - 시나리오를 JSON 파일로 분리해서 관리
# - 그래픽/애니메이션 추가 (Streamlit-AgGrid나 HTML/CSS)
# - 선택 기반 분기 맵 시각화
# - 실제 상담/자료 링크를 관리자 페이지에서 편집 가능하게 하기
