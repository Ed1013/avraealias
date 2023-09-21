#include current monster image in thumbnail
!snippet monimg -thumb <drac2>
    c=load_json(combat().get_metadata("monImgs"))
    m=get('name')
    i=c.get(m)
    if i is not None:
        image = i
    else: 
        image = "https://i.imgur.com/qOTuihZ.png"
</drac2>
{{image}}

#target all in one area
!serversnippet -area <drac2>
args = &ARGS&
areanum = int(args[len(args)-1])-1
targets = f'testing{areanum}'
areas = load_json(combat().get_metadata("combatAreas"))

for a in areas[areanum].members:
    targets+=f' -t {a}'

return targets
</drac2>