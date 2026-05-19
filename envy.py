import streamlit as st
import streamlit.components.v1 as components
import random

# ==========================================
# 1. 데이터 정의 (코드, MIDI, TAB악보, 설정)
# ==========================================

chords = {
    "클린톤": [
        "Em", "G", "D", "Am", "C", "Bm",
        "F", "A", "Dm", "Fm", "Cm", "Gm",
        "Dsus2", "Asus2", "Gsus2", "Esus4",
        "Cadd9", "Gadd9", "Em9", "Am9",
    ],
    "디스토션": [
        "E5", "G5", "D5", "A5",
        "F5", "B5", "C5", "Bb5",
        "F#5", "Ab5", "Eb5", "Db5",
        "E5-F5", "D5-E5", "A5-G5", "C5-D5",
    ],
    "빌드업": [
        "Em7", "Cmaj7", "G", "Bm7", "Dadd9",
        "Am7", "Fmaj7", "Gmaj7", "Dm7", "Em9",
        "Cadd9", "Asus4", "Dsus4", "Gsus4",
        "Bm9", "Am9", "Cmaj9", "Fmaj9",
        "Em11", "Dm9",
    ],
}

chord_notes = {
    "Em":    [40, 47, 52, 55, 59, 64],
    "G":     [43, 47, 52, 55, 59, 67],
    "D":     [54, 59, 62, 66],
    "Am":    [45, 52, 57, 60, 64],
    "C":     [48, 52, 55, 60, 64],
    "Bm":    [47, 54, 59, 62, 66],
    "F":     [41, 45, 48, 53, 57, 65],
    "A":     [45, 49, 52, 57, 64],
    "Dm":    [50, 53, 57, 62],
    "Em7":   [40, 47, 52, 55, 59, 62],
    "Cmaj7": [48, 52, 55, 59, 64],
    "Bm7":   [47, 54, 57, 62, 66],
    "Dadd9": [50, 54, 57, 62, 66],
    "Am7":   [45, 52, 55, 57, 64],
    "E5":    [40, 47, 52],
    "G5":    [43, 50, 55],
    "D5":    [38, 45, 50],
    "A5":    [33, 40, 45],
    "F5":    [41, 48, 53],
    "B5":    [35, 42, 47],
    "C5":    [36, 43, 48],
}

