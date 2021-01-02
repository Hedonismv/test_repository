#Написать генератор песенки «TEN green bottles
#hanging on the wall».
#В песенке вместо цифр должны быть именно слова,
#обозначающие цифры, т.е. TEN, NINE, EIGHT, etc.

def song_generator():
    bottles = 10
    word = 'TEN'
    while bottles != -1:
        print(f"{word} green bottles hanging on the wall,")
        print(f"{word} green bottles hanging on the wall,")
        print(f"And if one green bottle should accidentally fall,")
        print(f"There'll be...")
        print(f" ")
        bottles -= 1
        if bottles == 9:
            word = 'NINE'
        elif bottles == 8:
            word = 'EIGHT'
        elif bottles == 7:
            word = 'SEVEN'
        elif bottles == 6:
            word = 'SIX'
        elif bottles == 5:
            word = 'FIVE'
        elif bottles == 4:
            word = 'FOUR'
        elif bottles == 3:
            word = 'THREE'
        elif bottles == 2:
            word = 'TWO'
        elif bottles == 1:
            word = 'ONE'
        elif bottles == 0:
            word = 'NO'
        print(f"{word} green bottles hanging on the wall...\n")

if __name__ == '__main__':
    song_generator()
