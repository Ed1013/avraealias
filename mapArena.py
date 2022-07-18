!alias normalMap multiline
!map -mapsize 21x14 -bg https://i.imgur.com/FCeRtJY.jpg -options c70
#reduce the image /4 25%

!alias placeMonsters <drac2>
args = &ARGS&

string = '\n'
if combat():
    string = f'map -t {args[0]} -move D4'
else:
  string = f'Not in combat...'

return string
</drac2>
