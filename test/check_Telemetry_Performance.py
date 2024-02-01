import sys
import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_src_dir = os.path.abspath(os.path.join(current_dir, os.pardir, 'app'))
sys.path.append(parent_src_dir)

from db_interface import DB_Interface
from telemetry_manager import TelemetryManager
import threading
import queue

udp_packet_queue = queue.Queue()
TM_manager=TelemetryManager()
database=DB_Interface("192.168.68.63")


def udp_listener():
    # Thread for saving in queue udp packages
    while True:
        data = TM_manager.receiveTelemetries()
        if data:
            udp_packet_queue.put(data)
            print("Received data:", data.name)


def main():
    # Create a thread for the UDP listener
    udp_thread = threading.Thread(target=udp_listener)
    udp_thread.daemon = True
    udp_thread.start()

    while True:
        try:
            telemetry = udp_packet_queue.get(0.5)  # Timeout to periodically check for data
        except queue.Empty:
            continue  # No data in the queue, continue checking
        else:
            database.writeData(telemetry)
            print("Saved data:", telemetry.name)
            udp_packet_queue.task_done()

if __name__ == "__main__":
    main()
