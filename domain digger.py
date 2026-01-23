import subprocess
target_domain = input("Enter the domain (e.g:example.com) you want to use dig on:").strip()
parameter = input("Enter parameter you want to use:").upper()
valid_param = ['A','TXT','MX','NS']
if parameter in valid_param :
    command = ['dig',target_domain,parameter]
    result = subprocess.run(command ,capture_output=True,text=True)
    save = input("DO you want to save output to a file(Y/N)?").strip().upper()
    if save == 'Y' :
        ask = input("Enter the file name:(e.g:output.txt):").strip()
        with open(ask,'w') as f :
            f.write(result.stdout)
            print("output is saved in -",ask)
    else :
        print(result.stdout)
else:
    print("invalid Parameter , Please enter valid parameter.")
