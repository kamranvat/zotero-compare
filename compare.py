import os
import json

def extract_paper_titles(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        titles = [entry['title'] for entry in data]
    return set(titles)

def compare_libraries(library1, library2):
    titles1 = extract_paper_titles(library1)
    titles2 = extract_paper_titles(library2)
    
    common_titles = titles1.intersection(titles2)
    
    print(f"Number of common papers: {len(common_titles)}")
    print("Common paper titles:")
    for title in common_titles:
        print(f"- {title}")

def get_json_files(directory='./jsons'):
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    return json_files

def main():
    json_files = get_json_files()

    if len(json_files) < 2:
        print("Error: At least two JSON files are required for comparison.")
    elif len(json_files) == 2:
        library1 = os.path.join('./jsons', json_files[0])
        library2 = os.path.join('./jsons', json_files[1])
        compare_libraries(library1, library2)
    else:
        print("Available JSON files for comparison:")
        for i, file in enumerate(json_files, start=1):
            print(f"{i}. {file}")

        selection1 = int(input("Enter the number of the first library to compare: "))
        selection2 = int(input("Enter the number of the second library to compare: "))

        library1 = os.path.join('./jsons', json_files[selection1 - 1])
        library2 = os.path.join('./jsons', json_files[selection2 - 1])

        compare_libraries(library1, library2)

if __name__ == "__main__":
    main()
