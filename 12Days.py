#d={"Twelfth":"Twelve Drummers Drumming,","Eleventh":"Eleven Pipers Piping,","Tenth":"Ten Lords-a-Leaping,","Ninth":"Nine Ladies Dancing,"
#    ,"Eighth":"Eight Maids-a-Milking,","Seventh":"Seven Swans-a-Swimming,","Sixth":"Six Geese-a-Laying,","Fifth":"Five Gold Rings,"
#    ,"Fourth":"Four Calling Birds,","Third":"Three French Hens,","Second":"Two Turtle Doves, and","First":"A Partridge in a Pear Tree."}

#for key, value in d.items():
#    print("\nOn the {} day of Christmas\nMy true love sent to me\n{}".format(key, value))

#L=(["\nTwelve Drummers Drumming,","\nEleven Pipers Piping,","\nTen Lords-a-Leaping,","\nNine Ladies Dancing,","\nEight Maids-a-Milking,","\nSeven Swans-a-Swimming,","\nSix Geese-a-Laying,","\nFive Gold Rings,","\nFour Calling Birds,","\nThree French Hens,","\nTwo Turtle Doves, and","\nA Partridge in a Pear Tree."])
#print(x+L[11]+x+L[10]+L[11]+x+L[9]+L[10]+L[11]+x+L[8]+L[9]+L[10]+L[11])
# 

#d={1:"First",2:"Second",3:"Third",4:"Fourth",5:"Fifth",6:"Sixth",7:"Seventh",8:"Eighth",9:"Ninth",10:"Tenth",11:"Eleventh",12:"Twelfth"}
#l=["A Partridge in a Pear Tree.","Two Turtle Doves, and","Three French Hens,","Four Calling Birds,","Five Gold Rings,","Six Geese-a-Laying,","Seven Swans-a-Swimming,","Eight Maids-a-Milking,","Nine Ladies Dancing,","Ten Lords-a-Leaping,","Eleven Pipers Piping,","Twelve Drummers Drumming,"]
#print("On the First day of Christmas\nMy true love sent to me\n{}".format(l[0]))
#for i in range(1,12):
# x=d.get(i+1)
# y=l[i]
# print("\nOn the {} day of Christmas\nMy true love sent to me\n{}".format(x,y))
# if i>0:
#  z=reversed(range(0,i))
#  for i in z:
#   print(l[i])

days = {
    1: "First",
    2: "Second",
    3: "Third",
    4: "Fourth",
    5: "Fifth",
    6: "Sixth",
    7: "Seventh",
    8: "Eighth",
    9: "Ninth",
    10: "Tenth",
    11: "Eleventh",
    12: "Twelfth"
}
words = [
    "A Partridge in a Pear Tree.",
    "Two Turtle Doves, and",
    "Three French Hens,",
    "Four Calling Birds,",
    "Five Gold Rings,",
    "Six Geese-a-Laying,",
    "Seven Swans-a-Swimming,",
    "Eight Maids-a-Milking,",
    "Nine Ladies Dancing,",
    "Ten Lords-a-Leaping,",
    "Eleven Pipers Piping,",
    "Twelve Drummers Drumming,"
]
for i in range(12):    
    x= days.get(i+1)
    y= words[i]
    print("\nOn the {} day of Christmas\nMy true love sent to me\n{}".format(x,y))
    # printing the correct day and gift in the correct order ^^^^
    if i>0:
        # while i is being iterated over range 1-12 which is over 0
        z=reversed(range(0,i))
        # this range inverts the order from the current range value to the value of i
        for i in z:
            # this iterates oer each of the items in that above range
            print(words[i])