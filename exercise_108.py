# Dictionary basics :D
#1 - Define a dictionary call story1, it should have the followign keys:
        # start, middle and end
story_dict = {'start': 'In the beginning there was a hero named bob',
              'middle': 'as he fought on with the evil wizard his bald head kept shining like a cue ball',
              'end': 'the hero bob slipped and landed on the edge of his own sword....the end'
              }
#2 - Print the entire dictionary
print(story_dict)
#3 - Print the type of your dictionary
print(type(story_dict))

#4 - Print only the keys
print(story_dict.keys())

#4 - print only the values
print(story_dict.values())

#5 - print the individual values using the keys (individually, lots of printing commands)
print(story_dict['start'])
print(story_dict['middle'])
print(story_dict['end'])

#6 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero
story_dict['hero'] = 'BOB'
print(story_dict['hero'])
