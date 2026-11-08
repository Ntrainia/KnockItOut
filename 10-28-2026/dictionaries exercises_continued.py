# 6.3 Glossary
glossary = {'dictionary': 'An associative array, where arbitrary keys are mapped to values.',
            'key': 'A value that identifies an entry in a mapping.',
            'list': 'A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).',
            'object': 'Any data with state(attributes or value) and defined behaviors (methods). Also the ultimate base class of any new-style class',
            'type': 'The type of a Python object determines what kind of object it is; every object has a type'}
print("\nDictionary: " + glossary['dictionary'])
print("\nKey: " + glossary['key'])
print("\nList: " + glossary['list'])
print("\nObject: " + glossary['object'])
print("\nType: " + glossary['type'])

# 6.4 Glossary 2
glossary['indentation'] = 'Refers to the spaces at the beginning of a code line'
glossary['comments'] = 'Code lines that will not be executed'
words = ['dictionary', 'key', 'list', 'object', 'type']
for word in glossary.keys():
    if word in words :
        print("\n" + word.title() + ": " + glossary[word])

#