import streamlit as st
import random

st.set_page_config(page_title="Periodic Table Quiz")

# -----------------------------
# Question Bank
# -----------------------------
questions = [
    {
        "question": "Group 1A elements are known as:",
        "choices": ["Halogens", "Alkali metals", "Noble gases", "Transition metals"],
        "answer": "Alkali metals"
    },
    {
        "question": "Group 2A elements are called:",
        "choices": ["Alkaline earth metals", "Alkali metals", "Oxygen group", "Metalloids"],
        "answer": "Alkaline earth metals"
    },
    {
        "question": "Group 7A elements are known as:",
        "choices": ["Halogens", "Noble gases", "Transition metals", "Alkali metals"],
        "answer": "Halogens"
    },
    {
        "question": "Group 8A elements are also called:",
        "choices": ["Halogens", "Noble gases", "Oxygen group", "Alkali metals"],
        "answer": "Noble gases"
    },
    {
        "question": "Columns 3 to 12 of the periodic table are the:",
        "choices": ["Metalloids", "Noble gases", "Transition metals", "Halogens"],
        "answer": "Transition metals"
    },
    {
        "question": "Group 6A elements belong to which group?",
        "choices": ["Halogens", "Oxygen group", "Noble gases", "Alkali metals"],
        "answer": "Oxygen group"
    },
    {
        "question": "Semimetals are also called:",
        "choices": ["Noble gases", "Transition metals", "Metalloids", "Halogens"],
        "answer": "Metalloids"
    },
    {
        "question": "Which of the following is a metalloid?",
        "choices": ["Boron", "Neon", "Calcium", "Bromine"],
        "answer": "Boron"
    },
    {
        "question": "Metalloids are found in which groups?",
        "choices": ["1A–2A", "3A–6A", "7A–8A", "Only group 4A"],
        "answer": "3A–6A"
    },
    {
        "question": "Most elements in the periodic table are:",
        "choices": ["Nonmetals", "Noble gases", "Metals", "Metalloids"],
        "answer": "Metals"
    }
]

# -----------------------------
# Session State Initialization
# -----------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "order" not in st.session_state:
    st.session_state.order = random.sample(range(len(questions)), len(questions))

if "answered" not in st.session_state:
    st.session_state.answered = False

# -----------------------------
# Quiz Logic
# -----------------------------
st.title("🧪 Periodic Table Quiz")
st.write("Test your knowledge of the periodic table groups and classifications.")

index = st.session_state.question_index
q = questions[st.session_state.order[index]]

st.subheader(f"Question {index + 1} of {len(questions)}")
st.write(q["question"])

choice = st.radio("Choose an answer:", q["choices"], index=None)

if st.button("Submit Answer") and not st.session_state.answered:
    if choice is None:
        st.warning("Please select an answer before submitting.")
    else:
        st.session_state.answered = True
        if choice == q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. The correct answer is **{q['answer']}**.")

if st.session_state.answered:
    if st.button("Next Question"):
        st.session_state.question_index += 1
        st.session_state.answered = False

# -----------------------------
# End of Quiz
# -----------------------------
if st.session_state.question_index >= len(questions):
    st.subheader("Quiz Complete!")
    st.write(f"Your final score: **{st.session_state.score} / {len(questions)}**")

    if st.session_state.score == len(questions):
        st.success("Perfect score! You really know your periodic table.")
    elif st.session_state.score >= len(questions) * 0.7:
        st.info("Great job! You're getting the hang of it.")
    else:
        st.warning("Keep practicing — you'll get there!")

    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.order = random.sample(range(len(questions)), len(questions))
        st.session_state.answered = False
