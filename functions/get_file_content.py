import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)

        abs_file_path = os.path.abspath(
            os.path.join(abs_working_dir, file_path)
        )

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot access "{file_path}" outside working directory.'

        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" does not exist.'

        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" is not a file.'

        with open(abs_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return content or "File is empty."

    except PermissionError:
        return f'Error: Permission denied for "{file_path}".'
    except Exception as e:
        return f"Error: {str(e)}"