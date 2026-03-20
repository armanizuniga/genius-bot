# tests/test_agent.py

import pytest
from unittest.mock import MagicMock, patch
from bot.agent import GeniusAgent


# ── Helpers ────────────────────────────────────────────────────────────────

def make_mock_response(text: str):
    """Builds a fake Anthropic API response object."""
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text=text)]
    return mock_response


# ── Fixtures ───────────────────────────────────────────────────────────────

@pytest.fixture
def agent():
    """Creates a GeniusAgent with the Claude API patched out."""
    with patch("bot.agent.Anthropic") as mock_anthropic:
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        mock_client.messages.create.return_value = make_mock_response(
            "Hi! I'm Armani, how can I help?"
        )
        bot = GeniusAgent()
        bot.client = mock_client
        yield bot


# ── Tests ──────────────────────────────────────────────────────────────────

class TestGeniusAgentInit:
    def test_history_starts_empty(self, agent):
        assert agent.conversation_history == []

    def test_model_is_set(self, agent):
        assert agent.model == "claude-sonnet-4-20250514"

    def test_max_tokens_is_set(self, agent):
        assert agent.max_tokens == 1024


class TestGeniusAgentChat:
    def test_chat_returns_string(self, agent):
        response = agent.chat("My iPhone won't turn on")
        assert isinstance(response, str)

    def test_user_message_appended_to_history(self, agent):
        agent.chat("My iPhone won't turn on")
        assert agent.conversation_history[0]["role"] == "user"
        assert agent.conversation_history[0]["content"] == "My iPhone won't turn on"

    def test_assistant_message_appended_to_history(self, agent):
        agent.chat("My iPhone won't turn on")
        assert agent.conversation_history[1]["role"] == "assistant"

    def test_history_grows_with_each_message(self, agent):
        agent.chat("My iPhone won't turn on")
        agent.chat("I already tried restarting it")
        assert len(agent.conversation_history) == 4  # 2 user + 2 assistant

    def test_chat_returns_mocked_response(self, agent):
        response = agent.chat("Hello")
        assert response == "Hi! I'm Armani, how can I help?"


class TestGeniusAgentReset:
    def test_reset_clears_history(self, agent):
        agent.chat("My AirPods won't connect")
        agent.reset()
        assert agent.conversation_history == []

    def test_reset_after_multiple_messages(self, agent):
        agent.chat("My AirPods won't connect")
        agent.chat("I already tried forgetting the device")
        agent.chat("Still not working")
        agent.reset()
        assert len(agent.conversation_history) == 0

    def test_can_chat_after_reset(self, agent):
        agent.chat("My AirPods won't connect")
        agent.reset()
        agent.chat("New question about my Mac")
        assert len(agent.conversation_history) == 2
