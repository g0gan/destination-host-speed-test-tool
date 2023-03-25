import subprocess
import time

def test_speed(dest_host, timeout):
    start_time = time.time()
    try:
        result = subprocess.run(['ping', '-n', '1', '-w', str(timeout), dest_host], capture_output=True, text=True)
        if 'Reply from' in result.stdout:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Connection to {dest_host} successful. Time taken: {elapsed_time:.2f} seconds.")
        else:
            print(f"Connection to {dest_host} failed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__