tabs = {
    "Em":    ["e|--0--|", "B|--0--|", "G|--0--|", "D|--2--|", "A|--2--|", "E|--0--|"],
    "G":     ["e|--3--|", "B|--3--|", "G|--0--|", "D|--0--|", "A|--2--|", "E|--3--|"],
    "D":     ["e|--2--|", "B|--3--|", "G|--2--|", "D|--0--|", "A|--x--|", "E|--x--|"],
    "Am":    ["e|--0--|", "B|--1--|", "G|--2--|", "D|--2--|", "A|--0--|", "E|--x--|"],
    "C":     ["e|--0--|", "B|--1--|", "G|--0--|", "D|--2--|", "A|--3--|", "E|--x--|"],
    "Bm":    ["e|--2--|", "B|--3--|", "G|--4--|", "D|--4--|", "A|--2--|", "E|--x--|"],
    "F":     ["e|--1--|", "B|--1--|", "G|--2--|", "D|--3--|", "A|--3--|", "E|--1--|"],
    "A":     ["e|--0--|", "B|--2--|", "G|--2--|", "D|--2--|", "A|--0--|", "E|--x--|"],
    "Dm":    ["e|--1--|", "B|--3--|", "G|--2--|", "D|--0--|", "A|--x--|", "E|--x--|"],
    "Fm":    ["e|--1--|", "B|--2--|", "G|--1--|", "D|--3--|", "A|--3--|", "E|--1--|"],
    "Cm":    ["e|--3--|", "B|--4--|", "G|--5--|", "D|--5--|", "A|--3--|", "E|--x--|"],
    "Gm":    ["e|--3--|", "B|--3--|", "G|--3--|", "D|--5--|", "A|--5--|", "E|--3--|"],
    "Dsus2": ["e|--0--|", "B|--3--|", "G|--2--|", "D|--0--|", "A|--x--|", "E|--x--|"],
    "Asus2": ["e|--0--|", "B|--0--|", "G|--2--|", "D|--2--|", "A|--0--|", "E|--x--|"],
    "Gsus2": ["e|--3--|", "B|--3--|", "G|--0--|", "D|--0--|", "A|--0--|", "E|--3--|"],
    "Esus4": ["e|--0--|", "B|--0--|", "G|--2--|", "D|--2--|", "A|--2--|", "E|--0--|"],
    "Cadd9": ["e|--0--|", "B|--3--|", "G|--0--|", "D|--2--|", "A|--3--|", "E|--x--|"],
    "Gadd9": ["e|--0--|", "B|--3--|", "G|--0--|", "D|--0--|", "A|--2--|", "E|--3--|"],
    "Em9":    ["e|--0--|", "B|--0--|", "G|--0--|", "D|--2--|", "A|--2--|", "E|--0--|"],
    "Am9":    ["e|--0--|", "B|--1--|", "G|--0--|", "D|--2--|", "A|--0--|", "E|--x--|"],
    "E5":    ["e|--x--|", "B|--x--|", "G|--x--|", "D|--2--|", "A|--2--|", "E|--0--|"],
    "G5":    ["e|--x--|", "B|--x--|", "G|--x--|", "D|--5--|", "A|--5--|", "E|--3--|"],
    "D5":    ["e|--x--|", "B|--x--|", "G|--x--|", "D|--0--|", "A|--5--|", "E|--x--|"],
    "A5":    ["e|--x--|", "B|--x--|", "G|--x--|", "D|--2--|", "A|--0--|", "E|--x--|"],
    "F5":    ["e|--x--|", "B|--x--|", "G|--x--|", "D|--3--|", "A|--3--|", "E|--1--|"],
    "B5":    ["e|--x--|", "B|--x--|", "G|--x--|", "D|--4--|", "A|--2--|", "E|--x--|"],
    "C5":    ["e|--x--|", "B|--x--|", "G|--x--|", "D|--5--|", "A|--3--|", "E|--x--|"],
    "Bb5":   ["e|--x--|", "B|--x--|", "G|--x--|", "D|--3--|", "A|--1--|", "E|--x--|"],
    "F#5":   ["e|--x--|", "B|--x--|", "G|--x--|", "D|--4--|", "A|--4--|", "E|--2--|"],
    "Ab5":   ["e|--x--|", "B|--x--|", "G|--x--|", "D|--6--|", "A|--6--|", "E|--4--|"],
    "Eb5":   ["e|--x--|", "B|--x--|", "G|--x--|", "D|--1--|", "A|--1--|", "E|--x--|"],
    "Db5":   ["e|--x--|", "B|--x--|", "G|--x--|", "D|--0--|", "A|--4--|", "E|--x--|"],
    "E5-F5": ["e|--x--|", "B|--x--|", "G|--x--|", "D|--2--|", "A|--2--|", "E|--0--|"],
    "D5-E5": ["e|--x--|", "B|--x--|", "G|--x--|", "D|--0--|", "A|--5--|", "E|--x--|"],
    "A5-G5": ["e|--x--|", "B|--x--|", "G|--x--|", "D|--2--|", "A|--0--|", "E|--x--|"],
    "C5-D5": ["e|--x--|", "B|--x--|", "G|--x--|", "D|--5--|", "A|--3--|", "E|--x--|"],
    "Em7":   ["e|--0--|", "B|--3--|", "G|--0--|", "D|--2--|", "A|--2--|", "E|--0--|"],
    "Cmaj7": ["e|--0--|", "B|--0--|", "G|--0--|", "D|--2--|", "A|--3--|", "E|--x--|"],
    "Bm7":   ["e|--2--|", "B|--3--|", "G|--2--|", "D|--4--|", "A|--2--|", "E|--x--|"],
    "Dadd9": ["e|--0--|", "B|--3--|", "G|--2--|", "D|--0--|", "A|--x--|", "E|--x--|"],
    "Am7":   ["e|--0--|", "B|--1--|", "G|--0--|", "D|--2--|", "A|--0--|", "E|--x--|"],
    "Fmaj7": ["e|--0--|", "B|--1--|", "G|--2--|", "D|--3--|", "A|--x--|", "E|--x--|"],
    "Gmaj7": ["e|--2--|", "B|--3--|", "G|--0--|", "D|--0--|", "A|--2--|", "E|--3--|"],
    "Dm7":   ["e|--1--|", "B|--1--|", "G|--2--|", "D|--0--|", "A|--x--|", "E|--x--|"],
    "Asus4": ["e|--0--|", "B|--3--|", "G|--2--|", "D|--2--|", "A|--0--|", "E|--x--|"],
    "Dsus4": ["e|--3--|", "B|--3--|", "G|--2--|", "D|--0--|", "A|--x--|", "E|--x--|"],
    "Gsus4": ["e|--3--|", "B|--3--|", "G|--0--|", "D|--0--|", "A|--2--|", "E|--3--|"],
    "Bm9":   ["e|--0--|", "B|--3--|", "G|--2--|", "D|--4--|", "A|--2--|", "E|--x--|"],
    "Cmaj9": ["e|--0--|", "B|--3--|", "G|--0--|", "D|--2--|", "A|--3--|", "E|--x--|"],
    "Fmaj9": ["e|--0--|", "B|--1--|", "G|--0--|", "D|--3--|", "A|--x--|", "E|--x--|"],
    "Em11":  ["e|--0--|", "B|--3--|", "G|--0--|", "D|--2--|", "A|--2--|", "E|--0--|"],
    "Dm9":   ["e|--1--|", "B|--1--|", "G|--0--|", "D|--0--|", "A|--x--|", "E|--x--|"],
}

melody_settings = {
    "인트로": {
        "strings": ["e", "B", "G"],
        "fret_range": (0, 7),
        "notes": 8,
        "rest_chance": 0.2,
    },
    "클라이맥스": {
        "strings": ["D", "A", "E"],
        "fret_range": (0, 12),
        "notes": 8,
        "rest_chance": 0.1,
    },
    "아웃트로": {
        "strings": ["e", "B", "G", "D"],
        "fret_range": (0, 12),
        "notes": 8,
        "rest_chance": 0.3,
    },
}

