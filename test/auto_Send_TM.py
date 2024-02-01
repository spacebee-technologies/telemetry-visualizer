import socket
import struct
import time

ip="192.168.68.63"
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
    global transaction_id
    transaction_id += 1
    return transaction_id

#Add telemetrys to send and test 
transaction_id=0
while True:
    mode = 1  
    mode_bit_length = mode.bit_length()
    mode_bit_length = (mode_bit_length + 7) // 8
    mode_byte_representation = mode.to_bytes(mode_bit_length, byteorder='little')
    mode_message=make_message(1,mode_byte_representation,mode_bit_length,transaction_id())
    socket_file_descriptor.sendto(mode_message, (ip,port))
    print(f'Sent: {mode_message.hex()}')
    time.sleep(1)



    battery_voltaje = 11.9 
    battery_byte_representation = struct.pack('f', battery_voltaje)
    battery_byte_length = len(battery_byte_representation)

    battery_message=make_message(2,battery_byte_representation,battery_byte_length,transaction_id())
    socket_file_descriptor.sendto(battery_message, (ip,port))
    print(f'Sent: {battery_message.hex()}')
    time.sleep(1)
    for i in range(0,10,1):
        x=10.2+i
        y=2.6
        z=3.0
        byte_representation_x = struct.pack('f', x)
        byte_representation_y = struct.pack('f', y)
        byte_representation_z = struct.pack('f', z)

        byte_representation_accelerometer=byte_representation_x+byte_representation_y+byte_representation_z

        accelerometer_byte_length = len(byte_representation_accelerometer)
        accelerometer_message=make_message(3,byte_representation_accelerometer,accelerometer_byte_length,transaction_id())
        socket_file_descriptor.sendto(accelerometer_message, (ip,port))
        print(f'Sent: {accelerometer_message.hex()}')
        time.sleep(1)