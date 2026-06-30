import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        
        valid_target_dir = os.path.commonpath([abs_path, target_file]) == abs_path

        if not valid_target_dir:
            return f'Cannot read "{target_file}"'
        
        if not os.path.isfile(target_file):
            return f'"{target_file}" is not a file'
        
        content=""
        
        try:
            with open(target_file, "r", encoding="utf-8") as file:
                content = file.read(MAX_CHARS)
                if file.read(1):
                    content += f'[...File "{target_file}" truncated at {MAX_CHARS} characters]'

        except Exception as e:
            return f'Error: {e}'
        
        return content
    
    except Exception as e:
        return f'Error: {e}'
