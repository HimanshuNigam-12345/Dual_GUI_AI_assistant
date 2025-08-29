import sys
import os


# Add the parent directory to the path to find the 'shared' module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared.prompts import qa_prompts, summary_prompts, creative_prompts
from shared.core import get_ai_response, save_feedback
# All the duplicated functions (get_ai_response, save_feedback, etc.) can be deleted from this file.

def choose_prompt(prompts_dict):
    # ... (this function remains the same)
    print("\nChoose a prompt variant:")
    prompt_keys = list(prompts_dict.keys())
    for i, key in enumerate(prompt_keys):
        print(f"{i+1}. {key}")
    
    choice_idx = int(input("Your choice: ")) - 1
    
    if 0 <= choice_idx < len(prompt_keys):
        chosen_key = prompt_keys[choice_idx]
        return chosen_key, prompts_dict[chosen_key]
    else:
        print("Invalid choice. Using default.")
        default_key = prompt_keys[0]
        return default_key, prompts_dict[default_key]

def main():
    # ... (your main loop remains the same, it will now call the imported functions)
    while True:
        print("\n=== AI Assistant CLI ===")
        print("1. Answer Questions")
        print("2. Summarize Text")
        print("3. Generate Creative Content")
        print("4. Exit")
        choice = input("Select option: ")

        final_prompt = None
        func_map = {"1": "qa", "2": "summary", "3": "creative"}

        if choice in func_map:
            if choice == "1":
                user_input = input("Enter your question: ")
                variant, template = choose_prompt(qa_prompts)
                final_prompt = template.format(question=user_input)
            elif choice == "2":
                user_input = input("Enter text to summarize: ")
                variant, template = choose_prompt(summary_prompts)
                final_prompt = template.format(text=user_input)
            elif choice == "3":
                user_input = input("Enter story/poem/idea topic: ")
                variant, template = choose_prompt(creative_prompts)
                if variant == "few_shot":
                    final_prompt = template.format(theme=user_input)
                elif variant == "chain_of_thought":
                    final_prompt = template.format(hook=user_input)
                else:
                    final_prompt = template.format(topic=user_input)

            print("\n--- AI Response ---")
            response = get_ai_response(final_prompt)
            print(response)

            feedback = input("\nWas this helpful? (yes/no): ").lower()
            note = input("Optional note: ")
            save_feedback(func_map[choice], final_prompt, feedback == "yes", note)

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option.")
            continue

if __name__ == "__main__":
    main()