import sublime, sublime_plugin
import os.path
import os
import subprocess
from os.path import dirname, realpath

MY_PLUGIN = dirname(realpath(__file__))
s = {}


class PHPTools(sublime_plugin.EventListener):
    def __init__(self):
        self.php_path = "php"
        self.formatter_path = MY_PLUGIN + "/php.tools/codeFormatter.php"
        self.debug = True
        self.psr = False

    def on_post_save_async(self, view):
        s = sublime.load_settings('PHPTools.sublime-settings')
        print("Settings: ", s)
        self.php_path = s.get("php_path", "php")
        self.formatter_path = s.get("formatter_path", MY_PLUGIN + "/php.tools/codeFormatter.php")
        self.debug = s.get("debug", False)
        self.psr = s.get("psr", False)

        full_file_name = view.file_name()
        folder_name, file_name = os.path.split(full_file_name)
        folder_name = folder_name.replace(" ", "\\ ")
        extension = os.path.splitext(full_file_name)[1][1:]

        if self.debug:
            print("ex ", extension, "folder: ", folder_name)

        psr_toggle = ""
        if self.psr:
            psr_toggle = "--psr"

        if "php" != extension:
            return False

        full_file_name_tmp = full_file_name + "-tmp"
        cmd = "\"{}\" \"{}\" {} \"{}\" > \"{}\"; \"{}\" -l \"{}\" && mv \"{}\" \"{}\";".format(
            self.php_path,
            self.formatter_path,
            psr_toggle,
            full_file_name,
            full_file_name_tmp,
            self.php_path,
            full_file_name_tmp,
            full_file_name_tmp,
            full_file_name
        )
        PHPTools().run(cmd, folder_name)

    def run(self, cmd, folder_name):
        if self.debug:
            print("Cmd ", cmd)

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder_name, shell=True)
        result, err = p.communicate()
        if self.debug:
            if err:
                print("Error: ", err)
            else:
                print("Result: ", result)
