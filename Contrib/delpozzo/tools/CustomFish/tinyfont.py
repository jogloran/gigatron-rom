
#-----------------------------------------------------------------------
#
#       tinyfont.py -- a very small font
#
#-----------------------------------------------------------------------
#
#  Description:
#
#       The tiny font is an 3x5 pixel monospaced font where each character
#       is placed in a box of 4x6 pixels. At the native 160x120 Gigatron
#       resolution we can display 40x20 characters.
#
#       The encoding has 3x5 bits for the pixels and 1 shift bit to indicate
#       an overall shift down for characters g, j, p, q and y. The lowercase
#       j needs special handling. This scheme gives 2 bytes per character,
#       for a total of 192 bytes.
#
#  References:
#
#       http://vt100.tarunz.org
#       VT100 Terminal for Pilot (Brian J. Swetland)
#
#       https://robey.lag.net/2010/01/23/tiny-monospace-font.html
#       A very tiny, monospace, bitmap font (Robey Pointer)
#
#       https://fonts2u.com/small-5x3-regular.font
#       Small 5X3 regular (soxhead2000)
#
#       https://github.com/olikraus/u8g2
#       U8glib library for monochrome displays, version 2
#
#  History:
#
#       2018-08-01 (marcelk) Initial version inspired by open source examples
#       2018-08-xx (marcelk) Update of @corz
#
#-----------------------------------------------------------------------

def convert(font):
  for c in range(96):
    i, j = c % 16, c // 16
    word, shift = 0, 0
    for y in range(6):
      for x in range(3):
        p = ((j * 6 + y) * 16 + i) * 4 + x + 1
        if font[p] == '@':
          if y == 5 and shift == 0:
            shift, word = 1, word << 1
          word |= 1 << (5*(3-x) - y - 1 + shift)
    if shift == 0:
      print(' 0x%04x,' % word, end='')
    else:
      print('-0x%04x,' % (0x8000 - word), end='')
    print(' // %s' % repr(chr(32+c)))

tinyfont =\
    '......@..@.@.@.@..@@.@....@...@....@.@..........................'\
    '......@..@.@.@@@.@@....@.@.@..@...@...@..@.@..@................@'\
    '......@......@.@..@@..@...@.......@...@...@..@@@.....@@@......@.'\
    '.............@@@.@@..@...@.@......@...@..@.@..@...@..........@..'\
    '......@......@.@..@....@..@@.......@.@...........@........@.....'\
    '................................................................'\
    '..@@..@..@@..@@..@.@.@@@..@@.@@@.@@@.@@@...........@.....@...@@@'\
    '.@.@.@@....@...@.@.@.@...@.....@.@.@.@.@..@...@...@..@@@..@....@'\
    '.@.@..@...@..@@..@@@.@@..@@@..@..@@@.@@@.........@.........@..@.'\
    '.@.@..@..@.....@...@...@.@.@.@...@.@...@..@...@...@..@@@..@.....'\
    '.@@..@@@.@@@.@@....@.@@..@@@.@...@@@.@@......@.....@.....@....@.'\
    '................................................................'\
    '..@@..@..@@...@@.@@..@@@.@@@..@@.@.@.@@@..@@.@.@.@...@.@.@.@.@@@'\
    '.@.@.@.@.@.@.@...@.@.@...@...@...@.@..@....@.@.@.@...@@@.@@@.@.@'\
    '.@.@.@@@.@@..@...@.@.@@..@@..@.@.@@@..@....@.@@..@...@@@.@@@.@.@'\
    '.@...@.@.@.@.@...@.@.@...@...@.@.@.@..@..@.@.@.@.@...@.@.@@@.@.@'\
    '..@@.@.@.@@...@@.@@..@@@.@...@@@.@.@.@@@..@..@.@.@@@.@.@.@.@.@@@'\
    '................................................................'\
    '.@@...@..@@...@@.@@@.@.@.@.@.@.@.@.@.@.@.@@@..@@.....@@...@.....'\
    '.@.@.@.@.@.@.@....@..@.@.@.@.@.@.@.@.@.@...@..@..@....@..@.@....'\
    '.@.@.@.@.@@@..@...@..@.@.@.@.@@@..@..@@@..@...@...@...@.........'\
    '.@@..@@@.@@....@..@..@.@.@.@.@@@.@.@..@..@....@....@..@.........'\
    '.@....@@.@.@.@@...@..@@@..@..@.@.@.@..@..@@@..@@.....@@......@@@'\
    '................................................................'\
    '.@.......@.........@.......@.....@....@....O.@...@@.............'\
    '..@...@@.@@...@@..@@..@@..@...@@.@@..........@.@..@..@@@.@@...@.'\
    '.....@.@.@.@.@...@.@.@.@.@@@.@.@.@.@.@@...@@.@@...@..@@@.@.@.@.@'\
    '.....@.@.@.@.@...@.@.@@...@..@@@.@.@..@....@.@.@..@..@@@.@.@.@.@'\
    '.....@@@.@@...@@..@@..@@..@....@.@.@.@@@.@.@.@.@.@@@.@.@.@.@..@.'\
    '..............................@.......... @.....................'\
    '..................@...........................@@..@..@@...@@.@@@'\
    '.@@...@@.@.@..@@.@@@.@.@.@.@.@.@.@.@.@.@.@@@..@...@...@..@@..@@@'\
    '.@.@.@.@.@@..@@...@..@.@.@.@.@@@..@..@.@...@.@@...@...@@.....@@@'\
    '.@.@.@.@.@....@@..@..@.@.@@@.@@@..@...@@..@...@...@...@......@@@'\
    '.@@...@@.@...@@...@@..@@..@..@@@.@.@...@.@@@..@@..@..@@......@@@'\
    '.@.....@..............................@.........................'

print('// Generated by tinyfont.py')
convert(tinyfont)

