import pytest
from unittest.mock import patch
import jarvis

# ---------- speak and listen mocking ----------

@patch("jarvis.speak")
@patch("os.system")
def test_open_application_success(mock_os, mock_speak):
    result = jarvis.open_application("notepad")
    mock_speak.assert_called_once_with("Opening Notepad")
    mock_os.assert_called_once()
    assert result is True


@patch("jarvis.speak")
@patch("os.system")
def test_open_application_fail(mock_os, mock_speak):
    result = jarvis.open_application("unknown_app")
    mock_speak.assert_not_called()
    mock_os.assert_not_called()
    assert result is False


@patch("jarvis.speak")
@patch("datetime.datetime")
def test_get_time(mock_datetime, mock_speak):
    mock_datetime.now.return_value.strftime.side_effect = lambda fmt: "10:30 AM" if "%I" in fmt else "Monday"
    jarvis.get_time()
    mock_speak.assert_called_once()


@patch("jarvis.speak")
@patch("datetime.datetime")
def test_get_date(mock_datetime, mock_speak):
    mock_datetime.now.return_value.strftime.side_effect = lambda fmt: "October 27, 2025" if "%B" in fmt else "Monday"
    jarvis.get_date()
    mock_speak.assert_called_once()


@patch("jarvis.get_gemini_response", return_value="Mocked Gemini Response")
@patch("jarvis.speak")
def test_execute_command_unrecognized(mock_speak, mock_gemini):
    jarvis.execute_command("some random command")
    mock_speak.assert_any_call("I am not sure, let me check.")
    mock_speak.assert_any_call("Mocked Gemini Response")
