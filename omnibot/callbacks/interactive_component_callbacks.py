"""
Interactive component callbacks for internal omnibot functionality.
"""
import json

from omnibot import logging

logger = logging.getLogger(__name__)


def echo_dialog_submission_callback(container):
    """
    Just repond back with whatever is sent in.
    """
    payload = container.payload
    logger.debug(f"echo callback payload: {json.dumps(payload, indent=2)}")
    return {
        # Respond back to the slash command with the same text
        "responses": [
            {
                "text": payload["submission"]["echo_element"],
                "omnibot_parse": {"text": ["users", "specials", "channels"]},
            },
        ],
    }
