!serveralias join multiline
<drac2>
args = &ARGS&
ch=character()
lr=get_svar('longrest')
tokens = load_json(get_svar('charTokens'))
command = f'{ctx.prefix}init join -group Heroes'

if len(args) == 0:
    locs = ['e','f','g']
    location = f'{randchoice(locs)}{randint(5,10)}'
    command += f' -note "Location: {location} | Token: {tokens[ch.name.lower()]}" \n'
else:
    command += f' -note "Location: {args[0]} | Token: {tokens[ch.name.lower()]}" \n'

if lr == 'true':
    command += f'{ctx.prefix}game longrest \n'
else:
    command += f'{ctx.prefix}game shortrest \n'

command += f'{ctx.prefix}game hp max \n'
return command;
</drac2>
