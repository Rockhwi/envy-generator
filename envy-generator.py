import streamlit as st
import random

# 코드 데이터
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

# TAB 악보 데이터
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
    "Em9":   ["e|--0--|", "B|--0--|", "G|--0--|", "D|--2--|", "A|--2--|", "E|--0--|"],
    "Am9":   ["e|--0--|", "B|--1--|", "G|--0--|", "D|--2--|", "A|--0--|", "E|--x--|"],
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

# 파트별 멜로디 설정
melody_settings = {
    "인트로": {
        "strings": ["e", "B", "G"],       # 주로 고음 줄
        "fret_range": (0, 7),             # 낮은 프렛 (클린 개방음)
        "notes": 8,                        # 음표 개수
        "rest_chance": 0.2,               # 쉼표(---) 확률
    },
    "클라이맥스": {
        "strings": ["D", "A", "E"],       # 주로 저음 줄
        "fret_range": (0, 12),            # 전체 프렛
        "notes": 8,
        "rest_chance": 0.1,
    },
    "아웃트로": {
        "strings": ["e", "B", "G", "D"],  # 혼합
        "fret_range": (0, 12),
        "notes": 8,
        "rest_chance": 0.3,               # 여백 많이
    },
}

def generate_random_melody(part):
    setting = melody_settings[part]
    strings = ["e", "B", "G", "D", "A", "E"]
    active_strings = setting["strings"]
    fret_min, fret_max = setting["fret_range"]
    note_count = setting["notes"]
    rest_chance = setting["rest_chance"]

    # 각 줄별 음표 배열 초기화
    string_notes = {s: [] for s in strings}

    for i in range(note_count):
        # 이번 박자에 소리낼 줄 선택
        chosen = random.choice(active_strings)
        for s in strings:
            if s == chosen:
                if random.random() < rest_chance:
                    string_notes[s].append("--")
                else:
                    fret = random.randint(fret_min, fret_max)
                    string_notes[s].append(str(fret).rjust(2, "-"))
            else:
                string_notes[s].append("--")

    # TAB 형식으로 변환
    tab_lines = []
    for s in strings:
        line = f"{s}|"
        for note in string_notes[s]:
            line += f"---{note}---"
        line += "|"
        tab_lines.append(line)

    return tab_lines

# UI
st.title("🎸 POST ROCK 스타일 TAB 생성기")
st.caption("Post-Hardcore / Post-Rock")

st.divider()

# 코드 섹션
st.subheader("코드 TAB")
chord_part = st.radio("파트 선택", ["클린톤", "디스토션", "빌드업"], horizontal=True)

if st.button("랜덤 코드 진행 생성"):
    pool = chords[chord_part]
    length = 4 if chord_part == "디스토션" else random.randint(3, 4)
    progression = random.choices(pool, k=length)

    st.write("**코드 진행:** " + " → ".join(progression))

    unique_chords = list(dict.fromkeys(progression))
    cols = st.columns(len(unique_chords))
    for i, chord in enumerate(unique_chords):
        with cols[i]:
            st.markdown(f"**[ {chord} ]**")
            if chord in tabs:
                st.code("\n".join(tabs[chord]), language=None)

    st.divider()
    st.success("✅ 생성 완료! 다시 만들려면 위 버튼을 누르세요 🎸")

st.divider()

# 멜로디 섹션
st.subheader("멜로디 TAB")
melody_part = st.radio("멜로디 파트", ["인트로", "클라이맥스", "아웃트로"], horizontal=True)

if st.button("랜덤 멜로디 생성"):
    tab_lines = generate_random_melody(melody_part)
    st.code("\n".join(tab_lines), language=None)

    st.divider()
    st.success("✅ 생성 완료! 다시 만들려면 위 버튼을 누르세요 🎸")
