# fstab-python-parser
convert yaml fstab to /etc/fstab 

Prerequisities

1). Install python3 libraries on base OS.

2). Install yaml package using pip repository.

3). fstab input file as YAML format(Example: fstab.yaml)



Execution

1). copy fstab.yaml and fstab_parser.py script on any directory.

2). Run fstab_parser.py script with python3.

3). Out put will be on /etc/fstab


Note:
Script will ignore any other items but mount,type,device,NFS server IP,options,export
for example root-reserve: 10% 