open_strings = {"E": 40, "A": 45, "D": 50, "G": 55, "B": 59, "e": 64}

# ==========================================
# 2. 오디오 연산 및 생성 로직 함수
# ==========================================

def midi_to_freq(midi):
    return 440.0 * (2 ** ((midi - 69) / 12))

def generate_random_melody(part):
    setting = melody_settings[part]
    strings = ["e", "B", "G", "D", "A", "E"]
    active_strings = setting["strings"]
    fret_min, fret_max = setting["fret_range"]
    note_count = setting["notes"]
    rest_chance = setting["rest_chance"]

    string_notes = {s: [] for s in strings}
    melody_freqs = []

    for _ in range(note_count):
        chosen = random.choice(active_strings)
        for s in strings:
            if s == chosen:
                if random.random() < rest_chance:
                    string_notes[s].append("--")
                    melody_freqs.append(0)
                else:
                    fret = random.randint(fret_min, fret_max)
                    string_notes[s].append(str(fret).rjust(2, "-"))
                    midi = open_strings[s] + fret
                    melody_freqs.append(round(midi_to_freq(midi), 2))
            else:
                string_notes[s].append("--")

    tab_lines = []
    for s in strings:
        line = f"{s}|"
        for note in string_notes[s]:
            line += f"---{note}---"
        line += "|"
        tab_lines.append(line)

    return tab_lines, melody_freqs

def play_chord_html(notes):
    freqs = [round(midi_to_freq(n), 2) for n in notes]
    return f"""
    <script>
    (function() {{
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const freqs = {freqs};
        freqs.forEach(freq => {{
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, ctx.currentTime);
            gain.gain.setValueAtTime(0.15, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.5);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + 1.5);
        }});
    }})();
    </script>
    <p style="color:#55ff55; font-size:12px; font-weight:bold;">🔊 코드 재생 완료</p>
    """

def play_melody_html(freqs):
    valid = [(i, f) for i, f in enumerate(freqs) if f > 0]
    notes_js = str([[i * 0.3, f] for i, f in valid])
    return f"""
    <script>
    (function() {{
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const notes = {notes_js};
        notes.forEach(([time, freq]) => {{
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, ctx.currentTime + time);
            gain.gain.setValueAtTime(0.2, ctx.currentTime + time);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + time + 0.25);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(ctx.currentTime + time);
            osc.stop(ctx.currentTime + time + 0.25);
        }});
    }})();
    </script>
    <p style="color:#55ff55; font-size:12px; font-weight:bold;">🔊 멜로디 재생 완료</p>
    """

# ==========================================
# 3. Streamlit 웹 인터페이스 (UI) 구현
# ==========================================

st.title("🎸 ENVY 스타일 TAB 생성기")
st.caption("Post-Hardcore / Post-Rock — 모차르트 주사위 방식")
st.divider()

# --- 코드 섹션 ---
st.subheader("코드 TAB")
chord_part = st.radio("파트 선택", ["클린톤", "디스토션", "빌드업"], horizontal=True)

if st.button("랜덤 코드 진행 생성"):
    pool = chords[chord_part]
    length = 4 if chord_part == "디스토션" else random.randint(3, 4)
    st.session_state["progression"] = random.choices(pool, k=length)

# 세션 상태 기반 렌더링 (재생 버튼 클릭 시 악보 소멸 방지)
if "progression" in st.session_state:
    progression = st.session_state["progression"]
    st.write("**코드 진행:** " + " → ".join(progression))
    
    unique_chords = list(dict.fromkeys(progression))
    cols = st.columns(len(unique_chords))
    
    for i, chord in enumerate(unique_chords):
        with cols[i]:
            st.markdown(f"**[ {chord} ]**")
            if chord in tabs:
                st.code("\n".join(tabs[chord]), language=None)
            if chord in chord_notes:
                if st.button(f"▶ {chord} 재생", key=f"play_{chord}"):
                    components.html(play_chord_html(chord_notes[chord]), height=35)
    st.success("✅ 생성 완료!")

st.divider()

# --- 멜로디 섹션 ---
st.subheader("멜로디 TAB")
melody_part = st.radio("멜로디 파트", ["인트로", "클라이맥스", "아웃트로"], horizontal=True)

if st.button("랜덤 멜로디 생성"):
    tab_lines, freqs = generate_random_melody(melody_part)
    st.session_state["melody_tab"] = tab_lines
    st.session_state["melody_freqs"] = freqs

# 세션 상태 기반 렌더링 (멜로디 재생 버튼 클릭 시 악보 소멸 방지)
if "melody_tab" in st.session_state:
    st.code("\n".join(st.session_state["melody_tab"]), language=None)
    if st.button("▶ 멜로디 재생"):
        components.html(play_melody_html(st.session_state["melody_freqs"]), height=35)
    st.success("✅ 생성 완료!")