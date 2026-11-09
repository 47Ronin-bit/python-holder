import pickle
import random
 
# Global constants
CAPITALS_FILE = 'capitals.dat'
RESULTS_FILE = 'game_results.dat'
QUIT = 'q'
 
 
def create_capitals():
    # Create a dictionary with the state name as the key
    # and the capital as the value.
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
                'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
                'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover',
                'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
                'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
                'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
                'Maine': 'Augusta', 'Maryland': 'Annapolis',
                'Massachusetts': 'Boston', 'Michigan': 'Lansing',
                'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
                'Missouri': 'Jefferson City', 'Montana': 'Helena',
                'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
                'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                'New Mexico': 'Santa Fe', 'New York': 'Albany',
                'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
                'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
                'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
                'Texas': 'Austin', 'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier', 'Virginia': 'Richmond',
                'Washington': 'Olympia', 'West Virginia': 'Charleston',
                'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    return capitals
 
 
def save_capitals(capitals):
    # Serialize (pickle) the dictionary to a binary file.
    output_file = open(CAPITALS_FILE, 'wb')
    pickle.dump(capitals, output_file)
    output_file.close()
 
 
def load_capitals():
    # Deserialize (unpickle) the dictionary from the binary file.
    input_file = open(CAPITALS_FILE, 'rb')
    capitals = pickle.load(input_file)
    input_file.close()
    return capitals
 
 
def load_results():
    # Read every pickled game result until the end of the file.
    # Return an empty list if no results have been saved yet.
    results = []
 
    try:
        input_file = open(RESULTS_FILE, 'rb')
    except IOError:
        return results
 
    end_of_file = False
    while not end_of_file:
        try:
            results.append(pickle.load(input_file))
        except EOFError:
            end_of_file = True
 
    input_file.close()
    return results
 
 
def save_results(results):
    # Pickle each game result, one after another, into the file.
    output_file = open(RESULTS_FILE, 'wb')
    for result in results:
        pickle.dump(result, output_file)
    output_file.close()
 
 
def play_game(capitals):
    # Quiz the user until they quit. Return the game's results.
    states = list(capitals.keys())
    correct_count = 0
    incorrect_count = 0
    correct_states = set()    # a set ignores repeated correct answers
    missed_states = {}        # state name -> number of times missed
 
    
 
    # Randomly select the first state
    state = states[random.randint(0, len(states) - 1)]
    answer = input('What is the capital of ' + state + '?(you can press q at any time to quit) ')
 
    while answer.lower() != QUIT:
        # Compare the answer to the capital, ignoring case and spaces
        if answer.strip().lower() == capitals[state].lower():
            print('Correct!\n')
            correct_count += 1
            correct_states.add(state)
        else:
            print('Incorrect.')
            incorrect_count += 1
            missed_states[state] = missed_states.get(state, 0) + 1
 
        # Randomly select the next state
        state = states[random.randint(0, len(states) - 1)]
        answer = input('What is the capital of ' + state + '? (you can press q at any time to quit) ')
 
    result = {'correct': correct_count,
              'incorrect': incorrect_count,
              'correct_states': correct_states,
              'missed_states': missed_states}
    return result
 
 
def show_summary(result):
    # show the results of the game
   
    print('You got ', result['correct'], 'correct and ', result['incorrect'], 'incorrect.')
 
 
def main():
    # Create the dictionary, pickle it, and then unpickle it for use.
    save_capitals(create_capitals())
    capitals = load_capitals()
 
    # Play the game and shows the result
    result = play_game(capitals)
    show_summary(result)
 
 
# Call the main function
main()