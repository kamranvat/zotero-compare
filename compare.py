import os
import json
import argparse


def extract_paper_titles(json_file):
    """Gets the titles from the library

    Args:
        json_file (filepath to .json file): the Zotero exported library to pull titles from
    Returns:
        list: list of titles
    """
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        titles = [entry["title"] for entry in data]
    return titles


def find_duplicates(json_file):
    """Checks a single .json formatted library for duplicates and prints them as well as their count

    Args:
        json_file (filepath to .json file): Zotero exported library to check
    """
    titles = extract_paper_titles(json_file)
    duplicate_titles = set(title for title in titles if titles.count(title) > 1)

    print(f"Number of duplicates in {json_file}: {len(duplicate_titles)}")
    if duplicate_titles:
        print("Duplicate titles:")
        for title in duplicate_titles:
            print(f"- {title}")


def compare_libraries(library1, library2):
    """Takes two .json formatted libraries, extracts the titles with extract_paper_titles(), and prints titles that occur in both libraries as well as their count

    Args:
        library1 (filepath to .json file): The first zotero exported library for comparison
        library2 (filepath to .json file): The second zotero exported library for comparison
    """
    titles1 = extract_paper_titles(library1)
    titles2 = extract_paper_titles(library2)

    common_titles = set(titles1).intersection(titles2)

    print(f"Number of common papers: {len(common_titles)}")
    print("Common paper titles:")
    for title in common_titles:
        print(f"- {title}")


def get_json_files(directory="./jsons"):
    """Gets all .json files from the ./jsons directory

    Args:
        directory (str, optional): Filepath to folder containing the exported libraries. Defaults to "./jsons".

    Returns:
        list: List of .json files
    """
    json_files = [f for f in os.listdir(directory) if f.endswith(".json")]
    return json_files


def main():
    parser = argparse.ArgumentParser(description="Zotero Library Comparator")
    parser.add_argument(
        "-d",
        "--check_duplicates",
        action="store_true",
        help="Check for duplicates within JSON files",
    )
    args = parser.parse_args()

    json_files = get_json_files()

    if args.check_duplicates:
        for json_file in json_files:
            file_path = os.path.join("./jsons", json_file)
            find_duplicates(file_path)
    else:
        if len(json_files) < 2:
            print("Error: At least two JSON files are required for comparison.")
        elif len(json_files) == 2:
            library1 = os.path.join("./jsons", json_files[0])
            library2 = os.path.join("./jsons", json_files[1])
            compare_libraries(library1, library2)
        else:
            print("Available JSON files for comparison:")
            for i, file in enumerate(json_files, start=1):
                print(f"{i}. {file}")

            selection1 = int(
                input("Enter the number of the first library to compare: ")
            )
            selection2 = int(
                input("Enter the number of the second library to compare: ")
            )

            library1 = os.path.join("./jsons", json_files[selection1 - 1])
            library2 = os.path.join("./jsons", json_files[selection2 - 1])

            compare_libraries(library1, library2)


if __name__ == "__main__":
    main()
