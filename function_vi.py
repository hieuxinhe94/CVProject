#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
#  @START 
####                            Pvh Developer
####                               create 18-8-2016                 working good with .doc  file
############################################################################################################################ 

import textract
import codecs
import prettytable

import glob, os

print '=========== Buoc 1 : Tim kiem toan bo tep tin can trich xuat  trong floder ======='
path = os.getcwd()
                      
                                        
_dir = ""
_dir = "" + path+"/vi/"

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

for file in glob.glob("*.pdf"):
    lists[3][k]=str(file)
    k +=1
    
print "pdf : %s"  %(str(lists[3]))
lists[3] = None
print 'Pdf just disable for test'
# k+1 is length of lists[3]
############################################################################################################################
print '================================ Buoc 2 : format du lieu ======='
############################################################################################################################

_i=0
import textract


def convert_to_text_to_process():
     
        for _i in range(0,len(lists[2]) ,1) :                   # .doc
                lists[2][_i] = (textract.process(_dir+lists[2][_i])).decode('utf-8')
               
                _i+=1
        print _i        
       
convert_to_text_to_process()

        


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

# print '=============Buoc 3 : Nhap tu khoa va Tag ======='
dict_keys_en_Tag_short_profile = [u"họ & tên",u"giới tính",u"ngày sinh",u"nơi sinh",u"chiều cao",u"cân nặng",u"tình trạng hôn nhân",u"tôn giáo",u"quốc tịch",u"số cmnd",u"địa chỉ thường trú",u"đt",u"email",u"địa chỉ"]

dict_keys_en_Tag_short_Objective= [u"Nguyện vọng"]                     # Neu ko can thiet lam thi co the lay ca doan do
dict_keys_en_Tag_short_Education = [u"đh",u"học ",u"trường ",u"đường",u"lớp"]
dict_keys_en_Tag_short_Experience = [u"Kinh Nghiệm Làm Việc ",]
dict_keys_en_Tag_short_Skill = [u"Kỹ Năng "]             #tiếng anh","máy tính","nhóm","communication
dict_keys_en_Tag_short_Interest= [u"Thích"]
                                                     # Sau nay se cho vao List_tag[{},{}...]
dict_keys_en_Tag_long = [u"THÔNG TIN CÁ NHÂN", u"HỌC VẤN",u"QUÁ TRÌNH LÀM VIỆC",u"KỸ NĂNG", u"MONG MUỐN" ,u"End"]

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
# tim nhung tu khoa chinh truoc , phan vung chung ra thanh nhung doan nho ,sap xep thanh khung xuong, 
#sau do tu nhung doan nho moi tim cac tag 1 dong (short tag) , va luu thanh kieu json theo key - values         
############################################################################################################################

dict_keys_en_long_tag = [[None]*(len(dict_keys_en_Tag_long)) for i in range((len(_text_lists_convert2)))]
def find_partion():
        for i in range(0,len(_text_lists_convert2),1) :     
                   # chay lan luot cac tep da chuyen kieu doc sang 
                   _i = 0 
                   for line in _text_lists_convert2[i].splitlines():
                               _i +=1
                               for key in range(0,len(dict_keys_en_Tag_long),1):
                                            if dict_keys_en_Tag_long[key -1] in line :
                                                       #   print line 
                                                          dict_keys_en_long_tag[i][key-1] = (_i)
                                                          
                                          
                   print " Total line CV : %s" %(str(_i))
                   dict_keys_en_long_tag[i][5] = _i 
       # print ' ==> \n'
       # print " Partion of CV " 

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
                   
       #  print ' ==> \n '

#test_pdf()




#dict_keys_en_long_tag.sort()                    # Phan chia thanh tung doan nho , sap xep theo thu tu 
from prettytable import PrettyTable 

t =  PrettyTable(dict_keys_en_Tag_long)

for i in range(0,len(_text_lists_convert2),1):
        t.add_row(dict_keys_en_long_tag[i])
print t
      
     
############################################################################################################################
# Buoc 4-*
# Tim cac tu khoa nho hon , thuoc tung phan, quet tung vung nho :
#      ***
############################################################################################################################
# print '\n \t \t Quet lan luot cac mini tag trong long tag va luu vao result 1'

result_1 = [[("").encode("utf-8")]*(len(TAG[0] )) for i in range(len(_text_lists_convert2))]
result_2 = [[None]*(len(TAG[1] )) for i in range(len(_text_lists_convert2))]
result_3 = [[None]*(len(TAG[2] )) for i in range(len(_text_lists_convert2))]
result_4 = [[None]*(len(TAG[3] )) for i in range(len(_text_lists_convert2))]
result_5 = [[None]*(len(TAG[4] )) for i in range(len(_text_lists_convert2))]
result_6 = [[None]*(len(TAG[5] )) for i in range(len(_text_lists_convert2))]

# Tao ra 7 cai result hay tao 1 cai chua ca 7 ?  
# De quet tat ca cac vung lan luot , them vong for lon nhat vafo va bien k, dic..[i][k] ? NO! =(



def find_date (result_x,x):
       for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
	        for line in  _text_lists_convert2[i].splitlines()[dict_keys_en_long_tag[i][x-1]:dict_keys_en_long_tag[i][x]]:
                                 for key in range(0,len(TAG[x-1] ),1):
                                                if "/" in line:
                                                        print line
                                                        result_x[i][key] = line.strip().replace(TAG[x-1][key],"").encode("utf-8")              
       print " finish find : \n"
