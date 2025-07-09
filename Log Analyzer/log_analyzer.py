from collections import Counter

def analyze_log(file_path):
    log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    level_counter = Counter()

    try:
        with open(file_path, 'r') as log_file:
            lines = log_file.readlines()

            print("Last 5 log entries:")
            for line in lines[-5:]:
                print(line.strip())

            for line in lines:
                for level in log_levels:
                    if f'- {level} -' in line:
                        level_counter[level] += 1
                        break

        print("Log Summary:")
        for level in log_levels:
            print(f"{level}: {level_counter[level]} entries")

    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
    except Exception as e:
        print(f"Error while analyzing log: {e}")

if __name__ == '__main__':
    analyze_log('app.log')