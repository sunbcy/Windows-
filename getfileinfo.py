#-*-coding:utf-8-*-
import win32api
import pprint

def getFileProperties(fname):
    """read file's all properties and return as a dict."""
    propNames=('Comments',InternalName','productName','companyName','LegalCopyright','ProductVersion','FileDescription','LegalTrademarks','PrivateBuild','FileVersion','OriginalFilename','SpecialBuild')

    props={'FixedFileInfo':None,'StringFileInfo':None,'FileVersion':None}

    try:
        fixedInfo=win32api.GetFileVersionInfo(fname,'\\')
        props['FixedFileInfo']=fixedInfo
        props['FileVersion']="%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] /65536,fixedInfo['FileVersionMS'] %65536,fixedInfo['FileVersionLS'] / 65536,fixedInfo['FileVersionLS'] %65536)
        lang,codepage=win32api.GetFileVersionInfo(fname,'\\VarFileInfo\\Translation')[0]
        strInfo={}
        for propName in propNames:
            strInfoPath=u'\\StringFileInfo\\%04X%04X\\%s' % (lang,codepage,propName)
            strInfo[propName]=win32api.getFileVersionInfo(fname,strInfoPath)
        props['StringFileInfo']=strInfo
    except:
        pass
    return props

if __name__=='__main__':
    exe_path='xxx'
    pprint.pprint(getFileProperties(exe_path))
