# -*- coding: utf-8 -*-

#@START PROCCESS
####                            Pvh Developer
####                    create 8-8-2016                 working good with .doc  file
############################################################################################################################ 

import textract
import re
import prettytable



print '=========== Buoc 1 : Tim kiem toan bo tep tin can trich xuat  trong floder ======='
_dir = "/home/pvh/Documents/Python/textract/en/"
import glob, os
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

print ' *** pdf is disabled to test'
'''
for file in glob.glob("*.pdf"):
    lists[3][k]=str(file)
    k +=1
'''    
print "pdf : %s"  %(str(lists[3]))

# k+1 is length of lists[3]
############################################################################################################################
print '================================ Buoc 2 : format du lieu ======='
############################################################################################################################

_i=0
import textract


def convert_to_text_to_process():
       
        for _i in range(0,len(lists[2]) ,1) :                   # .doc
                lists[2][_i] = (textract.process(_dir+lists[2][_i])).decode('utf-8') #.lower()
               
                _i+=1
        print _i 
        '''       
        _j=i
        for _j in range(_i,len(lists[3])+_i,1) :                    # .pdf
                lists[2][_j] = (textract.process(_dir+lists[3][_j-_i])).decode('utf-8').lower()
               
                _j+=1
        print _j
        '''
convert_to_text_to_process()

        
print 'Process successful'
print   len(lists[2])       

print '=============End of format  Convert to text(str)======='
_text_lists_convert2 = lists[2]
_text_lists_convert1 = lists[1]



############################################################################################################################
#   Key Tag
#               ***          Can chuyen long Tag thanh mang len(long_tag) hang , va max len(short tag cot)
# Tung TAG nen co cach trich xua khac nhau 
# Profile thi tim tu khoa roi lay dong do
# Skill thi lay toan bo doan do 
# Education thi lay theo tung cau thuoc doan do
# Experience thi lay tug cau , roi chia cau ra bang cach tim tu khoa thoi gian 
# 
############################################################################################################################

print '=============Buoc 3 : Nhap tu khoa va Tag ======='
dict_keys_en_Tag_short_profile = ["full name","date of birth","status","gender","nationality","street","adress","country","email","e-mail","phone","mobile","fax","relocation"]
dict_keys_en_Tag_short_Objective= ["Objective"]     #mong muon      # Neu ko can thiet lam thi co the lay ca doan do
dict_keys_en_Tag_short_Education = ["university","street","school","coleage"]
dict_keys_en_Tag_short_Experience = ["Experience",]
dict_keys_en_Tag_short_Skill = ["Skills"]
dict_keys_en_Tag_short_Interest= ["Interest"]
                                                     # Sau nay se cho vao List_tag[{},{}...]
dict_keys_en_Tag_long = ["Profile", "Objective" , "Education","Experience","Skills","Interest","Total"]

TAG = [[]*(len(dict_keys_en_Tag_short_profile)+1) for i in range(len(dict_keys_en_Tag_long))]       # Chon max len
# Part  :[ 1[Profile]*m, 2[Objective], 3[Education], 4[Experience],5[Skill],6[Interest],7[...vv]] 

TAG[0]  = dict_keys_en_Tag_short_profile                                # Luu TAG[0] = profile = array sort tag
TAG[1]  = dict_keys_en_Tag_short_Objective                              
TAG[2]  = dict_keys_en_Tag_short_Education                           
TAG[3]  = dict_keys_en_Tag_short_Experience                              
TAG[4]  = dict_keys_en_Tag_short_Skill                            
TAG[5]  = dict_keys_en_Tag_short_Interest                              

#dict_keys_vi = ["Ho Ten":0,"":0]
############################################################################################################################
# tim nhung tu khoa chinh truoc , phan vung chung ra thanh nhung doan nho ,sap xep thanh khung xuong, sau do tu nhung doan nho moi tim cac tag 1 dong (short tag) , va luu thanh kieu json theo key - values         
############################################################################################################################

