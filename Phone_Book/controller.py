import recorder
#import serch_tel
import user_interface
import logger
import output_style

def run():
    temp = user_interface.choice()
    if temp == 1:
        print ('You have chosen to add a new contact')
        entry = recorder.record()
        logger.log_to_file(recorder.tecordtry)

    #if temp == 2:
    #    print ('You have chosen to serch contact')
    #    entry = serch_tel.sderch()
    #    logger.read_all_files(entry)
    
    if temp == 3:
        print (print ('You have chosen to print all contacts'))