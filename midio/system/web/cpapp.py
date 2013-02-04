import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))
import os
import time
import glob
import json
import cherrypy
import urllib

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


