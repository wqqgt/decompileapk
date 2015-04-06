import os
import zipfile

''' if this script run failed ,please run Apktool and report Error
to wangguotao@baidu.com
https://code.google.com/p/smali/wiki/TypesMethodsAndFields'''
BASE_PATH=os.getcwd()
JDGUI_PATH='/JD_GUI.app/Contents/MacOS/jd-gui'
DEX2JAR_PATH='/dex2jar/dex2jar.sh'
APKTOOLS_PATH='/apktool.sh'
TEST_FILE_PATH='/apks/kuaituliulan.apk'


def RunToolsWithCommand(tools_path, command):
    cmd = tools_path+' '+command
    os.system(cmd)
    print 'run command ' +cmd+' finished'

def DecomplieRun():
    '''get resource file'''
    cur_apktools = BASE_PATH+APKTOOLS_PATH
    cur_apktools_command = 'd '+BASE_PATH+TEST_FILE_PATH
    RunToolsWithCommand(cur_apktools, cur_apktools_command)
    cur_dex2jar = BASE_PATH+DEX2JAR_PATH
    cur_dex_path = UnzipApk(BASE_PATH+TEST_FILE_PATH)
    cur_dex2jar_command = cur_dex_path+'/classes.dex'
    RunToolsWithCommand(cur_dex2jar, cur_dex2jar_command)
    cur_jdgui = BASE_PATH+JDGUI_PATH
    cur_jdgui_command = cur_dex_path+'/classes_dex2jar.jar'
    RunToolsWithCommand(cur_jdgui, cur_jdgui_command)
    print 'all finished'

def RemoveSmaliDir():
    os.removedirs()

def UnzipApk(apk_path):
    fh = open(apk_path, 'rb')
    z = zipfile.ZipFile(fh)
    dex_path = BASE_PATH+'/'+'dex_file'
    for name in z.namelist():
        if (name=="classes.dex"):
            z.extract(name, dex_path)
    fh.close()
    return dex_path

DecomplieRun()