dict_keys_en_long_tag = [[None]*(len(dict_keys_en_Tag_long)) for i in range((len(_text_lists_convert2)))]
def find_partion():
        for i in range(0,len(_text_lists_convert2),1) :     
                   # chay lan luot cac tep da chuyen kieu doc sang 
                   _i = 0 
                   for line in _text_lists_convert2[i].splitlines():
                               _i +=1
                               for key in range(0,len(dict_keys_en_Tag_long),1):
                                            if (dict_keys_en_Tag_long[key -1] in line):
                                                          dict_keys_en_long_tag[i][key-1] = (_i)
                                                          
                                          
                   print " Total line CV : %s" %(str(_i))
                   dict_keys_en_long_tag[i][6] = (_i)
        print ' ==> \n'
        print " Partion of CV " 

find_partion()
print 'Test Pdf -----------------------------'
def test_pdf():
         for i in range(0,len(_text_lists_convert3),1) :     
                   # chay lan luot cac tep da chuyen kieu doc sang 
                   _i = 0 
                   for line in _text_lists_convert3[i].splitlines():    # ??? spliline
                               _i +=1
                               for key in range(0,len(dict_keys_en_Tag_long),1):
                                            if dict_keys_en_Tag_long[key -1] in line :
                                                          dict_keys_en_long_tag[i][key-1] = (_i)
                                                          
                                          
                   print " Total line CV : %s" %(str(_i))
                   
         print ' ==> \n '

#test_pdf()




#dict_keys_en_long_tag.sort()                    # Phan chia thanh tung doan nho , sap xep theo thu tu 
from prettytable import PrettyTable 

t =  PrettyTable(dict_keys_en_Tag_long)

for i in range(0,len(_text_lists_convert2),1):
        t.add_row(dict_keys_en_long_tag[i])
print t
print '\n  \t ***Process success \n'       
     
############################################################################################################################
# Buoc 4-*
# Tim cac tu khoa nho hon , thuoc tung phan, quet tung vung nho :
#      ***
############################################################################################################################
print '\n \t \t Quet lan luot cac mini tag trong long tag va luu vao result 1'

result_1 = [[None]*(len(TAG[0] )) for i in range(len(_text_lists_convert2))]
result_2 = [[None]*(len(TAG[1] )) for i in range(len(_text_lists_convert2))]
result_3 = [[None]*(len(TAG[2] )) for i in range(len(_text_lists_convert2))]
result_4 = [[None]*(len(TAG[3] )) for i in range(len(_text_lists_convert2))]
result_5 = [[None]*(len(TAG[4] )) for i in range(len(_text_lists_convert2))]
result_6 = [[None]*(len(TAG[5] )) for i in range(len(_text_lists_convert2))]

# Tao ra 7 cai result hay tao 1 cai chua ca 7 ?  
# De quet tat ca cac vung lan luot , them vong for lon nhat vafo va bien k, dic..[i][k] ? NO! =(

print ' TEst \n'

def find_date (result_x,x):
       for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
	        for line in  _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][x-1]:dict_keys_en_long_tag[i][x]]:
                                 for key in range(0,len(TAG[x-1] ),1):
                                                if "/" in line:
                                                      #  print line
                                                        result_x[i][key] = line.strip().replace(TAG[x-1][key],"").encode("utf-8")              
       print " finish find : \n"
#find_date(result_2,2)	 
def find_tag_education():
        for i in range(0,len(_text_lists_convert2),1):    
                        for line in  _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][2]:dict_keys_en_long_tag[i][3]]:
                                  for key in range(0,len(TAG[2] ),1):
                                                if TAG[2][key] in line :
                                                       # print line
                                                        result_3[i][key] = ""
                                                        result_3[i][key] += (line.strip()).encode("ascii", "ignore")
        print "find Education"                
                        
                        
def find_tag_profile():
	for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
	        for line in  _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][0]:dict_keys_en_long_tag[i][1]-1]:
                                 for key in range(0,len(TAG[0] ),1):
                                                if TAG[0][key] in line:
                                                       # print line
                                                        result_1[i][key] = line.strip().replace(TAG[0][key]or":","").encode("utf-8").replace(":", "").strip()              
	print " find profile : \n"

def find_tag_skill():
        for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
                result_5[i][0]=""    
                for line in  _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][4]:dict_keys_en_long_tag[i][5]-1]:
                                   	             
	                        result_5[i][0] += (str(line)+"\n").encode("ascii", "ignore")
	print 'find skills '

