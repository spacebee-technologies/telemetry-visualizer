import struct


class MessageManager:

    __header_format='<QHBQHHHBH'

        
    def make_CRC(self, header, body):
        "Make CRC with 16 bits CTC-16-CCITT with polynomial x^16+x^12+x^5+1."
        data=header+body
        crc = 0xFFFF
        for byte in data:
            crc ^= (byte << 8)
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc <<= 1

        return crc & 0xFFFF


    def check_CRC(self,header,body,crc_check):
        crc=self.make_CRC(header,body).to_bytes(2, 'little')
        if crc == crc_check:
            return True
        else:
            return False
        
    def unpack(self,response):
        header_size = struct.calcsize(self.__header_format)
        header_data = response[:header_size]
        timestamp, interaction_type, interaction_stage, transaction_id, service, operation, area_version, is_error_message, body_length = struct.unpack(self.__header_format, header_data)
        body_response = response[header_size:-2]  
        crc_response = response[-2:] 
        if interaction_stage==1:   #Checkea que el interaction type es una respuesta del mensaje
            if not is_error_message:
                
                if self.check_CRC(header_data,body_response,crc_response):

                    if interaction_type==2:
                        print("Error is telecommand")

                    elif interaction_type==3:
                        print("Error is telecommand")
                    
                    elif interaction_type==6:
                        return {'operation_id': operation, 'transaction_id':transaction_id,
                                'timestamp':timestamp, 'area_version': area_version,
                                'body': body_response
                                }
                
                else:
                    print("CRC check failed. Error in the communication detected.")
            else:
                print("The message is an error")
        else:
            print("Error, interaction stage not valid")

    