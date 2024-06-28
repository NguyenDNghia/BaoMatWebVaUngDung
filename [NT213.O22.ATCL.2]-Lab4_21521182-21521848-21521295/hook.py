import frida
import time

device = frida.get_usb_device()
pid = device.spawn("com.android.insecurebankv2")
device.resume(pid)

time.sleep(1) # sleep 1 to avoid crash (sometime)

session=device.attach(pid)


hook_script = """
Java.perform(function () {
    var PostLogin = Java.use('com.android.insecurebankv2.PostLogin');

    PostLogin.doesSuperuserApkExist.implementation = function (path) {
        console.log('doesSuperuserApkExist was called with path: ' + path);
        return false; 
    };
    
    PostLogin.doesSUexist.implementation = function () {
        console.log('doesSUexist was called');
        return false; 
    };
});
"""
script = session.create_script(hook_script)
script.load()
input('...?') # prevent terminat