import os
import sys

def load_num2words_dictionary(dictionary_file_path: str):
    number_to_word = {}
    comments = ['#', '//', '/*', '*/', ';']
    errors = []
    warnings = []

    try:
        with open(dictionary_file_path, "r", encoding='utf-8') as file:
            for i, line in enumerate(file, start=1):
                line = line.strip()
                if not line or any(line.startswith(prefix) for prefix in comments):
                    continue

                if '=' not in line:
                    warnings.append(f"[Line {i}] Invalid format: '{line}' — expected 'number = word'")
                    continue

                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()

                if not key.isdigit() or not value:
                    errors.append(
                        f"[Line {i}] Invalid entry: '{line}' — left side must be a number and right side non-empty"
                    )
                    continue

                number_to_word[int(key)] = value
    except Exception as e:
        print(f"Error reading dictionary file: {e}")
        return None, None, False

    if errors or warnings:
        if errors:
            print("Errors:")
            for err in errors:
                print(err)
        if warnings:
            print("Warnings:")
            for warn in warnings:
                print(warn)
        return number_to_word, {}, False

    number_to_word = dict(sorted(number_to_word.items(), reverse=True))
    word_to_number = {v.lower(): k for k, v in number_to_word.items()}

    return number_to_word, word_to_number, True

def is_valid_n2w_file(file_path):
    return os.path.exists(file_path) and file_path.endswith('.n2w') and os.path.isfile(file_path)

def main():
    if len(sys.argv) != 2:
        print("Usage: pyn2wc <path_to_n2w_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        if is_valid_n2w_file(file_path):
            number_to_word, word_to_number, valid = load_num2words_dictionary(file_path)
            if valid:
                print(f"{os.path.basename(file_path)} passed the checks.")
                print(f"{os.path.basename(file_path)} Is Ready To Use.")
        else:
            print(f"File '{file_path}' failed the checks. Ensure it exists, is a file, and has a .n2w extension.")
            sys.exit(1)
    except Exception as e:
        print(f"Error checking file '{file_path}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()