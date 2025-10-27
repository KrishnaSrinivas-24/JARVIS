import pytest
from unittest.mock import patch
import jarvis


@patch("jarvis.speak")
@patch("os.system")
def test_execute_open_command(mock_os, mock_speak):
    jarvis.execute_command("open notepad")
    mock_speak.assert_any_call("Opening Notepad")
    mock_os.assert_called_once()


@patch("jarvis.get_time")
@patch("jarvis.speak")
def test_execute_time_command(mock_speak, mock_time):
    jarvis.execute_command("what is the time")
    mock_time.assert_called_once()


@patch("jarvis.get_date")
@patch("jarvis.speak")
def test_execute_date_command(mock_speak, mock_date):
    jarvis.execute_command("what is the date")
    mock_date.assert_called_once()


@patch("jarvis.search_web")
@patch("jarvis.speak")
def test_execute_search_command(mock_speak, mock_search):
    jarvis.execute_command("search for open source ai")
    mock_search.assert_called_once_with("open source ai")
