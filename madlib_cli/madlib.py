import re
def read_template(path):
   # with open('assets/dark_and_stormy_night_template.txt', 'rb') as example:

    try:
       with open(path, 'r') as example:
        sentence = example.read()
        return sentence
    except FileNotFoundError:
        raise FileNotFoundError(f'Could not find the file at the provided path: {path}')


def parse_template(string):

    new_string = string

    pattern = r'\{([A-Za-z\s\d]+)\}'

    matches = re.findall(pattern, string)
    parts_tuple = tuple(matches)

    stripped_string = re.sub(pattern, '{}', new_string)

    return stripped_string, parts_tuple


def merge(template, data):
    if isinstance(data, tuple):
        story = template.format(*data)
        return story
    elif isinstance(data, dict):
        story = template.format(**data)
        return story
    elif isinstance(data, list):
        story = template.format(*data)
        return story
    else:
        raise TypeError('Unsupported data type. First argument must be a string. Second argument must be a tuple, list, or dictionary.')

def write_new_story_file(story):
    file_name = "my_story.txt"
    file_number = 1
    while True:
        try:
            with open(file_name, 'x') as f:
                f.write(story)
                print(f"File '{file_name}' created successfully.")
                break
        except FileExistsError:
            file_number += 1
            file_name = f"my_story_{file_number}.txt"






def print_definitions():
    def_input = input('Forget what this word means? Type y to see a list of word types, type n to keep playing.')
    def_input = def_input.strip()
    def_input = def_input.lower()

    if def_input == 'y':
        print("""
        *A 'plural noun' is a noun that refers to more than one person, place, thing, or idea.
        *Example: apple = noun, apples = plural noun
        
        *An 'adjective' is a word that describes the qualities or states of being of a noun.
        * Example: a yellow banana,  yellow = adjective & banana = noun
        """)

    elif def_input == 'n':
        return True
    else:
        print('Sorry, I did not understand your command. Please enter y for yes, n for no.')


template1 = read_template('/Users/maddielewis/401/madlib-cli/assets/make_me_a_video_game.txt')
template2 = read_template('/Users/maddielewis/401/madlib-cli/assets/dark_and_stormy_night_template.txt')

def main_program_loop():
    print("""**************************************
        **    Welcome to Mad Libs!  **
        **    In this game, you will be provided with inputs
           to help you build a story. You will be given a general prompt
           like "adjective" or "noun", which you may fill in with whatever you like,
           so long as it fits the type of word for that prompt.**
        ** After you have filled in all the prompts, the program will return your story 
        to you, and save it as a text file in this folder for future use. **
        **
        ** Don't worry about the end result, this game is about the journey!**
        ** If you don't understand the prompt, please type "help" to see some definitions.
        **************************************""")

    print("Let's begin.")

    while True:
        parsed_template, user_prompts = parse_template(template1)
        user_answers = []

        for user_prompt in user_prompts:
            print("Please enter a ", user_prompt, ". :)")
            word_input = input('>')
            word_input = word_input.strip()

            if word_input.lower() == 'help':
                print_definitions()
            elif word_input.lower() == '':
                print('Sorry, please try that prompt again.')
            else:
                user_answers.append(word_input)

        if len(user_answers) == len(user_prompts):
            print("""
            Huzzah, you've completed the prompts!
            Let's see your story.""")

            print("Number of prompts:", len(user_prompts))
            print("Number of answers:", len(user_answers))
            new_story = merge(parsed_template, user_answers)

            write_new_story_file(new_story)
            print(new_story)
            break  # Exit the loop when all answers are provided


if __name__ == "__main__":
    main_program_loop()
