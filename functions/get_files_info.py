import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

        if not valid_target_dir:
            return f'Cannot list "{directory}"'
        
        if not os.path.isdir(target_dir):
            return f'"{directory}" is not a directory'
        
        print(f"Result for '{directory}' directory:")
        for i in os.listdir(target_dir):
            try:
                size = os.path.getsize(os.path.join(target_dir, i))
                isdir = os.path.isdir(os.path.join(target_dir, i))
                print(f'    - {i}: file_size={size} bytes, is_dir={isdir}')
            
            except Exception as e:
                return f'Error  "{i}": {e}'
    
    except Exception as e:
        return f'Error: {e}'
