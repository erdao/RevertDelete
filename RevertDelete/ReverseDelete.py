import sublime
import sublime_plugin

class ReverseDeleteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel_regions = []
        for sel_region in self.view.sel():
            sel_regions.append(sel_region)
        for sel_region in sel_regions:
            if not sel_region.empty():
                lines=self.view.split_by_newlines(sel_region)
                for line in lines:
                    modifyLine=self.view.line(line)
                    curLine=self.view.substr(modifyLine)
                    newLine= ''+curLine[1:]
                    self.view.replace(edit,modifyLine,newLine)