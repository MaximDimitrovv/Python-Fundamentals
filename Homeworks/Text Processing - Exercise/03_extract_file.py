path_info_list = input().split("\\")

file = path_info_list[-1].split(".")

file_name = file[0]
file_extension = file[1]

print(f"File name: {file_name}\nFile extension: {file_extension}")