# ShutilCopy-example

This is a simple program that copy files from one folder into other using Shutil.copy and Tqdm.
It also verifies if there are files in the destiny folder and prompts the user to proceed or not with the copy.

It's a bit clumsy but uses some beginner concepts important to those starting with Python.

Also, it's important to note that whenever you are using shutil.copy you just need to provide a source and destination path for it to work. If 
working with multiple files just remember to load them in a list with their full path before iterating over them. This would be an example:
      
          list=os.listdir('My\files\folder')
          for i in range (len(list))
            list[i]='path\untill\my\files+list[i]
            
And just then make the copy iteration :           
         for i in list
         shutil.copy(i,'My\other\folder')
