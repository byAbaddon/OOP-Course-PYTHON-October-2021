def start_playing(wrap):
    return wrap.play()


# --------------------------------------------
class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))

'''
Playing the guitar
'''
