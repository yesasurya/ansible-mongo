import sys


def check_if_entry_already_exist(hostname, lines):
  for line in lines:
    if hostname in line:
      return True
  return False


if __name__ == '__main__':
  arg_length = len(sys.argv)
  entries = {}
  for i in range(1, arg_length, 2):
    ip_addr = sys.argv[i]
    hostname = sys.argv[i + 1]
    entries[ip_addr] = hostname

  with open('/etc/hosts', 'r+') as hostfile:
    lines = hostfile.readlines()
    valid_entries = {}
    for ip_addr, hostname in entries.items():
      if not check_if_entry_already_exist(hostname, lines):
        valid_entries[ip_addr] = hostname

    for ip_addr, hostname in valid_entries.items():
      hostfile.write('{0} {1}\n'.format(ip_addr, hostname))
