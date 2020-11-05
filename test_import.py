import read_from_file_and_net as rfn

my_url = "https://markfoley.info/pa1/gettysburg.txt"

gettysburg_text = rfn.get_file_from_net(my_url)

print(my_url)