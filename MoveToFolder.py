import os
import shutil
from tqdm import tqdm

def MoveToFolder(src_folder,dest_folder,word):
  safe_list=os.listdir(dest_folder)
  list3=os.listdir(src_folder)
  if len(safe_list)!=0:
         user_action=input("There are files in this folder,do you want to overwrite then? Yes/No ")
         if user_action=='Yes':
             for i in range (len(list3)):
              list3[i]=src_folder+list3[i]
             for i in tqdm(list3):
              if word in i:
                shutil.copy(i,dest_folder)
             print('\n Files were sucessfully copied to '+dest_folder)
             return None
         print("Then check the files in the folder and remove them OR choose an empty folder")
         return None
  if len(safe_list)==0:
         for i in range (len(list3)):
          list3[i]=src_folder+list3[i]
         for i in tqdm(list3):
            if word in i:
              shutil.copy(i,dest_folder)
         print('\n Files were sucessfully copied to '+dest_folder)
         return None
         
