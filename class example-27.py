f = open('output.txt', 'w') # opening same file 
# write
f.write("\n writing new line contedn")
# close
f.close()


"""
When we are openin a file in write mode, if the file is not exist

then it will crate a new file

Incase if the file is exist it will over write the content

If you wnated add new content thne we need open in append mode

"""

f = open('output.txt', 'a') # opening same file 
# write
f.write("\n --------------------------")
# close
f.close()
