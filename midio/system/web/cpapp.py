import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))
import os
import time
import glob
import json
import cherrypy
import urllib

# setup UDP socket for sending data to vsynth program
import time
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP




def get_immediate_subdirectories(dir) :
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]



class Root():

    # /patch/patch-name  loads patch
    def patch(self, p):
        patch_path = '../../patches/'+p+'/'+p+'.py'
        patch = open(patch_path, 'r').read()
        return patch
    
    patch.exposed = True


    def save(self, name, contents):
        p = name
       # patch_path = '../../patches/'+p+'/'+p+'.py'
       # with open(patch_path, "w") as text_file:
       #     text_file.write(contents)
       # return "SAVED " + name
        
        global sock
        sock.sendto(contents, (UDP_IP, UDP_PORT))
    save.exposed = True

    # returns list of all the patches
    def index(self):
        
        print "loading patches..."
        patches = []
        patch_folders = get_immediate_subdirectories('../../patches/')

        for patch_folder in patch_folders :
            patch_name = str(patch_folder)
            patch_path = '../../patches/'+patch_name+'/'+patch_name+'.py'
            patches.append(urllib.quote(patch_name))

        return json.dumps(patches)

    index.exposed = True


