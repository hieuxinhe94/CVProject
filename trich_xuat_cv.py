# -*- coding: utf-8 -*-

#@START PROCCESS
####                            Pvh Developer
####                               create 8-8-2016                 working good with .doc  file
############################################################################################################################ 
print '================ TRÍCH XUẤT VĂN BẢN : (CV XIN VIỆC) ================================= '
print " \t\t\t TÁC GIẢ : PHAM VAN HIẾU \n"
print "email : hieuxinhe94@gmail.com \n"
print 'github.com/hieuxinhe94/openCV'
print '*** chương trình có sử dụng các moduln mả nguồn mở của python:\n  1.textract  : xử lí ,chuyển văn bản từ nhiều định dạng sang kiểu text \n 2.langid : nhận diện 97 loại ngôn ngử tự nhiên trên thế giới \n 3.prettytable : hiển thị chế độ bảng dử liệu trực tiếp trên thiết bị đầu cuối \n 4.các gói shultil,os,glob,... \n'


#============================================================================================================
print 'Các bước cốt lỏi  chính của chương trình như sau : '

print 'di chuyển tất cả các file của các ngôn ngử khác nhau về từng floder riêng .'

import nhan_biet_ngonngu
print 'done! '
print "\n  chay từng tệp tin nhận dạng riêng cho mổi loại ngôn ngử gồm : \n  - chuyển kiểu docx,doc,pdf,images thành kiểu text (txt) \n - chia nhỏ từng vùng sau khi nhận biết được tiêu đề cũa từng phần  \n - nhận dạng vùng đó và tìm các từ khóa phù hợp \n - Lấy các dòng có từ khóa hoặc chế biến theo từng thuật toán ,yêu cầu  riêng \n -Tạo bảng trực quan trên màn hình terminal,cmd ,... \n -Ghi dử liệu đó thành từng bảng,cột tương ứng \n -Xuất ra file excel,csv ,txt ... tùy chọn \n \t\t\t Kết thúc  "

print '\n \t Xử lí cv tiếng anh ....'
import function_en

print "\n\n \t Xử lí cv tiếng việt ...."
import function_vi




print "\n\n\n\n \t OPTIONS "
print 'open terminal \n'
print 'Enter : >>  python trich_xuat_cv.py'
print '******* run a file if you want to see more : python function_en.py ,python function_vi.py '
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Done~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
############################################################################################################################
#@END OF PROCESS              
################                Building Successful                             
##                                      pvh  

