!serveralias join multiline
<drac2>
args = &ARGS&
ch=character()
tokens = load_json(get_svar('charTokens'))
command = f'init join -group Heroes'

if len(args) == 0:
    locs = ['e','f','g']
    location = f'{randchoice(locs)}{randint(5,10)}'
    command += f' -note "Location: {location} | Token: {tokens[ch.name.lower()]}"'
else:
    command += f' -note "Location: {args[0]} | Token: {tokens[ch.name.lower()]}"'

return command;
</drac2>
!game shortrest
!game hp max
