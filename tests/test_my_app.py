from my_app.capture import capture
from my_app.ordinals import remove_ordinal_matches


def test_my_app_remove_ordinal_matches():
    result = remove_ordinal_matches(
        "2. Niemandem darf seine Staatsangehörigkeit willkürlich entzogen noch das Recht versagt werden, seine Staatsangehörigkeit zu wechseln."
    )
    assert (
        result
        == "Niemandem darf seine Staatsangehörigkeit willkürlich entzogen noch das Recht versagt werden, seine Staatsangehörigkeit zu wechseln."
    )


def test_my_app_remove_ordinal_matches_zh():
    result = remove_ordinal_matches("㈡ 任何人的财产不得任意剥夺。", "zh")
    assert result == "任何人的财产不得任意剥夺。"


def test_my_app_remove_ordinal_matches_missing():
    result = remove_ordinal_matches("㈡ 任何人的财产不得任意剥夺。", "missing")
    assert result == "任何人的财产不得任意剥夺。"


def test_my_app():
    cmd = [
        "pipenv",
        "run",
        "python",
        "-m",
        "my_app",
        "--text",
        "1. Gehe nicht über los.",
    ]
    out, err, exitcode = capture(cmd)
    assert exitcode == 0
    assert out.decode().strip() == "Gehe nicht über los."
    assert err == b""


def test_my_app_zh():
    cmd = [
        "pipenv",
        "run",
        "python",
        "-m",
        "my_app",
        "--text",
        "㈡ 任何人的财产不得任意剥夺。",
        "--lang",
        "zh",
    ]
    out, err, exitcode = capture(cmd)
    assert exitcode == 0
    assert out.decode().strip() == "任何人的财产不得任意剥夺。"
    assert err == b""
