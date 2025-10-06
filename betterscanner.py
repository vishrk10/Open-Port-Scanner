#!/usr/bin/env python3
import socket, threading, sys, time

def parse_ports(s):
    if not s: return list(range(1,1025))
    parts = s.split(',')
    pset = set()
    for part in parts:
        if '-' in part:
            a,b = part.split('-'); pset.update(range(int(a), int(b)+1))
        else:
            pset.add(int(part))
    return sorted(x for x in pset if 1 <= x <= 65535)

def scan(ip, port, timeout, sem, banner):
    with sem:
        s = socket.socket()
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            b = ""
            if banner:
                try:
                    s.settimeout(0.8)
                    b = s.recv(1024).decode(errors='ignore').strip()
                except: pass
            print(f"{port}/tcp OPEN{(' - '+b) if b else ''}")
        except: pass
        finally:
            try: s.close()
            except: pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 mini_scan.py target [ports] [threads]"); sys.exit(1)
    target = sys.argv[1]
    ports_arg = sys.argv[2] if len(sys.argv) > 2 else ""
    threads = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    banner = ("--banner" in sys.argv)
    try:
        ip = socket.gethostbyname(target)
    except Exception as e:
        print("Resolve error:", e); sys.exit(1)

    ports = parse_ports(ports_arg)
    sem = threading.Semaphore(threads)
    start = time.time()
    for p in ports:
        t = threading.Thread(target=scan, args=(ip, p, 1.0, sem, banner), daemon=True)
        t.start()
    # wait for threads (simple)
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread: continue
        t.join()
    print(f"Done. Scanned {len(ports)} ports in {time.time()-start:.2f}s")
