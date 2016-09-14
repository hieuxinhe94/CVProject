#CVProject
                        Tác Giả : PHẠM VĂN HIẾU 
                        email : hieuxinhe94@gmail.com
                        github/hieuxinhe94/CVProject
               Ý Tưởng : Xử lí khối lượng lớn tệp tin và với thời gian nhanh nhất có thể            
               ** Chương trình đả được kiểm thử với xử lý 100 tệp CV chỉ trong 6s**
            (Yêu cầu : 
            cài đặt gói python  numpy  :  sudo apt-get install python-numpy
            và  python 2.7  )
<       CHƯƠNG TRÌNH KHÔNG THỂ CHẠY TRÊN WINDOWS VÌ CÁC MOLDUN : textract,numppy KHÔNG THỂ CHẠY TỐT Ở NỀN TẢNG NÀY  >               
<                         CÓ THỂ CHẠY TRÊN TẤT CẢ CÁC NỀN TẢNG UNIX , MAC , DESBIAN                             >                 

Biên Dịch và chạy chương trình :                                                                      
      1.  git clone https://github.com/hieuxinhe94/CVProject.git                                                   
      2. Open  Terminarl ,...  and go to CVProject Floder                                                           
      3. Enter : python trich_xuat_cv.py                                                                                
      4. Enter path to data floder :                                                                                  
        ex: (/home/user/Documents/CVProject/data/) Đường dẩn đến thư mục chứa các file cv                                 
      5. finish : Mở thư mục chứa data vừa rồi và xem kết quả ở các file cvs,txt được tạo ra                            
        hoặc cũng có thể quan sát trực tiếp trên thiết bị đầu cuối                                  
      
      
      

![alt tag](https://github.com/hieuxinhe94/CVProject/blob/master/fghjk.gif)


                ** Chương trình có sử dụng các moduln mả nguồn mở như :
        1. Textract : Xử lí văn bản từ nhiều định dạng sang kiểu text 
        2. Langid   : Nhận biết 97 loại ngôn ngử tự nhiên 
        3.  Numpy   : git clone http://github.com/numpy/numpy.git numpy 
        4. pretty table : Hiển thị giao diện trực tiếp các bảng dử liệu trên thiết bị đầu cuối 
        5. các gói : Shultil , goslate , ... 
        
                
                
  ![alt tag](https://github.com/hieuxinhe94/CVProject/blob/master/result_en.png)
  ![alt tag](https://github.com/hieuxinhe94/CVProject/blob/master/result_vi.png)


                  **  Quy trình thực thi chính của phần mềm  như sau :

    I. Nhận biết ngôn ngử :
        0.Nhập vào địa chỉ thư mục chứa dử liệu , chương trình sẻ lưu lại ở setup.txt
        1.Đọc từng tệp tin đầu vào và nhận ra đó thuộc ngôn ngử nào 
        2.Di chuyển các tệp tin đó vào từng thư mục chứa cùng một loại ngôn ngủ (mới hổ trợ eng,vi)
        <#nhan_biet_ngonngu.py>
    II. Xử lí văn bản :
        1. Tìm kiếm các định dạng doc,pdf,.. trong từng thư mục của các ngôn ngử lưu  trong setup.txt
        2. Đọc và chuyển kiểu đó sang text 
        3 .Cập nhật lại danh sách và tiến hành trích xuất   
    III. Thống kê ,tìm từ khóa :
        1. Nhận diện các từ khóa tiêu đề (Profile , Education,Hồ Sơ ,Kinh NGhiệm ... )
        2. Phân chia thành từng đoạn ,ngăn cách bởi các từ khóa lớn đó 
        3. Từ những đoạn vưa tìm được  bắt đầu nhận diện từ khóa chi tiết chỉ trong đoạn đó 
           theo từng thuật toán riêng ,đảm báo đúng yêu cầu dử  liệu 
        4.Hiển thị bảng dử  liệu lên màn hình 
    IV. Xuất FIle :
        Tụ động tạo mới hoặc ghi đè ,hoặc ghi thêm dử liệu ra cá file với định dạng gồm Csv(exel),text table ,
        
    V. Kết thúc 




******************************** CHƯƠNG TRÌNH KHÔNG HOẠT ĐỘNG TỐT  TRÊN WINDOWS  *******************
*************************               VÀ KHÔNG THỂ KHẮC PHỤC NÓ                 ******************************



                  B. Hướng phát triển thêm :
        1. fix lổi khi các Tag lớn  xáo trộn , không theo thứ tự phổ biến 
        2. Trả về các định dạng Json kết nối webservice và database 
        3. viết nhiều hàm nhằm thực thi chính xác hơn với kiểu Pdf 
        4. Làm việc tốt với các định dạng unicode,symbol toán học ...
        
        
        
                        
                

                        
                
