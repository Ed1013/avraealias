!alias normalArena multiline
!init add 20 Map -p
!echo ```!map -mapsize 21x14 -bg https://i.imgur.com/FCeRtJY.jpg -options c70```
#reduce the image /4 25%

#add tokens to map
!map -t <nombre> -loadtoken <nombre> -move <position>

#add monsters
!map -t <nombre> -token <shortcode> -size <T,S,M,L,H,G> -move <position>

#summon celestial tokens
!alias celtoken echo ```!map -t celestial -token jbsct -size L```
