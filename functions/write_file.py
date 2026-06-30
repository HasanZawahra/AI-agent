import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        
        valid_target_dir = os.path.commonpath([abs_path, target_file]) == abs_path

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        
        parent_directory = os.path.dirname(target_file)
        os.makedirs(parent_directory, exist_ok=True)
    
        try:
            with open(target_file, "w", encoding="utf-8") as file:
                file.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
        except Exception as e:
            return "Error: " + str(e)
        

    except Exception as e:
        return "Error: " + str(e)