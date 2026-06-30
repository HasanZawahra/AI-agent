import argparse
import os
import sys
from dotenv import load_dotenv
from google import genai
import call_function
from prompts import system_prompt
from google.genai import types
from call_function import available_functions, call_function
from config import MAX_ITERATIONS

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.")

    client = genai.Client(api_key=api_key)


    for _ in range(MAX_ITERATIONS):
        response = client.models.generate_content(model = "gemini-2.5-flash", 
                                                contents = messages, 
                                                config=types.GenerateContentConfig(
                                                        tools=[available_functions], system_instruction=system_prompt),)
        
        verbose_mode = args.verbose

        if verbose_mode:
            print(f"User prompt: {args.user_prompt}")
            print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
            print("Response tokens: " + str(response.usage_metadata.candidates_token_count))


        if response.function_calls:
            if response.candidates and response.candidates[0].content:
                messages.append(response.candidates[0].content)
            
            function_results_list = []
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=verbose_mode)
                print(f"Function call result: {function_call_result}")
                
                if not function_call_result.parts:
                    raise ValueError("The function call response parts list is empty.")
                    
                first_part = function_call_result.parts[0]
                if first_part.function_response is None:
                    raise TypeError("The first part does not contain a valid FunctionResponse object.")
                    
                if first_part.function_response.response is None:
                    raise ValueError("The FunctionResponse object field '.response' is None.")
                
                function_results_list.append(first_part)

                if verbose_mode:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            
            messages.append(types.Content(role="user", parts=function_results_list))

        else:
            print(response.text)
            break

    else:
        print(f"Error: Exceeded the maximum allowance of {MAX_ITERATIONS} iterations without receiving a final answer.")
        print("The model is stuck in an infinite loop of calling functions or failing to terminate.")
        sys.exit(1)
   


if __name__ == "__main__":
    main()
