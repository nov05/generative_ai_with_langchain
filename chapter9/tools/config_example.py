# Nov05: Copy this to config.py
import os


def set_environment():
    os.environ["OPENAI_API_KEY"] = (
        "YOUR_API_KEY"
    )
    # https://www.promptwatch.io/settings
    os.environ["PROMPTWATCH_API_KEY"] = (
        "YOUR_API_EKY"
    )
    # And/Or other keys
