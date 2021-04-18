Letter = '''
Dear <|NAME|>,


What a fabulous job you did with the store renovations! The merchandise displays 
are wonderful,and the decor beautifully complements the atmosphere you are trying 
to create.

Without your thoughtful planning and oversight, an undertaking like this would
have been nearly impossible.

Heartfelt congratulations and best wishes for your continued success.

Regards,

<|NAME2|> 
<|DATE|>
'''
name = input("Enter the name of Reciver\n")
name2 = input("Enter the name sender\n")
date = input("Enter the date\n")
Letter = Letter.replace("<|NAME|>", name)
Letter = Letter.replace("<|NAME2|>", name2)
Letter = Letter.replace("<|DATE|>", date)
print(Letter)
