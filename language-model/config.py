OPENAI_API_KEY = "I DELETED OUR API KEY FROM HERE"

TRANSCRIPT_FILE = "transcriptions/transcript.txt"


COMMAND_WORD = "jerry"

PROMPT_INSTRUCTIONS = "Return the name of the function (weather, map, shops) in the text below. " \
    "If the text contains the words 'show', 'snow', or 'shoe', return 'show' for the action. " \
    "If the text contain the words 'open', 'opel', or 'ope', return 'open' for the action. " \
    "If the text contain the words 'back', 'beck', or 'bc', return 'back' for the action. " \
    "If the text contain the words 'search', 'serch', or 'church', return 'search' for the action and very next word return as function." \
    "If the text contain the words 'route', 'root', or 'road', return 'route' for the action." \
    "Return the result in JSON format:"

PROMPT_OUTPUT_FORMAT = """
{
    "action": "",
    "function": ""
}
"""