def find_tag_exprience():
     for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep4
            result_4[i][0] =""
            for line in _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][3]:dict_keys_en_long_tag[i][4]-1]:
                       if '19' or '20' in line :
                                result_4[i][0] += (line.strip() + "\n").encode("ascii", "ignore")
                        
     print 'find exprience'
def find_tag_interest():
              for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
                   result_6[i][0] =""
                   for line in _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][5]:dict_keys_en_long_tag[i][6]]:
                               
                                result_6[i][0] += (line.strip() + "\n").encode("ascii", "ignore")
              print 'find interest'
def find_objective():
        for i in range(0,len(_text_lists_convert2),1):
                result_2[i][0] = ""
                for line in _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][1]:dict_keys_en_long_tag[i][2]]:
                         result_2[i][0] += (line.strip()+"\n").encode("ascii","ignore")          
find_tag_interest()                                
find_tag_exprience()
find_tag_education()
find_tag_profile()
find_tag_skill()
find_objective()




	                        
	#return result_x
# profile  tim theo kieu tim tag thi hop ly , con education , exeprience thi nen tim theo kieu tim ngay thang (/) con skill thi ngat theo dong ,doan 
	# TAG PROFILE




def show_data (result,k):
        k = PrettyTable(TAG[k-1])
        for i in range(0,len(_text_lists_convert2),1):
                k.add_row(result[i])
        print k
        return k

show_data(result_1,1) #       Tam thoi  comment lai vi no roi qua
show_data(result_2,2)        
show_data(result_3,3)                
show_data(result_4,4)
show_data(result_5,5)
show_data(result_6,6)

def write_file_txt(result_x,x):
        data_output = (show_data(result_x,x)).get_string()
        with open('text_profile.txt','a') as f:
                f.write(data_output)
                f.close()       
#write_file_txt(result_1,1)



import csv
def write_excel(result_x,x,out_file):
        arr=  data_output = (result_x)
        f = open(out_file,'w')
        writer= csv.writer(f)
        writer.writerow(TAG[x-1])
        for values in arr :
                writer.writerow(values)
               
        f.close()
        
       

write_excel(result_1,1,'out_persional.csv')
write_excel(result_2,2,'out_Objective.csv')   
write_excel(result_3,3,'out_employee.csv')                 # no tu dong tao ra tep moi neu chua co
write_excel(result_4,4,'out_education.csv')
write_excel(result_5,5,'out_skill.csv')
write_excel(result_6,6,'out_interest.csv')



print '\n===Write excels Success ==================\n'
############################################################################################################################
#                       Buoc 5
# Dieu quan trong la ban phai che bien dc du lieu , chuyen du lieu str kia ve dictionaryVariable de xu li va chuyen thanh #kieu json la can thiet 
############################################################################################################################
#

############################################################################################################################
# return Json type:             Buoc 6
############################################################################################################################

print '\t \n '
print '\t\t\t\t\t\t\t\t\t \b ALL  OUT PUT \t \n'
'''
arr = TAG[0]+TAG[1]+TAG[2]+TAG[3]+TAG[4]+TAG[5]
print arr
m = PrettyTable(arr)
for i in range(0,len(_text_lists_convert2),1):
               m.add_row(result_1[i]+result_2[i]+result_3[i]+result_4[i]+result_5[i] + result_6[i])
print m

teext = m.get_string()
with open ('text_tbl.txt', 'a') as _file:            # ko ghi de ,ghi de a= w
                _file.write(teext)
'''                




def write_excel_all(out_file):
        arr = result_1+result_2+result_3+result_4+result_5+ result_6            # wrong!
        k = TAG[0]+TAG[1]+TAG[2]+TAG[3]+TAG[4]+TAG[5]
        f = open(out_file,'w')
        writer= csv.writer(f)
        writer.writerow(k)
        for values in arr :
                writer.writerow(values)
               
        f.close()
write_excel_all('out_all_table.csv')

print "END OF PROGRAME"
############################################################################################################################
#@END OF PROCESS                Xa voi qua
################                Building Successful                             
##                                      pvh  

