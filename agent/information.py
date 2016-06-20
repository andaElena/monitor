import wmi
def get_totalDiskSpace(machine):
	"""Return total disk space."""
	totalDiskSpace=0
	for disk in machine.Win32_LogicalDisk(DriveType=3):
		totalDiskSpace+=(float(disk.Size)/pow(2,30))
	return float(totalDiskSpace)
def get_freeDiskSpace(machine):
	"""Return free disk space."""
	freeDiskSpace=0
	for disk in machine.Win32_LogicalDisk(DriveType=3):
		freeDiskSpace+=(float(disk.freeSpace)/pow(2,30))
	return float(freeDiskSpace)
def get_cpuLoadPercentage(machine):
	"""Return cpu load percentage."""
	cpuLoad=0
	for cpu in machine.Win32_Processor():
		cpuLoad=cpu.LoadPercentage
	return cpuLoad
def get_totalMemory(machine):
	"""Return total physica memory."""
	totalMemory=0
	for computerSystem in machine.Win32_ComputerSystem():
   		totalMemory+=long(computerSystem.TotalPhysicalMemory)
   	totalMemory=float(totalMemory)/pow(2,30)
   	return totalMemory
def get_freeMemory(machine):
	"""Return free physical memory."""
	freeMemory=0
	for operatingSystem in machine.Win32_OperatingSystem():
		freeMemory+=int(operatingSystem.FreePhysicalMemory)
	freeMemory=float(freeMemory)/pow(2,20)
	return freeMemory