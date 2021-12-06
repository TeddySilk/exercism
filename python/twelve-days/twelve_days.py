verse_dict = {
    1: ['first', 'a Partridge in a Pear Tree'],
    2: ['second', 'two Turtle Doves'],
    3: ['third', 'three French Hens'],
    4: ['fourth', 'four Calling Birds'],
    5: ['fifth', 'five Gold Rings'],
    6: ['sixth', 'six Geese-a-Laying'],
    7: ['seventh', 'seven Swans-a-Swimming'],
    8: ['eighth', 'eight Maids-a-Milking'],
    9: ['ninth', 'nine Ladies Dancing'],
    10:['tenth', 'ten Lords-a-Leaping'],
    11:['eleventh', 'eleven Pipers Piping'],
    12:['twelfth', 'twelve Drummers Drumming']
}

def recite(start_verse, end_verse):
    output = []
    for verse in range(start_verse, end_verse + 1):
        elements = [verse_dict[i] for i in range(1, verse + 1)]
        day = f"On the {elements[verse-1][0]} day of Christmas my true love gave to me: "
        elements.reverse()
        if verse == 1:
            gifts = ", ".join([element[1] for element in elements]) + "."
        else:
            gifts = ", ".join([element[1] for element in elements if element[0] != 'first'])
            gifts = gifts + ", and " + elements[-1][1] + "."
        output.append(day + gifts)
        
    return output

print(recite(1,3))
