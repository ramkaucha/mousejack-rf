#include <fcntl.h>
#include <linux/usbdevice_fs.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <unistd.h>

int main(int argc, char **argv) {
  const char *filename;
  int fd;

  if (argc != 2) {
    fprintf(stderr, "Usage: %s /dev/bus/usb/BBB/DDD\n", argv[0]);
    return 1;
  }

  filename = argv[1];
  fd = open(filename, O_WRONLY);
  if (fd < 0) {
    perror("Error opening device");
    return 1;
  }

  printf("Restting USB device %s\n", filename);

  if (ioctl(fd, USBDEVFS_RESET, 0) < 0) {
    perror("Reset failed");
    return 1;
  }

  printf("Reset successful");
  close(fd);

  return 0;
}
