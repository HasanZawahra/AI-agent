import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
        try:
            abs_path = os.path.abspath(working_directory)
            
            target_file = os.path.normpath(os.path.join(abs_path, file_path))
            
            valid_target_dir = os.path.commonpath([abs_path, target_file]) == abs_path

            if not valid_target_dir:
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

            if not os.path.isfile(target_file):
                return f'Error: "{file_path}" does not exist or is not a regular file'

            if not file_path.endswith(".py"):
                return f'Error: "{file_path}" is not a Python file'
            
            command = ["python", target_file]
            
            if args:
                command.extend(args)


            try:
                result = subprocess.run(
                    command,
                    cwd=abs_path,
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                answer_lines = []

                if result.returncode != 0:
                    answer_lines.append(f"Process exited with code {result.returncode}")

                has_stdout = result.stdout and result.stdout.strip()
                has_stderr = result.stderr and result.stderr.strip()

                if not has_stdout and not has_stderr:
                    answer_lines.append("No output produced")
                else:
                    if has_stdout:
                        answer_lines.append(f"STDOUT:\n{result.stdout.strip()}")
                    if has_stderr:
                        answer_lines.append(f"STDERR:\n{result.stderr.strip()}")

                return "\n".join(answer_lines)
            
            except subprocess.TimeoutExpired:
                return "Error: Process timed out after 30 seconds"
            except Exception as e:
                return f"Error: {e}"

            except Exception as e:
                return f"Error: {str(e)}"
            
        except Exception as e:
            return f"Error: {e}"