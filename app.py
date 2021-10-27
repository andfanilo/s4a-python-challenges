import streamlit as st
from streamlit_ace import st_ace

if "current_page" not in st.session_state:
    st.session_state.current_page = 1

if "answers" not in st.session_state:
    st.session_state.answers = {
        1: """def add_two_numbers(a, b):
    return -1
""",
        2: """def flatten_list(l):
    return []
""",
    }


def _run_test(content: str, test: str) -> bool:
    try:
        exec(f"{content}\n{test}")
        return True
    except:
        return False


def _display_test_result(test: str, result: bool):
    c1, c2 = st.columns(2)
    with c1:
        st.code(test)
    with c2:
        if result:
            st.info("OK")
        else:
            st.error(f"NOK")


def _goto_next_page():
    st.session_state.current_page += 1


def page_1():
    st.markdown("Let's first test your ability to write Python functions :eyes:")
    st.info("Challenge: Return the sum of 2 numbers")
    content = st_ace(value=st.session_state.answers[1], language="python")
    if _test_page_1(content):
        st.balloons()
        st.session_state.answers[1] = content
        with st.expander("More explanation"):
            st.markdown(
                "Yes, this is how you build an addition. Did you know there is a sum() method?"
            )
        st.button("Next challenge!", on_click=_goto_next_page)


def _test_page_1(content) -> bool:
    test_1 = "assert add_two_numbers(1, 2)==3"
    test_2 = "assert add_two_numbers(1, 4)==5"

    test_1_passed = _run_test(content, test_1)
    test_2_passed = _run_test(content, test_2)

    _display_test_result(test_1, test_1_passed)
    _display_test_result(test_2, test_2_passed)

    return all([test_1_passed, test_2_passed])


def page_2():
    st.markdown("Let's go for some list challenges")
    st.info("Challenge: Do you know how to flatten a list?")
    content = st_ace(value=st.session_state.answers[2], language="python")
    if _test_page_2(content):
        st.balloons()
        st.session_state.answers[2] = content
        with st.expander("More explanation"):
            st.markdown("Yes")
        st.button("Next challenge!", on_click=_goto_next_page)


def _test_page_2(content) -> bool:
    test_1 = "assert flatten_list([[0, 1], [3], [4, 5, 6]])==[0, 1, 3, 4, 5, 6]"
    test_2 = "assert flatten_list([[0, 1], 3, [4, 5, 6]])==[0, 1, 3, 4, 5, 6]"

    test_1_passed = _run_test(content, test_1)
    test_2_passed = _run_test(content, test_2)

    _display_test_result(test_1, test_1_passed)
    _display_test_result(test_2, test_2_passed)

    return all([test_1_passed, test_2_passed])


def page_3():
    st.success("This is the end! You are very good at Python: check up your answers")
    st.json(st.session_state.answers)


def _test_page_3():
    return


PAGES = {
    1: page_1,
    2: page_2,
    3: page_3,
}


def main():
    st.set_page_config(page_title="Python Challenges", page_icon="snake", layout="wide")
    st.title("Python Challenges - Test")
    st.markdown("Want to take up the Python challenges?")
    st.caption(
        "Careful about restarting the app, it will bring you back to the beginning :wink: this is still a PoC"
    )

    PAGES[st.session_state.current_page]()


if __name__ == "__main__":
    main()
