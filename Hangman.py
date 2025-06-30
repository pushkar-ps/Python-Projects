from pyfiglet import figlet_format as figlet
from termcolor import cprint, colored
import random

# Game Title
cprint(figlet("Hangman"), "blue")
cprint("Enter 'Ctrl + C' or '^C' at any time to quit.\n", "red")

# Random word setup
words_with_hints = {
    # 🔥 Superheroes & Fiction
    "batman": "A caped crusader who fights crime in Gotham.",
    "spiderman": "Bitten by a radioactive spider.",
    "ironman": "Genius billionaire with an arc reactor.",
    "hulk": "Don’t make him angry!",
    "thor": "The god of thunder with a hammer.",
    "joker": "Laughs a lot, but he’s no joke.",
    "groot": "I am...?",
    "thanos": "Snapped half the universe.",
    "goku": "Saiyan who loves to fight.",
    "naruto": "Hidden leaf ninja with a fox inside.",

    # 🤣 Funny & Internet Culture
    "meme": "Funny image or video shared online.",
    "banana": "A yellow fruit that monkeys love.",
    "noob": "Beginner who doesn’t know much (yet).",
    "sus": "Short for suspicious (Among Us).",
    "emoji": "Used to express feelings via text.",
    # "yeet": "To throw something forcefully (and funnily).",

    # 💻 Tech & Programming
    "python": "A powerful and beginner-friendly programming language.",
    "linux": "An open-source operating system.",
    "github": "Where coders share and store code.",
    "binary": "Language of computers: 1s and 0s.",
    "stack": "A data structure. Last in, first out.",
    "loop": "Keeps running until you tell it to stop.",
    "html": "Markup language for building websites.",
    "java": "A programming language (not coffee).",
    "router": "Directs traffic... on your Wi-Fi!",
    "bug": "An error in code, not an insect.",
    "compiler": "Turns human code into machine code.",

    # 🌍 Geography & Nature
    "volcano": "Erupts with lava and fire.",
    "desert": "Very hot, very dry... lots of sand.",
    "island": "Land surrounded by water.",
    "ocean": "Big blue mystery.",
    "mountain": "Go climb one for adventure!",
    "earthquake": "The ground starts shaking... run!",

    # 🎬 Pop Culture & Brands
    "netflix": "Watch series, movies, and chill.",
    "apple": "Steve Jobs started this fruity company.",
    "google": "It knows everything. Literally.",
    "tesla": "Electric cars and Elon Musk.",
    "youtube": "Video site that never ends.",
    "pixar": "Famous animation studio. Think Toy Story!",
    # "harrypotter": "Wizard boy with a lightning scar.",

    # 🚀 Space & Science
    "galaxy": "A system of stars... billions of them.",
    "neutron": "A neutral subatomic particle.",
    "rocket": "Goes to space. Loud and fast.",
    "gravity": "Keeps your feet on the ground.",
    "satellite": "Orbits Earth and helps GPS.",
    "blackhole": "Even light can’t escape it.",
    "nasa": "US space agency. Moon stuff.",

    # 👨‍💻 Famous People
    "einstein": "E=mc² guy. Genius alert!",
    "zuckerberg": "Created Facebook in his dorm.",
    "billgates": "Microsoft founder and philanthropist.",
    "stevejobs": "Visionary behind Apple.",
    "elonmusk": "Tesla, SpaceX, X... need we say more?",

    # 🧠 Brainy & Random
    "philosophy": "Thinking deeply. Like, really deeply.",
    "creativity": "Inventing something new and original.",
    "motivation": "What drives you to keep going.",
    "focus": "Stay on task. Don’t get distracted!",
    "rhythm": "It’s got the beat!",
    "illusion": "Your brain gets tricked.",
    "future": "What’s coming next.",
    "discipline": "Doing what needs to be done, even when you don’t feel like it.",
    "focus": "Your weapon for achieving greatness — avoid distractions.",
    "grit": "Courage and persistence, even when things get tough.",
    "vision": "A clear mental image of what you want to achieve.",
    "consistency": "Doing small things every day, like a machine.",
    "ambition": "A fire inside you to become the best.",
    "habit": "Something you do daily, that builds your future.",
    "curiosity": "What drives you to learn and grow.",
    "patience": "Waiting without frustration. Power of calm.",
    "failure": "Not the end — just a lesson in disguise.",
    "oxygen": "You breathe it every second — invisible but vital.",
    "gravity": "Keeps your feet on Earth (and dreams grounded).",
    "mirror": "It reflects… and reveals.",
    "echo": "Sound bouncing back at you — like a ghost reply.",
    "pyramid": "Ancient triangle-shaped wonder built in Egypt.",
    "language": "What humans use to share thoughts and emotions.",
    "keyboard": "Your tool for creation, communication, and memes.",
    "atlas": "A book or app full of maps.",
    "eclipse": "When the moon or sun gets blocked.",
    "clock": "Tells time — and steals it too.",
    # "yeet": "To throw something with confidence and no regrets.",
    "bruh": "Universal word for 'really?' moments.",
    "cringe": "Something so awkward, it hurts to watch.",
    "vibe": "The energy or mood of a person or place.",
    "zoom": "App we all lived on during lockdown.",
    "captcha": "Little puzzles proving you’re not a robot.",
    "emoji": "A tiny face that expresses big emotions.",
    "sleep": "What every programmer sacrifices for deadlines.",
    "procrastinate": "I'll do it… later.",
    "glitch": "A weird error, like reality broke a little.",
    "mandela": "Leader who forgave after 27 years in prison.",
    "tata": "Indian businessman known for ethics and vision.",
    "obama": "First Black US President. Power of calm words.",
    "musk": "Rockets, cars, brain chips — he’s everywhere.",
    "galileo": "Showed us the Earth wasn’t the center.",
    "daVinci": "Inventor and painter of the future in the past.",
    "rahuldravid": "Mr. Dependable of Indian cricket.",
    "ratan": "A name that means responsibility, values, and empire.",
    "neuralink": "Musk’s project to connect brains and machines.",
    "tesla": "Inventor from the past. Power from the future."
}

