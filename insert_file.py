import sublime, sublime_plugin
import os

class InsertFileCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.find_templates()
        self.window.show_quick_panel(self.templates, self.template_selected)
    
    def find_templates(self):
        self.templates = []
        self.template_paths = []

        for root, dirnames, filenames in os.walk('/path_to_forms_directory'):
            for filename in filenames:
                if filename.endswith(".tex"): # extension / suffix of user form files
                    self.template_paths.append(os.path.join(root, filename))
                    self.templates.append(os.path.basename(root) + ": " + os.path.splitext(filename)[0])

    def template_selected(self, selected_index):
        if selected_index != -1:
            self.template_path = self.template_paths[selected_index]

            print "\n" * 25
            print "----------------------------------------------------------------------------------------\n"
            print ("Inserting File:  " + self.template_path + "\n")
            print "----------------------------------------------------------------------------------------\n"

            template = open(self.template_path).read()

            print template

            view = self.window.run_command("insert_snippet", {'contents': template})

            sublime.status_message("Inserted File: %s" % self.template_path)