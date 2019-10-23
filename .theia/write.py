f = open('newfile.txt', 'a')
lines = ['Hello','World']
text = '\n'.join(lines)
f.writelines(text)
f.close()