Points = 0

while True:
    word, hint = random.choice(list(words_with_hints.items()))
    guessed_word = [word[i] if i == 0 else '_' for i in range(len(word))]

    cprint(f"Hint: {hint}", "grey", attrs=["bold"])
    cprint(f"First Letter: {word[0]}", "cyan", attrs=["bold"])
    print()

    # Word guessing loop
    while "_" in guessed_word:
        print(" ".join(guessed_word))
        print()
        usrGuess = input(colored("Guess a letter: ", "yellow")).lower()

        if usrGuess in word:
            for i in range(len(word)):
                if word[i] == usrGuess:
                    guessed_word[i] = usrGuess
        else:
            cprint("Wrong guess!", "red")

    # Word complete
    Points += 1
    print()
    cprint(" ".join(guessed_word), "cyan")
    cprint(f"🎉 Congratulations! You completed the word: {word}", "green")
    cprint(f"You Score Is {Points}, You Solved {Points} Words","white",attrs=["bold"])
    print()
    
    
    

# My GAME CODE ##########################
# cprint(figlet("Hangman"),"blue")
# cprint("Enter 'Ctrl + C' or '^C'at any time to quit.\n","red")

# words = ("batman", "pushkar", "hero")
# word = words[random.randint(0, len(words) - 1)]
# guessed_word = ['_' for _ in word]


# while "_" in guessed_word:
#     print(guessed_word)
#     usrGuess = input(colored("Guess A Letter: ","yellow")).lower()

#     for i in range(len(word)):
#         if usrGuess == word[i]:
#             guessed_word[i] = usrGuess

# cprint(guessed_word)
# cprint(f"Congrulation You Complete The Word {word}","green")

