#include current monster image in thumbnail
!snippet monimg -thumb <drac2>
    c=load_json(combat().get_metadata("monImgs"))
    m=get('name')
</drac2>
{{c[m]}}

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