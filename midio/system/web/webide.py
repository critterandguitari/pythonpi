import cherrypy
import os
import time
import glob
import json

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 80,
                                              })

def get_immediate_subdirectories(dir) :
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]



class HelloWorld(object):

    def foo(self, p):
        return 'Foo!' + p
    foo.exposed = True


    def index(self):
        
        print "loading patches..."
        patches = []
        patch_folders = get_immediate_subdirectories('../../patches/')

        for patch_folder in patch_folders :
            patch_name = str(patch_folder)
            patch_path = '../../patches/'+patch_name+'/'+patch_name+'.py'
            patches.append(patch_path)

        return json.dumps(patches)

        index.exposed = True

root = HelloWorld()


#root.foo = foo


cherrypy.quickstart(root)
