##### HANGMAN GAME By Michael #####
import random
word_list = ['ADULT', 'AEROPLANE', 'AIR', 'AIRCRAFT', 'CARRIER', 'AIRFORCE', 'AIRPORT', 'ALBUM', 'ALPHABET', 'APPLE', 'ARM', 'ARMY', 'BABY', 'BACKPACK', 'BALLOON', 'BANANA', 'BANK', 'BARBECUE',
             'BATHROOM', 'BATHTUB', 'BED', 'BED', 'BEE', 'BIBLE', 'BIBLE', 'BIRD', 'BOMB', 'BOOK', 'BOSS', 'BOTTLE', 'BOWL', 'BOX', 'BOY', 'BRAIN', 'BRIDGE', 'BUTTERFLY', 'BUTTON', 'CAPPUCCINO',
             'CAR', 'CARPET', 'CARROT', 'CAVE', 'CHAIR', 'CHESS', 'BOARD', 'CHIEF', 'CHILD', 'CHISEL', 'CHOCOLATES', 'CHURCH', 'CHURCH', 'CIRCLE', 'CIRCUS', 'CIRCUS', 'CLOCK', 'CLOWN', 'COFFEE',
             'COMET', 'COMPACT', 'DISC', 'COMPASS', 'COMPUTER', 'CRYSTAL', 'CUP', 'CYCLE', 'DATA', 'BASE', 'DESK', 'DIAMOND', 'DRESS', 'DRILL', 'DRINK', 'DRUM', 'DUNG', 'EARS', 'EARTH', 'EGG',
             'ELECTRICITY', 'ELEPHANT', 'ERASER', 'EXPLOSIVE', 'EYES', 'FAMILY', 'FAN', 'FEATHER', 'FESTIVAL', 'FILM', 'FINGER', 'FIRE', 'FLOODLIGHT', 'FLOWER', 'FOOT', 'FORK', 'FREEWAY', 'FRUIT',
             'FUNGUS', 'GAME', 'GARDEN', 'GAS', 'GATE', 'GEMSTONE', 'GIRL', 'GLOVES', 'GOD', 'GRAPES', 'GUITAR', 'HAMMER', 'HAT', 'HIEROGLYPH', 'HIGHWAY', 'HOROSCOPE', 'HORSE', 'HOSE', 'ICE',
             'INSECT', 'JET', 'FIGHTER', 'JUNK', 'KALEIDOSCOPE', 'KITCHEN', 'KNIFE', 'LEATHER', 'JACKET', 'LEG', 'LIBRARY', 'LIQUID', 'MAGNET', 'MAN', 'MAP', 'MAZE', 'MEAT', 'METEOR', 'MICROSCOPE',
             'MILK', 'MILKSHAKE', 'MIST', 'MONEY', 'MONSTER', 'MOSQUITO', 'MOUTH', 'NAIL', 'NAVY', 'NECKLACE', 'NEEDLE', 'ONION', 'PAINTBRUSH', 'PANTS', 'PARACHUTE', 'PASSPORT', 'PEBBLE', 'PENDULUM',
             'PEPPER', 'PERFUME', 'PILLOW', 'PLANE', 'PLANET', 'POCKET', 'POTATO', 'PRINTER', 'PRISON', 'PYRAMID', 'RADAR', 'RAINBOW', 'RECORD', 'RESTAURANT', 'RIFLE', 'RING', 'ROBOT', 'ROCK',
             'ROCKET', 'ROOF', 'ROOM', 'ROPE', 'SADDLE', 'SALT', 'SANDPAPER', 'SANDWICH', 'SATELLITE', 'SCHOOL', 'SEX', 'SHIP', 'SHOES', 'SHOP', 'SHOWER', 'SIGNATURE', 'SKELETON', 'SLAVE', 'SNAIL',
             'SOFTWARE', 'SOLID', 'SPACE', 'SHUTTLE', 'SPECTRUM', 'SPHERE', 'SPICE', 'SPIRAL', 'SPOON', 'SPOT', 'LIGHT', 'SQUARE', 'STAIRCASE', 'STAR', 'STOMACH', 'SUN', 'SUNGLASSES', 'SURVEYOR',
             'SWIMMING', 'POOL', 'SWORD', 'TABLE', 'TAPESTRY', 'TEETH', 'TELESCOPE', 'TELEVISION', 'TENNIS', 'RACQUET', 'THERMOMETER', 'TIGER', 'TOILET', 'TONGUE', 'TORCH', 'TORPEDO', 'TRAIN',
             'TREADMILL', 'TRIANGLE', 'TUNNEL', 'TYPEWRITER', 'UMBRELLA', 'VACUUM', 'VAMPIRE', 'VIDEOTAPE', 'VULTURE', 'WATER', 'WEAPON', 'WEB', 'WHEELCHAIR', 'WINDOW', 'WOMAN', 'WORM']
word = list(word_list[random.randrange(len(word_list) - 1)])
out_word = word
out = ""
for num in range(len(word)):
    out +=  " _"
guess = 0
while guess < 10 and "_" in out:
    ask = input("Guess: ")
    if ask in word:
        for num in word:
            if num is ask:
                x = word.index(num)
                word[x] = "0"
                out = list(out)
                out[(x * 2) + 1] = ask 
                out = "".join(out)
    else:
        guess += 1
    print(out)
if "_" not in (out):
    print("You win!")
else:
    print("You lose!")
    print("The word is", "".join(out_word))