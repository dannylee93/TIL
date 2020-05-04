#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Zipfile 모듈로 압축파일 만들기

# 1. 필요한 모듈 임포트(폴더 내 여러 파일 압축해야해서 조금 복잡해진다.)
import os
import zipfile

# 2. 반복할만큼 미리 객체 만들기(이건 필수적 아님)
list = [1,2,3,4,'h','k','s']

# 3. list 만큼 작업 반복
for idx in list:
    # 4. 내가 만들 압축파일의 이름과 경로에 대한 객체 생성
    zip_df = zipfile.ZipFile("./roi_{}.zip".format(idx), 'w')
    
    # 5. os.walk() 메소드를 통해 원래 폴더의 모든 파일과 하위폴더 순회
    for folder, subfolders, files in os.walk('./roi_{}'.format(idx)):
        for file in files:
            # 6. 조건문의 파일형식을 계속 바꾸며 파일 형식마다 바꿀 수도 있다.
            if file.endswith('.jpg'):
                #7. write의 3가지 매개변수 : 압축하고자 하는 파일 이름, 압축된 파일에 대해 다른 파일명을 해줄수 있게
                zip_df.write(os.path.join(folder, file), 
                             os.path.relpath(os.path.join(folder,file),'./roi_{}'.format(idx)),
                             compress_type = zipfile.ZIP_DEFLATED
                            )

zip_df.close()

