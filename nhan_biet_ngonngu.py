# -*- coding: utf-8 -*-

#############################################################################
# Nhan biết ngon ngu rồi di chuyen ngu vao tung thu muc rieng  
#
#############################################################################

from langid import langid
# tim kiem tat ca tep tin co trong dir 
import shutil
import os 
import glob

# ho tro nhap thu muc o day 
print "nhap thu muc chua du lieu "
       # = "/home/pvh/Documents/GITHUB/data/"

def input_target():
           print   '** /computer/project/github/data/ \n'
           _dir =    raw_input(" Nhập đường dẩn đến thư mục chứa dử liệu \n ")
           with open('setup.txt','a') as s:
                        s.write(""+_dir)
                        s.close()                
           return _dir 
          
_dir = input_target() 
_dir_en = _dir+"en/"
_dir_vi = _dir+ "vi/"


class user:
        root = _dir
        floder= ""
        

os.chdir(_dir)
lists = [{},{},{},{},{}]
i,j,k,t=0,0,0,0
for file in glob.glob("*.txt"):
    lists[1][i] = str(file)
    i +=1
print "txt: %s"  %str((lists[1]))
# i+1 is length of lists[1] or use len(lists[1])

for file in glob.glob("*.doc"):
    lists[2][j]=str(file)
    j+=1
print  "doc : %s " %(str(lists[2]))    
# j+1 is length of lists[2]
# 
print ' * Pdf just disable for test'
for file in glob.glob("*.pdf"):
    lists[3][k]=str(file)
    k +=1
    
print "pdf : %s"  %(str(lists[3]))
print '================================ Buoc 2 : format du lieu ======='
############################################################################################################################
#       
############################################################################################################################
_i=0
import textract

_text_lists_convert2 = [None] *(len(lists[2])+ len(lists[3])+1)
_text_lists_convert3 = [None] *(len(lists[3]))
def convert_to_text_and_and_move_field():
       
        for _i in range(0,len(lists[2]) ,1) :                   # .doc
                _text_lists_convert2[_i] = (textract.process(_dir+lists[2][_i])).decode('utf-8').lower()
                lan,x =  langid.classify(_text_lists_convert2[_i])
               
                
                if lan == "vi":   
                        shutil.remove(_dir+lists[2][_i]  + "",_dir_vi + lists[2][_i] +"")             
                if lan == "en":
                        shutil.remove(_dir+lists[2][_i]  + "",_dir_en + lists[2][_i] +"")                      
                else :
                        print 'done or the language not of english , vietnames with doc^^'
                
                
                _i+=1
      #  print '\tHave %s doc file ' %(str(_i))        
'''   _j=_i
        for _j in range(_i,len(lists[3])+_i,1) :                    # .pdf
                _text_lists_convert2[_j] = (textract.process(_dir+lists[3][_j-_i])).decode('utf-8').lower()
                lan,x =  langid.classify(_text_lists_convert2[_j-_i])
               
                
                if lan == "vi":   
                        shutil.copy(_dir+lists[3][_j-_i]  + "",_dir_vi + lists[3][_j-_i] +"")             
                if lan == "en":
                        shutil.copy(_dir+lists[3][_j-_i]  + "",_dir_en + lists[3][_j-_i] +"")                      
                else :
                        print 'done or the language not of english , vietnames  with pdf^^'
                # neu ma tieng anh thi remove no den floder tieng anh , neu tieng bviet thi move no den tieng viet
                
                _j+=1
      '''          
      #  print "\tHave %s pdf file" %(str(_j-_i))
convert_to_text_and_and_move_field()
     
print '\tHave %s doc file ' %(str(_i))   
print '============= Done of identify the language of cv in floder ======= \n'




