"""
question data for the Quiz game
"""

import html
import requests

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {
        "text": "Approximately one quarter of human bones are in the feet.",
        "answer": "True",
    },
    {
        "text": "The total surface area of a human lungs is the size of a football pitch.",
        "answer": "True",
    },
    {
        "text": (
            "In West Virginia, USA, if you accidentally hit an animal with your car, "
            "you are free to take it home to eat."
        ),
        "answer": "True",
    },
    {
        "text": (
            "In London, UK, if you happen to die in the House of Parliament, "
            "you are entitled to a state funeral."
        ),
        "answer": "False",
    },
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {
        "text": "No piece of square dry paper can be folded in half more than 7 times.",
        "answer": "False",
    },
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
]


def get_json_from_api(url, headers=None, params=None, timeout=10):
    """
    call the given api url and return the json object returned
    """
    try:
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        return response.json()  # Parse and return JSON
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except ValueError:
        print("Response was not valid JSON")
        return None


def get_open_trivia_db_data():
    """
    get quiz data from an Open Trivia DB api call
    call convert_json_data() to convert it to a list of text / answer dictionary items
    return that list
    """
    api_url = "https://opentdb.com/api.php?amount=12&difficulty=medium&type=boolean"
    data = get_json_from_api(api_url)
    if not data:
        print("Something went wrong.")
        return None

    q_a_list = convert_json_data(data)
    return q_a_list


def convert_json_data(data):
    """
    convert the data returned from Open Trivia DB api call
    to a list of text: answer dictionary items
    """
    q_a_list = []
    for item in data.get("results", []):
        question = html.unescape(item.get("question", ""))
        answer = item.get("correct_answer", "")

        q_a_list.append({"question": question, "correct_answer": answer})
    return q_a_list
