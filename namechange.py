import os

# fabric 폴더 경로
folder_path = 'pouch/textile'

# 파일 이름 변경을 위한 매핑
quality_mapping = {
    '최고급': 'finest',
    '고급': 'fine',
    '일반': 'common',
    '저가형': 'cheap'
}

special_mapping = {
    '라이트': 'light',
    '베이스': 'base',
    '안감': 'in',
    '겉감': 'out',
    '무늬':'pattern'
}

textile_mapping = {
    '양털':'wool',
    '거미줄':'cobweb',
    '가는실':'thinThread',
    '굵은실':'thickThread'
}


#파우치 내의 폴더명
pouch_path = os.path.basename(folder_path)

for filename in os.listdir(folder_path):
    print(os.path.join(folder_path,filename))
    # 파일 이름과 확장자 분리
    name, ext = os.path.splitext(filename)
    name_part = name.split('-')
    new_name = ''.join([textile_mapping[name_part[0]],'_',special_mapping[name_part[1]]])+ext
    new_file_path = os.path.join(folder_path, new_name)
    print(new_file_path)
    os.rename(os.path.join(folder_path,filename),new_file_path)
    



# for filename in os.listdir(folder_path):
#     # 파일 이름과 확장자 분리
#     name, ext = os.path.splitext(filename)
#     if not name.split('-')[-1][-1].isdigit():
#         mapping_part = name.split('-')[-1]
#         print(mapping_part)
#         new_name = name.replace(name, pouch_path+'_'+special_mapping[mapping_part])+ext
#         new_file_path = os.path.join(folder_path,new_name)
#         os.rename(os.path.join(folder_path,filename), new_file_path)
#     # 품질을 찾기 위한 분리
#     for quality_kor in quality_mapping.keys():
        
#         if quality_kor in name and name.split('-')[-1][-1].isdigit():
#             quality_eng = quality_mapping[quality_kor]
#             # 로마자 부분 추출
#             roman_part = name.split('-')[-1][-1]  # 마지막 부분 가져오기
#             new_name = f"{quality_eng}_roman{roman_part}{ext}"

#             # 새로운 이름이 이미 존재하는지 확인
#             new_file_path = os.path.join(folder_path, new_name)
#             if not os.path.exists(new_file_path):
#                 # 파일 이름 변경
#                 os.rename(os.path.join(folder_path, filename), new_file_path)
#                 print(f"Renamed: {filename} to {new_name}")
#             else:
#                 print(f"File already exists: {new_name}")
#             break



