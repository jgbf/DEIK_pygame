
FPS = 30 # Itt be tudjatok allitani a madar zuhanasi sebesseget -> nagyobb szam gyorsabb zuhanas
PIPEGAPSIZE  = 100 # Hely az also es a felso cso kozott -> nagyobb szam nagyobb hely

IMAGES, SOUNDS, HITMASKS = {}, {}, {}

SCREENWIDTH  = 288
SCREENHEIGHT = 512
BASEY        = SCREENHEIGHT * 0.79
PLAYERS_LIST = [
    (
        'assets/sprites/bluebird-midflap.png',
        'assets/sprites/bluebird-midflap.png',
        'assets/sprites/bluebird-midflap.png',
    )
]

BACKGROUNDS_LIST = ['assets/sprites/background-day.png']
PIPES_LIST = ['assets/sprites/pipe-green.png']

try:
    xrange
except NameError:
    xrange = range