#find_date(result_2,2)	 


def find_tag(result_x,x):
	for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
	        for line in  _text_lists_convert2[i].splitlines()[dict_keys_en_long_tag[i][x-1]:dict_keys_en_long_tag[i][x]]:
                                 for key in range(0,len(TAG[x-1] ),1):
                                                if TAG[x-1][key] in line:
                                                       # print line
                                                        result_x[i][key] = line.strip().replace(TAG[x-1][key],"").encode("utf-8")              
	# print " findding : \n"
	
	#return result_x
# profile  tim theo kieu tim tag thi hop ly , con education , exeprience thi nen tim theo kieu tim ngay thang (/) con skill thi ngat theo dong ,doan 
                       
def tim_tag_thongtincanhan():
	for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
	        for line in  _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][0]:dict_keys_en_long_tag[i][1]-1]:
                                 for key in range(0,len(TAG[0] ),1):
                                                if TAG[0][key] in line:
                                                       # print line
                                                        result_1[i][key] = line.strip().replace(TAG[0][key]or":","").encode("utf-8").replace(":", "").strip()
                                                                
	#print " find profile : \n"

def tim_tag_kynang():
        for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
                result_5[i][0]= ""    
                for line in  _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][4]:dict_keys_en_long_tag[i][5]-1]:
                                   	             
	                        result_5[i][0] += line.strip().encode("utf-8").replace(":", "").strip() + "\n"
	#print 'find skills '

def tim_tag_kinhnghiem():
     for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep4
            result_4[i][0] = ""
            for line in _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][3]:dict_keys_en_long_tag[i][4]-1]:
                       if '19' or '20' in line :
                                result_4[i][0] += line.strip().encode("utf-8").replace(":", "").strip()+ "\n"
                        
    # print 'find exprience'
def tim_tag_sothich():
              for i in range(0,len(_text_lists_convert2),1):          # quet tung tep , i la stt tep
                   result_6[i][0] = ""
                   for line in _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][5]:dict_keys_en_long_tag[i][6]]:
                               
                                result_6[i][0] += line.strip().encode("utf-8").replace(":", "").strip()
     #         print 'find interest'
def tim_tag_nguyenvong():
        for i in range(0,len(_text_lists_convert2),1):
                result_3[i][0] = ""
                for line in _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][1]:dict_keys_en_long_tag[i][2]]:
                         result_3[i][0] += line.strip().encode("utf-8").replace(":", "").strip() +"\n"       
def tim_tag_giaoduc():
        for i in range(0,len(_text_lists_convert2),1):    
                        for line in  _text_lists_convert2[i].lower().splitlines()[dict_keys_en_long_tag[i][2]:dict_keys_en_long_tag[i][3]]:
                                  for key in range(0,len(TAG[2] ),1):
                                                if TAG[2][key] in line :
                                                       # print line
                                                        
                                                        result_2[i][key] = line.strip().encode("utf-8").replace(":", "").strip()
      #  print "find Education"                
                        
                    
tim_tag_thongtincanhan()
tim_tag_kynang()
#tim_tag_sothich()
tim_tag_nguyenvong()
tim_tag_kinhnghiem()
tim_tag_giaoduc()

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

def write_file_txt(result_x,x,_file):
        data_output = (show_data(result_x,x)).get_string()
        with codecs.open(_file,'w','utf-8') as f:
                f.write(data_output)
                f.close()       
write_file_txt(result_1,1,'txt_thongtincanhan.txt')

write_file_txt(result_2,2,'txt_giaoduc.txt')

write_file_txt(result_3,3,'txt_kinhngiem.txt')

write_file_txt(result_4,4,'txt_kynang.txt')
write_file_txt(result_5,5,'txt_nguyenvong.txt')
write_file_txt(result_6,6,'txt_sothich_txt')

# text file thì oke rồi còn csv file thì chưa ngon 1 chút nào cả 
 



 
import csv
def write_excel(result_x,x,out_file):
        arr = result_x  #???
        f = codecs.open(out_file,'w','utf-8')
        writer= csv.writer(f)
        print () #???
        writer.writerow(unicode(TAG[x-1]))
        for values in arr :
                writer.writerow(unicode(values))
               
        f.close()
        
       
'''
write_excel(result_1,1,'out_persional.csv')
write_excel(result_2,2,'out_employee.csv')                 # no tu dong tao ra tep moi neu chua co
write_excel(result_3,3,'out_education.csv')
write_excel(result_4,4,'out_skill.csv')
write_excel(result_5,5,'out_exprience.csv')
write_excel(result_5,5,'out_interest.csv')
'''


print '\n===========Success ==================\n'
############################################################################################################################
#                       Buoc 5
# Dieu quan trong la ban phai che bien dc du lieu , chuyen du lieu str kia ve dictionaryVariable de xu li va chuyen thanh #kieu json la can thiet 
############################################################################################################################
#

############################################################################################################################
# return Json type:             Buoc 6
############################################################################################################################


def write_excel_all(out_file):
        arr = result_1+result_2+result_3+result_4+result_5+ result_6            # wrong!
        k = (TAG)
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

