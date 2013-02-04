import cherrypy
import os
import time
import glob
import json
import urllib

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 80,
                                              })

def get_immediate_subdirectories(dir) :
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]



class HelloWorld(object):

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

root = HelloWorld()


#root.foo = foo


cherrypy.quickstart(root)
