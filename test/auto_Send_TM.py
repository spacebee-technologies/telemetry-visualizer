import socket
import struct
import time
import csv

ip="192.168.0.185"
port= 51526

socket_file_descriptor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def make_message(operation,body_bits,body_length,transaction_id):
    timestamp=0
    header_format='<QHBQHHHBH'
    interaction_stage = 1       # 8 bits	1 or 2 according to message order
    service= 0                  # 0 for telemetries (TM) or 1 for telecommands (TC)            # 16 bits	Unique identifier for a given telemetry or telecommand
    area_version=1           # 16 bits	Protocol version
    is_error_message=False      # 8 bit	Boolean value to indicate if is an error message (0x1 for true, 0x0 for false)

    def make_header(transaction_id):
        return struct.pack(header_format, timestamp,
                                6,
                                interaction_stage,
                                transaction_id,
                                service,
                                operation,
                                area_version,
                                is_error_message,
                                body_length)
    def make_CRC(header, body):
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
    
    header=make_header(transaction_id)
    crc=make_CRC(header,body_bits).to_bytes(2, 'little')
    message=header+body_bits+crc

    return message

def transaction_id():
    global transaction_id_counter
    transaction_id_counter += 1
    return transaction_id_counter 

#Add telemetrys to send and test 
transaction_id_counter = 0

with open('autoSend_Data.csv', 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    variable_titles = next(csvreader)

    while True:
        for row in csvreader:
            # Read the first row to get the variable titles
            mode =int(row[0])
            mode_bit_length = (mode.bit_length() + 7) // 8
            mode_byte_representation = mode.to_bytes(mode_bit_length, byteorder='little')
            mode_message=make_message(1,mode_byte_representation,mode_bit_length,transaction_id())
            socket_file_descriptor.sendto(mode_message, (ip,port))
            print(f'Sent: {mode_message.hex()}')
            time.sleep(0.5)
            
            profile = int(row[1])
            profile_bit_length = (profile.bit_length() + 7) // 8
            profile_byte_representation = profile.to_bytes(profile_bit_length, byteorder='little')
            profile_message=make_message(4,profile_byte_representation,profile_bit_length,transaction_id())
            socket_file_descriptor.sendto(profile_message, (ip,port))
            print(f'Sent: {profile_message.hex()}')
            time.sleep(0.5)

            battery_voltaje = float(row[2])
            battery_byte_representation = struct.pack('f', battery_voltaje)
            battery_byte_length = len(battery_byte_representation)
            battery_message=make_message(2,battery_byte_representation,battery_byte_length,transaction_id())
            socket_file_descriptor.sendto(battery_message, (ip,port))
            print(f'Sent: {battery_message.hex()}')
            time.sleep(0.5)

            x=float(row[3])
            y=float(row[4])
            z=float(row[5])
            byte_representation_x = struct.pack('f', x)
            byte_representation_y = struct.pack('f', y)
            byte_representation_z = struct.pack('f', z)
            byte_representation_accelerometer=byte_representation_x+byte_representation_y+byte_representation_z
            accelerometer_byte_length = len(byte_representation_accelerometer)
            accelerometer_message=make_message(3,byte_representation_accelerometer,accelerometer_byte_length,transaction_id())
            socket_file_descriptor.sendto(accelerometer_message, (ip,port))
            print(f'Sent: {accelerometer_message.hex()}')
            time.sleep(0.5)
        
            current1 =float(row[6])
            current1_byte_representation = struct.pack('f', current1)
            current1_byte_length = len(current1_byte_representation)
            current1_message=make_message(5,current1_byte_representation,current1_byte_length,transaction_id())
            socket_file_descriptor.sendto(current1_message, (ip,port))
            print(f'Sent: {current1_message.hex()}')
            time.sleep(0.5)

            current2 = float(row[7])
            current2_byte_representation = struct.pack('f', current2)
            current2_byte_length = len(current2_byte_representation)
            current2_message=make_message(6,current2_byte_representation,current2_byte_length,transaction_id())
            socket_file_descriptor.sendto(current2_message, (ip,port))
            print(f'Sent: {current2_message.hex()}')
            time.sleep(0.5)

            current3 = float(row[8])
            current3_byte_representation = struct.pack('f', current3)
            current3_byte_length = len(current3_byte_representation)
            current3_message=make_message(7,current3_byte_representation,current3_byte_length,transaction_id())
            socket_file_descriptor.sendto(current3_message, (ip,port))
            print(f'Sent: {current3_message.hex()}')
            time.sleep(0.5)

            current4 = float(row[9])
            current4_byte_representation = struct.pack('f', current4)
            current4_byte_length = len(current4_byte_representation)
            current4_message=make_message(8,current4_byte_representation,current4_byte_length,transaction_id())
            socket_file_descriptor.sendto(current4_message, (ip,port))
            print(f'Sent: {current4_message.hex()}')
            time.sleep(0.5)

            current5 = float(row[10])
            current5_byte_representation = struct.pack('f', current5)
            current5_byte_length = len(current5_byte_representation)
            current5_message=make_message(9,current5_byte_representation,current5_byte_length,transaction_id())
            socket_file_descriptor.sendto(current5_message, (ip,port))
            print(f'Sent: {current5_message.hex()}')
            time.sleep(0.5)

            current6 = float(row[11])
            current6_byte_representation = struct.pack('f', current6)
            current6_byte_length = len(current6_byte_representation)
            current6_message=make_message(10,current6_byte_representation,current6_byte_length,transaction_id())
            socket_file_descriptor.sendto(current6_message, (ip,port))
            print(f'Sent: {current6_message.hex()}')
            time.sleep(0.5)

            tempOBC = float(row[12])
            tempOBC_byte_representation = struct.pack('f', tempOBC)
            tempOBC_byte_length = len(tempOBC_byte_representation)
            tempOBC_message=make_message(13,tempOBC_byte_representation,tempOBC_byte_length,transaction_id())
            socket_file_descriptor.sendto(tempOBC_message, (ip,port))
            print(f'Sent: {tempOBC_message.hex()}')
            time.sleep(0.5)

            tempPDU = float(row[13])
            tempPDU_byte_representation = struct.pack('f', tempPDU)
            tempPDU_byte_length = len(tempPDU_byte_representation)
            tempPDU_message=make_message(14,tempPDU_byte_representation,tempPDU_byte_length,transaction_id())
            socket_file_descriptor.sendto(tempPDU_message, (ip,port))
            print(f'Sent: {tempPDU_message.hex()}')
            time.sleep(0.5)

            i2cCAN = int(row[14]) 
            i2cCAN_bit_length = (i2cCAN.bit_length() + 7) // 8
            i2cCAN_byte_representation = i2cCAN.to_bytes(i2cCAN_bit_length, byteorder='little')
            i2cCAN_message=make_message(12,i2cCAN_byte_representation,i2cCAN_bit_length,transaction_id())
            socket_file_descriptor.sendto(i2cCAN_message, (ip,port))
            print(f'Sent: {i2cCAN_message.hex()}')
            time.sleep(0.5)

            i2cBus = int(row[15]) 
            i2cBus_bit_length = (i2cBus.bit_length() + 7) // 8
            i2cBus_byte_representation = i2cBus.to_bytes(i2cBus_bit_length, byteorder='little')
            i2cBus_message=make_message(11,i2cBus_byte_representation,i2cBus_bit_length,transaction_id())
            socket_file_descriptor.sendto(i2cBus_message, (ip,port))
            print(f'Sent: {i2cBus_message.hex()}')
 
            time.sleep(2)
  