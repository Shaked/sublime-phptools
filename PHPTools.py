import sublime, sublime_plugin
import threading
import os.path
import os
import subprocess
from os.path import dirname, realpath

MY_PLUGIN = dirname(realpath(__file__))
def plugin_loaded():
    global s
    s = sublime.load_settings('PHPTools.sublime-settings')
    print("Settings: ", s)

class PHPTools(sublime_plugin.EventListener):

    def on_post_save_async(self, view):
        full_file_name = view.file_name()
        folder_name, file_name = os.path.split(full_file_name)
        extension = os.path.splitext(full_file_name)[1][1:]
        print("ex ", extension)
        if "php" != extension:
            return False

        full_file_name_tmp = full_file_name + "-tmp"
        bin_php = s.get("php_path", "php")
        formatter_path = s.get("formatter_path", MY_PLUGIN + "/php.tools/codeFormatter.php")
        cmd = "{} {} {} > {}; mv {} {};".format(
            bin_php,
            formatter_path,
            full_file_name,
            full_file_name_tmp,
            full_file_name_tmp,
            full_file_name
        )
        PHPTools().run(cmd, folder_name)

    def run(self, cmd, folder_name):
        print("Cmd ", cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder_name, shell=True)
        result, err = p.communicate()
        if err:
            print("Error: ", err)
        else:
            print("Result: ", result)
