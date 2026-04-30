"""Run 100 Days of Code development sandbox"""

import warnings
import importlib
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=UserWarning, module="langchain_core")

# Load .env ONCE here — all submodules inherit it via os.getenv()
load_dotenv()

# ← Change this to switch projects
PROJECT_LIST = {
    "019l143": ("D19 L143", "d019", "d019l143.py"),
    "019l140": ("D19 L140", "d019", "d019l140.py"),
    "018l137": ("D18 L137", "d018", "d018l137.py"),
    "018l136": ("D18 L136", "d018", "d018l136.py"),
    "018l129": ("D18 L129", "d018", "d018l129.py"),
    # "017ql120": ("D17q L120", "d017q", "d017ql120.py"),
    # "017l117": ("D17 L117", "d017", "d017l117.py"),
    # "016bl113": ("D16b L113", "d016b", "d016bl113.py"),
    # "016l112": ("D16 L112", "d016", "d016l112.py"),
    # "016l110": ("D16 L110", "d016", "d016l110.py"),
    # "015l105": ("D15 L105", "d015", "d015l105.py"),
    # "014l102": ("D14 L102", "d014", "d014l102.py"),
    # "012l092": ("D12 L92", "d012", "d012l092.py"),
    # "012ex11": ("D12 Ex11", "d012", "d012ex11.py"),
    # "011l079": ("D11 L79", "d011", "d011l079.py"),
    # "010l076": ("D10 L76", "d010", "d010l076.py"),
    # "009l070": ("D9 L70", "d009", "d009l070.py"),
    # "009l069": ("D9 L69", "d009", "d009l069.py"),
    # "009ex": ("D9 Ex9", "d009", "d009ex9.py"),
    "Q": ("Quit", "", ""),
}
# put the key of the first dictionary item in DEFAULT_PROJECT
DEFAULT_PROJECT = next(iter(PROJECT_LIST), None)


def safe_input(prompt):
    """
    wrap input in a try-except to catch and retry if a KeyboardInterupt
    error occurs on the input statement
    """
    while True:
        try:
            return input(prompt)
        except KeyboardInterrupt:
            print()
            continue


def run_project():
    """
    show the menu, prompt for a selection
    if ans is empty, run the default project
    if ans == 'q', exit
    """
    prompt = build_prompt(PROJECT_LIST)
    ans = safe_input(prompt)
    if ans == "":
        ans = DEFAULT_PROJECT
    elif ans == "Q":
        return

    folder, file = get_selected_project(PROJECT_LIST, ans)
    if folder == "":
        print("invalid selection")
    print(f"{folder=}, {file=}")

    try:
        module = importlib.import_module(f"{folder}.run")
        module.main(file)
    except ModuleNotFoundError:
        print(f"no 'run.py' found in subfolder: {folder}")
    except AttributeError:
        print(f"No main() function found in {folder}.run.py")


def build_prompt(project_list):
    """build a prompt menu from the project_list dictionary"""
    lines = []
    for key, (label, _, _) in project_list.items():
        lines.append(f"{key}: {label}\n")
    return "".join(lines)


def find_by_key(items, search_key):
    """find the search_key in the dictionary items"""
    return items.get(search_key) or ("", "", "")


def get_selected_project(project_list, selection):
    """
    return the folder and file portions of the project list value tuple
    for the selected project
    """
    _, folder, file = find_by_key(project_list, selection)
    return folder, file


if __name__ == "__main__":
    run_project()
