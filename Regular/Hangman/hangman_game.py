import random
import re

films = [
    'Dilwale Dulhania Le Jayenge (1995)',
        'The Godfather (1972)',
        'Sholay (1975)',
        'Titanic (1997)',
        '3 Idiots (2009)',
        'The Shawshank Redemption (1994)',
        'Kabhi Khushi Kabhie Gham (2001)',
        'The Dark Knight (2008)',
        'Mughal-e-Azam (1960)',
        'Forrest Gump (1994)',
        'Lagaan (2001)',
        'Inception (2010)',
        'Pyaasa (1957)',
        'Gladiator (2000)',
        'Dangal (2016)',
        'The Matrix (1999)',
        'Gully Boy (2019)',
        'Pulp Fiction (1994)',
        'Chak De! India (2007)',
        'Fight Club (1999)',
        'Barfi! (2012)',
        "Schindler's List (1993)",
        'Taare Zameen Par (2007)',
        'The Lord of the Rings: The Return of the King (2003)',
        'Bajrangi Bhaijaan (2015)',
        'Saving Private Ryan (1998)',
        'Queen (2013)',
        'Avatar (2009)',
        'Zindagi Na Milegi Dobara (2011)',
        'The Silence of the Lambs (1991)',
        'PK (2014)',
        'The Lion King (1994)',
        'My Name Is Khan (2010)',
        'Jurassic Park (1993)',
        'Yeh Jawaani Hai Deewani (2013)',
        'The Avengers (2012)',
        'Kahaani (2012)',
        'Interstellar (2014)',
        'Bajirao Mastani (2015)',
        'Goodfellas (1990)',
        'Dil Chahta Hai (2001)',
        'Star Wars: Episode IV - A New Hope (1977)',
        'Andhadhun (2018)',
        'Braveheart (1995)',
        'Rang De Basanti (2006)',
        'Terminator 2: Judgment Day (1991)',
        'Gangs of Wasseypur (2012)',
        'The Wolf of Wall Street (2013)',
        'Rockstar (2011)',
        'The Social Network (2010)',
        'Uri: The Surgical Strike (2019)',
        'Mad Max: Fury Road (2015)',
        'Veer-Zaara (2004)',
        'Black Panther (2018)',
        'M.S. Dhoni: The Untold Story (2016)',
        'The Departed (2006)',
        'Swades (2004)',
        'The Revenant (2015)',
        'Devdas (2002)',
        'The Pursuit of Happyness (2006)',
        'Haider (2014)',
        'Gladiator (2000)',
        'Golmaal (2006)',
        'Finding Nemo (2003)',
        'Badhaai Ho (2018)',
        'Jaws (1975)',
        'Padmaavat (2018)',
        'The Truman Show (1998)',
        'Stree (2018)',
        'Good Will Hunting (1997)',
        'Dhoom 3 (2013)',
        'La La Land (2016)',
        'Raazi (2018)',
        'American Beauty (1999)',
        'Hera Pheri (2000)',
        'The Grand Budapest Hotel (2014)',
        'OMG : Oh My God! (2012)',
        'The Great Gatsby (2013)',
        'Drishyam (2015)',
        'No Country for Old Men (2007)',
        'Simmba (2018)',
        'Slumdog Millionaire (2008)',
        'Jab We Met (2007)',
        'Toy Story (1995)',
        'Airlift (2016)',
        'Back to the Future (1988)',
        'Neerja (2016)',
        'The Curious Case of Benjamin Button (2008)',
        'Rockstar (2011)',
        'The Sixth Sense (1999)',
        'Yeh Jawaani Hai Deewani (2013)',
        'A Beautiful Mind (2001)',
        'Toilet: Ek Prem Katha (2017)',
        'Pirates of the Caribbean: The Curse of the Black Pearl (2003)',
        'Munna Bhai M.B.B.S. (2003)',
        'The Prestige (2006)',
        'Gully Boy (2019)',
        'Shawshank Redemption (1994)',
        'Tumbbad (2018)',
        'The Green Mile (1999)'

]


def main():
    input('\nHello, press enter to play hangman!')
    print('\nEnter -e or --exit to end game')
    print('Enter -r or --retry to restart game with another movie.\n\n')

    
    # select a random movie
    movie, year = select_movie(films)

    # print movie name and year - DEMO
    # print(f'(Demo purpose - Movie name : {movie})\n')
    
    # frame question with blanks
    ques = question(movie)

    # create list of moviename
    movie_list = [letter for letter in movie]

    # run game and get result
    res = game(ques, movie_list, year)

    if res == 'exit':
        print('Game Ended.')
        return
    if res == True or res == False: 
        print(get_result(res))


def select_movie(films):
    movie = random.choices(films)
    
    if search := re.search(r'^([A-Za-z0-9_.-:,\' ]*) \((\d{4})\)$', movie[0]):
        return search.groups()


def question(movie_name):
    q = []
    for letter in movie_name:
        if letter.isalpha() or letter.isnumeric():
            q.append('_')
        else:
            q.append(letter)

    return q


def game(question, movie, year):

    # create moviename in str
    moviename = ''.join(map(str, movie)).strip().lower()

    # copy moviename list 
    moviecp = movie.copy()

    # create a list of all elements of movie in lowercase
    lower_movie = [x.lower() for x in movie]
    
    # initiate counter
    count = 1
    hint = False

    while count < 11 and '_' in question:
        print(*question, '\n')

        if count > 5 and hint == False:
            print('To get hint, enter \'--hint\'\n')

        answer = input(f'Guess a character or the movie name ({11-count} chances left): ').lower().strip()

        if answer == '--hint' and count > 5 and hint == False:
            print(f'The movie was released in {year}\n')
            hint = True
        
        elif answer == '--exit' or answer == '-e' or answer == '--quit':
            return 'exit'

        elif answer == '-r' or answer == '--retry':
            print('\n')
            return main()

        elif answer in lower_movie:
            while answer in lower_movie:
                index = lower_movie.index(answer)
                question[index] =  moviecp[index]
                lower_movie[index] = 'NULL'

        elif answer == moviename:
            question=moviecp.copy()
            break

        else:
            # if wrong guess increase counter
            count+=1
        
    if count < 11:
        print(*question,'\n')
        return True
    return False


def get_result(result):
    if result:
        return 'Correct!'
    else:
        return 'Incorrect, try again!'


if __name__ == "__main__":
    main()