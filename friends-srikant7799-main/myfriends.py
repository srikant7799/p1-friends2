"""Assignment 1: Friend of a Friend

Please complete these functions, to answer queries given a dataset of
friendship relations, that meet the specifications of the handout
and docstrings below.

Notes:
- you should create and test your own scenarios to fully test your functions, 
  including testing of "edge cases"
"""

from py_friends.friends import Friends

"""
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************

If you worked in a group on this project, please type the EIDs of your groupmates below (do not include yourself).
Leave it as TODO otherwise.
Groupmate 1: bkm2384
Groupmate 2: TODO
"""

def load_pairs(filename):
    """
    Args:
        filename (str): name of input file

    Returns:
        List of pairs, where each pair is a Tuple of two strings

    Notes:
    - Each non-empty line in the input file contains two strings, that
      are separated by one or more space characters.
    - You should remove whitespace characters, and skip over empty input lines.
    """
    list_of_pairs = []
    with open(filename, 'rt') as infile:

# ------------ BEGIN YOUR CODE ------------

        list_of_pairs = infile.readlines()
        for i in range(len(list_of_pairs)):
            list_of_pairs[i] = list_of_pairs[i].rstrip()
            list_of_pairs[i] = tuple(list_of_pairs[i].split(" "))
            list_of_pairs = list(list_of_pairs)





# ------------ END YOUR CODE ------------

    return list_of_pairs


def make_friends_directory(pairs):
    """Create a directory of persons, for looking up immediate friends

    Args:
        pairs (List[Tuple[str, str]]): list of pairs

    Returns:
        Dict[str, Set] where each key is a o, with value being the set of 
        related persons given in the input list of pairs

    Notes:
    - you should infer from the input that relationships are two-way: 
      if given a pair (x,y), then assume that y is a friend of x, and x is 
      a friend of y
    - no own-relationships: ignore pairs of the form (x, x)
    """
    directory = dict()



    # ------------ BEGIN YOUR CODE ------------


    for o in pairs:

        if o[0] != o[1]:

            if o[0] in directory:
                directory[o[0]].update(set(o[1:]))
            else:
                directory[o[0]] = set(o[1:])
            if o[1] in directory:
                directory[o[1]].update(set(o[0:]))
            else:
                directory[o[1]] = set(o[0:])

    for x in directory:
        if x in directory[x]:
            directory[x].remove(x)

    # ------------ END YOUR CODE ------------
    return directory


def find_all_number_of_friends(my_dir):
    """List every person in the directory by the number of friends each has

    Returns a sorted (in decreasing order by number of friends) list 
    of 2-tuples, where each tuples has the person's name as the first element,
    the  number of friends as the second element.
    """
    friends_list = []

    # ------------ BEGIN YOUR CODE -----------
    q = dict(my_dir)
    x = q.keys()
    count=(len(x))

    for x in q:

        m = len(q[(str(x))])
        temptup=(x,m)
        friends_list.append(temptup)


    lenlis=len(friends_list)





    friends_list = sorted (friends_list, key=lambda dta:(-dta[1],dta[0]))

    # ------------ END YOUR CODE ------------

    return friends_list


def make_team_roster(person, my_dir):
    """Returns str encoding of a person's team of friends of friends
    Args:
        person (str): the team leader's name
        my_dir (Dict): dictionary of all relationships

    Returns:
        str of the form 'A_B_D_G' where the underscore '_' is the
        separator character, and the first substring is the 
        team leader's name, i.e. A.  Subsequent unique substrings are 
        friends of A or friends of friends of A, in ascii order
        and excluding the team leader's name (i.e. A only appears
        as the first substring)

    Notes:
    - Team is drawn from only within two circles of A -- friends of A, plus 
      their immediate friends only
    """
    assert person in my_dir
    label = person
    listtemp=[]

    # ------------ BEGIN YOUR CODE ------------

    listtemp = list(my_dir.get(label))

    for i in range (len(listtemp)):
        listtemp.extend(list(my_dir.get(listtemp[i])))
        listtemp1=(list(set(listtemp)))
        listtemp1.sort()
        print(listtemp1)

    for m in range(len(listtemp1)):
        if label == listtemp1[m]:
            listtemp1.pop(m)
            break

    for e in range(len(listtemp1)):
        label += "_" + listtemp1[e]

    # ------------ END YOUR CODE ------------

    return label


def find_smallest_team(my_dir):
    """Find team with smallest size, and return its roster label str
    - if ties, return the team roster label that is first in ascii order
    """
    smallest_teams = []

    # ------------ BEGIN YOUR CODE

    q = dict(my_dir)
    x = q.keys()

    smallest_teams1=[]
    dicttemp={}


    for o in x:


        listtemp = list(my_dir.get(o))

        p = len(listtemp)
        listtemp3=[]
        #print(o,p,listtemp)

        for i in range(p):
            listtemp3.extend(list(my_dir.get(listtemp[i])))
            #print(i,list(my_dir.get(listtemp[i])))
            listtemp2 = (list(set(listtemp3)))
            listtemp2.sort()
        temptup=(len(listtemp2), o ,listtemp2)

        smallest_teams1.append(temptup)


    smallest_teams2 = sorted(smallest_teams1, key=lambda dta: (dta[0], dta[1]))

    listtemp1=smallest_teams2[0][2]
    listtemp1=sorted(listtemp1)
    for i in range(len(listtemp1)):
        if smallest_teams2[0][1] == listtemp1[i]:
            listtemp1.pop(i)
            break
    label = smallest_teams2[0][1]
    for e in range(len(listtemp1)):
        label += "_" + listtemp1[e]

    print(label)
    smallest_teams = []
    smallest_teams.append(label)

    # ------------ END YOUR CODE


    return smallest_teams[0] if smallest_teams else ""



if __name__ == '__main__':
    # To run and examine your function calls

    print('\n1. run load_pairs')
    my_pairs = load_pairs('myfriends.txt')
    print(my_pairs)

    print('\n2. run make_directory')
    my_dir = make_friends_directory(my_pairs)
    print(my_dir) 

    print('\n3. run find_all_number_of_friends')
    print(find_all_number_of_friends(my_dir))

    print('\n4. run make_team_roster')
    my_person = 'DARTHVADER'   # test with this person as team leader
    team_roster = make_team_roster(my_person, my_dir)
    print(team_roster) 

    print('\n5. run find_smallest_team')
    print(find_smallest_team(my_dir))

    print('\n6. run Friends iterator')
    friends_iterator = Friends(my_dir)
    for num, pair in enumerate(friends_iterator):
        print(num, pair)
        if num == 10:
            break
    print(len(list(friends_iterator)) + num)
