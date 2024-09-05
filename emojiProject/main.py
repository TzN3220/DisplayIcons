
import emojis
try:
 option=int(input("Insert 1 for print_all_icons or 2 search_icons_by_keyword"))
except(ValueError):
 print("Error")
else:
 if (option==1):
   emojis.print_all_icons()
 if (option==2):
        kewWord = input("Please insert Keyword for search emoji:")
        emojis.search_icons_by_keyword(kewWord)
        emoji_name=input("Please choose name of emoji from the list")
        emojis.display_icon(emoji_name)






