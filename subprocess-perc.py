newlines = ['\n', '\r\n', '\r']
def unbuffered(proc, stream='stdout'):
    	stream = getattr(proc, stream)
    #with contextlib.closing(stream):
        while True:
            out = []
            last = stream.read(1)
            if last == '' and proc.poll() is not None:
                break
            while last not in newlines:
                if last == '' and proc.poll() is not None:
                    break
                out.append(last)
                last = stream.read(1)
            out = ''.join(out)
            yield out
 
def example():
    cmd = ['rpm', '-ivh', '/home/fish-2.0.0-201305151006.1.x86_64.rpm','--percent']
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        # Make all end-of-lines '\n'
        universal_newlines=True,
    )


    for line in unbuffered(proc):
         	print "per compled", line

example()
