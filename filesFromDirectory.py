''' add import filesFromDirectory to top of script using this module '''
''' usage example - filesFromDirectory.file_list("configs") '''


import os

''' Function to grab file list from directory '''
def file_list(additionalSubDirects):
    cwd = os.getcwd()
    cwd = cwd+"/"+str(additionalSubDirects)+"/"
    file_in_direct = os.listdir(cwd)

    file_list = []

    for file in file_in_direct:
	    file_list.append(cwd+file)

    return file_list

