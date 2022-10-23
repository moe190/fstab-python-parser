import yaml,re


patt = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")   #regex to check if ip for NFS


with open('fstab.yaml') as yml_file:         #open file in read mode
     yo = yaml.safe_load(yml_file)               # load yaml from file in safe mode
     
    
for docs in yo:                                  #loop throw docs in yaml if multiple
    item = yo[docs]                              #load yaml doc
    print(str(item) + "text \n\n")
    for key,value in item.items():               # loop throw doc items and their values
        print(key,value)
        with open("fstab-result", "a") as file:  #open /etc/fstab in apending mode
            if 'options'  in value and re.match(patt,key):    #check if NFS and options
                print('nfs and options')
                file.write("{}:{:14} {:14}  {:14} {:14} 0 0\n".format(key,value['export'],value['mount'],value['type'] , ",".join(value['options'])))
            elif 'options' in value and not re.match(patt,key): #check if not NFS and options
                print('options and no NFS')
                file.write("{:14} {:14} {:14} {:14} 0 0\n".format(key,value['mount'],value['type']),",".join(value['options']))
            else:                                               #defaults no options and no NFS
                print('defaults')
                file.write("{:14} {:14} {:14} defaults 0 0\n".format(key,value['mount'],value['type']))
          