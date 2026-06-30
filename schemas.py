from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the first pre-defined maximum chars count if the file contains more than the count, or reads the intire file if its less",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to read, starting from the permitted working directory",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Securely validates and runs a local Python script via a timed subprocess, returning its formatted stdout, stderr, or execution error messages.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the Python file (.py) to execute, starting from the permitted working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass into the script during execution",
            ),
        },
    ),
)

schema_write_file= types.FunctionDeclaration(
    name="write_file",
    description="Creates any missing parent directories, validates that the destination path is within the allowed sandbox boundary, and overwrites the target file with the provided text content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path where the file should be created or overwritten, starting from the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file",
            ),
        },
    ),
)
