'''2) skill1={'Java', 'C', 'SQL', 'Python'}
    skill2={'Python', 'C++', 'ASP.net', 'VC++', 'SQL'}
    skill3={'Spr boot', 'Java', 'HTML', 'CSS', 'JavaScript'}

    process the THREE skill1 list out ALL the skills the orgz has
    what are the skills common between skill1 and skill2 then skill1 and skill3?
    what are the skills commong between all the skill sets:  1, 2, 3 ?'''

skill1 = {'Java', 'C', 'SQL', 'Python'}
skill2 = {'Python', 'C++', 'ASP.net', 'VC++', 'SQL'}
skill3 = {'Spr boot', 'Java', 'HTML', 'CSS', 'JavaScript'}

skill1 = set(list(skill1)[:3])
print(skill1)
print('skill common between skill1 and skill2:', (skill1.intersection(skill2)))
print('skills common between skill1 and skill2:', skill1.intersection(skill3))
print('skills common between all the skill sets:  1, 2, 3:',
      skill1.intersection(skill2).intersection(skill3))
